# Global variables for github repository
%global commit0 70f3794ad7a79e3764c5d90ec1eddc372a76a7c4
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         sherlock.lv2
Version:      0.16.0
Release:      2%{?dist}
Summary:      An investigative LV2 plugin bundle
URL:          https://github.com/OpenMusicKontrollers/sherlock.lv2
Source0:      https://github.com/OpenMusicKontrollers/sherlock.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: sratom-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: flex
BuildRequires: meson

%description
An investigative LV2 plugin bundle

%prep
%setup -qn %{name}-%{commit0}

%build

VERBOSE=1 meson --prefix=/usr build
cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install
cd build
DESTDIR=%{buildroot} ninja install

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update for Fedora 29
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update to latest master
- switch to meson build
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-1
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.12.0
- Initial build
