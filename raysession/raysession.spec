%global __python %{__python3}

Name:    raysession
Version: 0.8.3
Release: 1%{?dist}
Summary: A JACK session manager

License: GPLv2+
URL:     https://github.com/Houston4444/RaySession

Source0: https://github.com/Houston4444/RaySession/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: python3-qt5-devel
BuildRequires: python3
BuildRequires: qtchooser
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: gtk-update-icon-cache
BuildRequires: desktop-file-utils

Requires(pre): python3-qt5
Requires(pre): python3-pyliblo

Obsoletes: RaySession

%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour, Carla,
QTractor, Non-Timeline, etc... It uses the same API as Non Session Manager, so
programs compatible with NSM are also compatible with Ray Session.
As Non Session Manager, the principle is to load together audio programs, then
be able to save or close all documents together.

%prep
%autosetup -n RaySession-%{version}

# Fix desktop categories
sed -i -e "s/AudioVideo;AudioEditing/Audio;Video/g" data/raysession.desktop
# Fix permission on executable python script
chmod a+x src/shared/jacklib.py

%build

%set_build_flags

%make_build PREFIX=/usr

%install

%make_install PREFIX=/usr

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/raysession/*

%changelog
* Wed Jun 17 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-1
- update to 0.8.3-1

* Thu Nov 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- update to 0.8.2-1

* Thu Oct 24 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Tue Oct 15 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Wed Jul 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.2-1
- update to 0.7.2-1

* Sat May 4 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- Initial spec file
