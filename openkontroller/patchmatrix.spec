# Global variables for github repository
%global commit0 b4a060046bdf5af61ad145dd2f6c2a59a172082b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    patchmatrix
Version: 0.12.0
Release: 2%{?dist}
Summary: A JACK patchbay in flow matrix style
URL:     https://github.com/OpenMusicKontrollers/patchmatrix
Group:   Applications/Multimedia
License: GPLv2+

Source0: https://github.com/OpenMusicKontrollers/patchmatrix/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
%setup -qn %{name}-%{commit0}

%build

VERBOSE=1 meson --prefix=/usr build
cd build

DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-1
- inital release
