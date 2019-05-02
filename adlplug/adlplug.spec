# Global variables for github repository
%global commit0 17f7fc5c810e1188eee494f1190e47f599479c30
%global gittag0 v1.0.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    adlplug
Version: 1.0.1
Release: 3%{?dist}
Summary: Synthesizer plugin for ADLMIDI (VST/LV2)
URL:     https://github.com/jpcima/ADLplug
Group:   Applications/Multimedia

License: BSL-1.0

# git clone https://github.com/jpcima/ADLplug
# git checkout v1.0.1
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz ADLplug.tar.gz ADLplug/*
# rm -rf ADLplug

Source0: ADLplug.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: libX11-devel libXft-devel libXrandr-devel libXinerama-devel libXcursor-devel

%description
Synthesizer plugin for ADLMIDI (VST/LV2)

%package -n opnplug
Summary:    Synthesizer plugin for OPNMIDI (VST/LV2)
Group:      Applications/Multimedia
Requires:   %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description -n opnplug
Synthesizer plugin for OPNMIDI (VST/LV2)

%prep

%setup -qn ADLplug

# For Fedora 29
%if 0%{?fedora} >= 29
  sed -i -e "114,125d" thirdparty/JUCE/modules/juce_graphics/colour/juce_PixelFormats.h
%endif

%build

mkdir -p build_adl
cd build_adl

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       ..

make VERBOSE=1 %{?_smp_mflags}

cd ..

mkdir -p build_opn
cd build_opn

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       -DADLplug_CHIP=OPN2 \
       ..

make VERBOSE=1 %{?_smp_mflags}

%install

cd build_adl

make DESTDIR=%{buildroot} install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/ADLplug.desktop

cd ..
cd build_opn

make DESTDIR=%{buildroot} install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/OPNplug.desktop

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
%{_bindir}/ADLplug
%{_libdir}/lv2/ADLplug.lv2/*
%{_libdir}/vst/ADLplug.so
%{_datadir}/applications/ADLplug.desktop
%{_datadir}/pixmaps/ADLplug.png
%{_datadir}/icons/hicolor/32x32/apps/ADLplug.png
%{_datadir}/icons/hicolor/96x96/apps/ADLplug.png

%files -n opnplug
%doc LICENSE README.md
%{_bindir}/OPNplug
%{_libdir}/lv2/OPNplug.lv2/*
%{_libdir}/vst/OPNplug.so
%{_datadir}/applications/OPNplug.desktop
%{_datadir}/pixmaps/OPNplug.png
%{_datadir}/icons/hicolor/32x32/apps/OPNplug.png
%{_datadir}/icons/hicolor/96x96/apps/OPNplug.png

%changelog
* Mon Apr 15 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.1
- update to 1.0.1

* Mon Mar 18 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- update to 1.0.0

* Sun Nov 11 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.4-3
- update to 1.0.0-beta.4.3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.3-3
- update for Fedora 29

* Thu Oct 11 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.3-3
- update to 1.0.0-beta.3-3

* Thu Oct 04 2018 Jean Pierre Cimalando <jp-dev.nospam@inbox.ru> - 1.0.0-beta.2-1
- update to latest master version
- update package summary
- remove a libcurl-devel dependency which became unnecessary

* Fri Sep 28 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1-2
- update to latest master version

* Sat Sep 22 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1-1
- Initial spec file
