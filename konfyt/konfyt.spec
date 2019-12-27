# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 e9090061125b6ebc587230ac4d88721434e00a73
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    konfyt
Version: 1.1.0
Release: 1%{?dist}
Summary: A patch manager
URL:     https://github.com/noedigcode/konfyt
Group:   Applications/Multimedia

License: GPLv2+

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: https://github.com/noedigcode/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++ sed
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: Carla-devel 
BuildRequires: liblscp-devel 
BuildRequires: fluidsynth-devel

%description
Konfyt is a digital keyboard workstation for Linux which allows you to set up
patches, each with multiple layers, and instantly switch between these patches
for live keyboard playing. Patches may consist of multiple layers of soundfonts
(.sf2), SFZs, audio input ports and MIDI output ports. Konfyt features a library
which scans the filesystem for and allows quick access to soundfont programs and
SFZs.

%prep
%setup -qn %{name}-%{commit0}

%ifarch x86_64
sed -i -e "s/usr\/lib/usr\/lib64/g" konfyt.pro
%endif

sed -i -e "/AudioVideo/d" desktopentry/konfyt.desktop
sed -i -e "s/\/home\/gideon\/bin\///g" desktopentry/konfyt.desktop

%build

qmake-qt5 konfyt.pro
make VERBOSE=1 %{?_smp_mflags}

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 desktopentry/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 %{name} %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/

%__install -m 644 icons/konfyt\ 16.png  %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%__install -m 644 icons/konfyt\ 32.png  %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%__install -m 644 icons/konfyt\ 64.png  %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%__install -m 644 icons/konfyt\ 128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# install konfyt.desktop properly.
desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --add-category=X-Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
update-desktop-database &> /dev/null

%postun
update-desktop-database &> /dev/null

%files
%doc COPYING README.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Fri Dec 27 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file 1.1.0
