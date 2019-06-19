# Global variables for github repository
%global commit0 9e76db3f3e4b7dc7c304fd58591a352bb2b6c894
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    noise-suppression-for-voice
Version: 0.2.0
Release: 2%{?dist}
Summary: Real-time Noise Suppression LADSPA / LV2 Plugin
License: GPLv2+

URL:     https://github.com/werman/noise-suppression-for-voice
Source0: https://github.com/werman/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: ladspa-devel

%description
A real-time noise suppression LV2 / LADSPA plugin for voice based on Xiph's RNNoise - https://github.com/xiph/rnnoise.
More info about the base library - https://people.xiph.org/~jm/demo/rnnoise/.

%package -n ladspa-%{name}
Summary: Real-time Noise Suppression LADSPA Plugin
Group:   Applications/Multimedia

%package -n lv2-%{name}
Summary: Real-time Noise Suppression LV2 Plugin
Group:   Applications/Multimedia

%package -n %{name}-doc
Summary: Real-time Noise Suppression LADSPA / LV2 Plugin documentation
Group:   Applications/Multimedia

%description -n ladspa-%{name}
A real-time noise suppression LADSPA plugin for voice based on Xiph's RNNoise - https://github.com/xiph/rnnoise.
More info about the base library - https://people.xiph.org/~jm/demo/rnnoise/.

%description -n lv2-%{name}
A real-time noise suppression LV2 plugin for voice based on Xiph's RNNoise - https://github.com/xiph/rnnoise.
More info about the base library - https://people.xiph.org/~jm/demo/rnnoise/.

%description -n %{name}-doc
Documentation related to the real-time noise suppression plugin for voice based on Xiph's RNNoise.

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/ARCHIVE DESTINATION \${CMAKE_INSTALL_LIBDIR}/ARCHIVE DESTINATION \${CMAKE_INSTALL_LIBDIR}\/ladspa/g" src/ladspa_plugin/CMakeLists.txt
sed -i -e "s/LIBRARY DESTINATION \${CMAKE_INSTALL_LIBDIR}/LIBRARY DESTINATION \${CMAKE_INSTALL_LIBDIR}\/ladspa/g" src/ladspa_plugin/CMakeLists.txt

sed -i -e "s/ARCHIVE DESTINATION \${CMAKE_INSTALL_LIBDIR}/ARCHIVE DESTINATION \${CMAKE_INSTALL_LIBDIR}\/lv2\/rnnoise\.lv2/g" src/lv2_plugin/CMakeLists.txt
sed -i -e "s/LIBRARY DESTINATION \${CMAKE_INSTALL_LIBDIR}/LIBRARY DESTINATION \${CMAKE_INSTALL_LIBDIR}\/lv2\/rnnoise\.lv2/g" src/lv2_plugin/CMakeLists.txt

%build

%cmake -DLIBINSTDIR=lib64 \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

%files -n %{name}-doc
%doc README.md LICENSE

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Apr 15 2019 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-2
- build ladspa and lv2 packages

* Mon Apr 15 2019 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial version
