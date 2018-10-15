# Global variables for github repository
%global commit0 bbefb4cfef159681fe68db34cab0585b6b7a2ebc
%global gittag0 v1.0.0-beta.3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    adlplug
Version: 1.0.0.b3
Release: 2%{?dist}
Summary: Synthesizer plugin for ADLMIDI (VST/LV2)
URL:     https://github.com/jpcima/ADLplug
Group:   Applications/Multimedia

License: BSL-1.0

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

%files -n opnplug
%doc LICENSE README.md
%{_bindir}/OPNplug
%{_libdir}/lv2/OPNplug.lv2/*
%{_libdir}/vst/OPNplug.so
%{_datadir}/applications/OPNplug.desktop
%{_datadir}/pixmaps/OPNplug.png

%changelog
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
