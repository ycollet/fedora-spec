# Global variables for github repository
%global commit0 85ad5c0a760d4df07271afa7b9b7b75973bdca1f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    patchmatrix
Version: 0.20.0
Release: 2%{?dist}
Summary: A JACK patchbay in flow matrix style
URL:     https://github.com/OpenMusicKontrollers/patchmatrix
License: GPLv2+

Source0: https://github.com/OpenMusicKontrollers/patchmatrix/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: meson

%description
A JACK patchbay in flow matrix style

%prep
%autosetup -n %{name}-%{commit0}

%build

VERBOSE=1 meson --prefix=/usr build
cd build

VERBOSE=1 %ninja_build 

%install

cd build
VERBOSE=1 %ninja_install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to 0.26.0-2

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update to 0.16.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-1
- inital release
