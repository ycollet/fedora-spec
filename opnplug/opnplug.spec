# Global variables for github repository
%global commit0 4693b43e9ae1db35e2ea2dd0f55486f9c59766d4
%global gittag0 v1.0.0-beta.2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:        opnplug
Version:     1.0.0.b2
Release:     1%{?dist}
Summary:     Synthesizer plugin for OPNMIDI (VST/LV2)
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

%description
Synthesizer plugin for OPNMIDI (VST/LV2)

%prep

%setup -qn ADLplug

%build

mkdir -p build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       -DADLplug_CHIP=OPN2 \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

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
%{_bindir}/OPNplug
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_datadir}/applications/OPNplug.desktop
%{_datadir}/pixmaps/OPNplug.png

%changelog
* Thu Oct 04 2018 Jean Pierre Cimalando <jp-dev.nospam@inbox.ru> - 1.0.0-beta.2-1
- Initial spec file
