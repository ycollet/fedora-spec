# Global variables for github repository
%global commit0 7452282d077a0ca685bee07b9f1a967d5b35bdaa
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    synthpod
Version: 0.1.0
Release: 3%{?dist}
Summary: Lightweight Nonlinear LV2 Plugin Container
URL:     https://github.com/OpenMusicKontrollers/synthpod
Group:   Applications/Multimedia
License: GPLv2+

Source0: https://github.com/OpenMusicKontrollers/synthpod/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
BuildRequires: mesa-libGL-devel
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

sed -i -e "s/asoundlib.h/alsa\/asoundlib.h/g" bin/synthpod_alsa.c

%build

VERBOSE=1 meson --prefix=/usr build
cd build

DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/*

%changelog
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
