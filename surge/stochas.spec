%global debug_package %{nil}

Name:    stochas
Version: 0.0.1
Release: 1%{?dist}
Summary: A VST3 MIDI sequencer
License: GPLv2+

# Use ./source-stochas.sh to get the sources (latest master for now)

URL:     https://github.com/surge-synthesizer/stochas
Source0: stochas.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: rsync
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: jack-audio-connection-kit-devel
#BuildRequires: cairo-devel
#BuildRequires: libX11-devel
#BuildRequires: libxkbcommon-x11-devel
#BuildRequires: xcb-util-cursor-devel
#BuildRequires: xcb-util-keysyms-devel
#BuildRequires: xcb-util-devel

%description
A VST3 MIDI sequencer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/find_package/#find_package/g" cmake/versiontools.cmake

%build

%set_build_flags

mkdir build
cd build

%cmake cmake -DCMAKE_STRIP="true" -DCMAKE_C_FLAGS="$CFLAGS" -DCMAKE_CXX_FLAGS="$CXXFLAGS" ..

%make_build

%install 

cd build

%__install -m 755 -d %{buildroot}%{_libdir}/vst3/
%__install -m 644 -p stochas_artefacts/VST3/Stochas.vst3/Contents/x86_64-linux/*.so %{buildroot}/%{_libdir}/vst3/	

%__install -m 755 -d %{buildroot}%{_bindir}/
%__install -m 644 -p stochas_artefacts/Standalone/Stochas %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Aug 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
