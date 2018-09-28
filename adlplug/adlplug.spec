# Global variables for github repository
%global commit0 6a2322630bc7861b6316867703186d002a5070be
%global gittag0 v1.0.0-beta.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:        adlplug
Version:     1.0.0.b1
Release:     2%{?dist}
Summary:     Linux MultiMedia Studio
URL:         https://github.com/jpcima/ADLplug
Group:       Applications/Multimedia

License: BSL-1.0

Source0: ADLplug.tar.gz

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: libX11-devel libXft-devel libXrandr-devel libXinerama-devel libXcursor-devel
BuildRequires: libcurl-devel

%description
Synthesizer plugin for ADLMIDI and OPNMIDI (VST/LV2)

%prep

%setup -qn ADLplug

%build

mkdir -p build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install
  
desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/ADLplug.desktop

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
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_datadir}/applications/ADLplug.desktop
%{_datadir}/pixmaps/ADLplug.png

%changelog
* Fri Sep 28 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1-2
- update to latest master version
* Sat Sep 22 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1-1
- Initial spec file
