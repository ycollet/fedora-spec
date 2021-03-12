Name:    linux-show-player
Version: 0.5.2
Release: 1%{?dist}
Summary: A Cue player designed for stage productions

License: GPLv2+
URL:     https://github.com/FrancescoCeruti/linux-show-player

Source0: https://github.com/FrancescoCeruti/linux-show-player/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-setuptools

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

Requires: python3-gobject
Requires: python3-qt5-base
Requires: python3-mido
Requires: portmidi
Requires: python-jack-client
Requires: gstreamer1-plugins-good
Requires: gstreamer1-libav
Requires: python3-sortedcontainers

%description
Linux Show Player (LiSP) - Sound player designed for stage productions.

%prep
%autosetup -n %{name}-%{version}

%build

%py3_build

%install

%py3_install

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 755 -d %{buildroot}%{_datadir}/pixmaps
install -m 755 -d %{buildroot}%{_datadir}/mime/packages

install -m 644 dist/linuxshowplayer.desktop %{buildroot}%{_datadir}/applications
install -m 644 dist/linuxshowplayer.png %{buildroot}%{_datadir}/pixmaps
install -m 644 dist/linuxshowplayer.xml %{buildroot}%{_datadir}/mime/packages
  
desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/linuxshowplayer.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*
%{python3_sitelib}/*

%changelog
* Fri Mar 12 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- Initial spec file
