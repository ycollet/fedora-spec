# Global variables for github repository
%global commit0 c6cd3720b987f73ed5f412db9607433b3769f1db
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    synthpod
Version: 0.1.1
Release: 3%{?dist}
Summary: Lightweight Nonlinear LV2 Plugin Container
URL:     https://github.com/OpenMusicKontrollers/synthpod
License: GPLv2+

Source0: https://github.com/OpenMusicKontrollers/synthpod/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++ sed
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: sratom-devel
BuildRequires: nanomsg-devel
BuildRequires: efl-devel
BuildRequires: elementary-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-xrm-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libuv-devel
BuildRequires: meson
BuildRequires: cairo-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: alsa-lib-devel
BuildRequires: libevdev-devel

%description
Lightweight Nonlinear LV2 Plugin Container

%prep
%setup -qn %{name}-%{commit0}

%build

VERBOSE=1 meson --prefix=/usr -Dlv2libdir=%{_lib}/lv2 build
cd build
VERBOSE=1 %ninja_build 

%install 

cd build
VERBOSE=1 %ninja_install

%files
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/*

%changelog
* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-3
- update to last master version - c6cd3720b987f73ed5f412db9607433b3769f1db

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-3
- update to 0.1.0-3

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- fixe for Fedora 31

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0
- Initial build
