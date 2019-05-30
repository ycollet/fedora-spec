# Global variables for github repository
%global commit0 59baeb86b8851f521bc8162e22e3f15061662cc3
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    ensemble-chorus
Version: 0.0.1
Release: 1%{?dist}
Summary: Effect plugin for ensemble-chorus (VST/LV2)
URL:     https://github.com/jpcima/ensemble-chorus
Group:   Applications/Multimedia

License: BSL-1.0

# git clone https://github.com/jpcima/ensemble-chorus
# #git checkout v1.0.1
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz ensemble-chorus.tar.gz ensemble-chorus/*
# rm -rf ensemble-chorus

Source0: ensemble-chorus.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: libX11-devel libXft-devel libXrandr-devel libXinerama-devel libXcursor-devel

%description
Effect plugin for ensemble-chorus (VST/LV2)

%prep

%setup -qn ensemble-chorus

# For Fedora 29
%if 0%{?fedora} >= 29
  sed -i -e "114,125d" thirdparty/JUCE/modules/juce_graphics/colour/juce_PixelFormats.h
%endif
%ifarch x86_64
  sed -i -e "s/lib\/lv2/lib64\/lv2/g" CMakeLists.txt
  sed -i -e "s/lib\/vst/lib64\/vst/g" CMakeLists.txt
%endif

sed -i -e "s/AudioMidi;//g" resources/desktop/ensemble_chorus.desktop

%build

mkdir -p build
cd build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       ..

make VERBOSE=1 %{?_smp_mflags}

cd ..

%install

cd build

make DESTDIR=%{buildroot} install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/ensemble_chorus.desktop

%post

touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun

update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans

/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%doc LICENSE README.md
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_datadir}/applications/ensemble_chorus.desktop
%{_datadir}/pixmaps/ensemble_chorus.png
%{_datadir}/pixmaps/ensemble_chorus.xpm

%changelog

* Thu May 30 2019 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
