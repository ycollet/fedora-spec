# Global variables for github repository
%global commit0 4f5c779b961c7a4898a642002fe81cbe8115f50e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    sherlock.lv2
Version: 0.26.0
Release: 3%{?dist}
Summary: An investigative LV2 plugin bundle
URL:     https://github.com/OpenMusicKontrollers/sherlock.lv2
License: GPLv2+

Source0: https://github.com/OpenMusicKontrollers/sherlock.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: sratom-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: flex
BuildRequires: meson

%description
An investigative LV2 plugin bundle

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

VERBOSE=1 meson --prefix=/usr -Dlv2libdir=%{_lib}/lv2 build
cd build
VERBOSE=1 %ninja_build 

%install
cd build
VERBOSE=1 %ninja_install

%files
%doc README.md ChangeLog
%license COPYING
%{_libdir}/lv2/*

%changelog
* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.26.0-3
- update to 0.26.0-3

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.24.0-3
- update to 0.24.0-3

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.24.0-2
- update to 0.24.0-2

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to 0.20.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.12.0
- Initial build
