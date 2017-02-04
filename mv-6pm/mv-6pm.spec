# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:         6PM
Version:      0.9
Release:      1%{?dist}
Summary:      A Jack audio synthetizer
URL:          http://sourceforge.net/projects/mv-6pm/
Group:        Applications/Multimedia

License:      GPLv2+

Source0:      6PM_v0.9.tgz
Source1:      mv-6pm.desktop
Patch1:       mv-6pm-use-global-presets.patch

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Location)
BuildRequires: pkgconfig(Qt5OpenGL)

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel

%description
6PM is a phase modulation (PM) synthesizer made of six oscillators. 

%prep
%setup -qn %{name}_v%{version}


%build

cd src
qmake-qt5 6PM.pro
make VERBOSE=1 %{?_smp_mflags}

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_datadir}/mv-6pm/
%__install -m 755 -d %{buildroot}/%{_datadir}/mv-6pm/MidiMaps
%__install -m 755 -d %{buildroot}/%{_datadir}/mv-6pm/Presets
%__cp -r MidiMaps/* %{buildroot}%{_datadir}/mv-6pm/MidiMaps/
%__cp -r Presets/* %{buildroot}%{_datadir}/mv-6pm/Presets/

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 src/6pm %{buildroot}%{_bindir}/%{name}

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 src/images/icon.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install mv-6pm.desktop properly.
desktop-file-install --vendor '' \
        --add-category X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

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
%doc README Changelog LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mv-6pm/*
%{_datadir}/icons/hicolor/*


%changelog
* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial spec file 0.5.0
