# Global variables for github repository
%global commit0 d847c51287a4dd66d946acaac7222ec752dfb43a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    midi_matrix.lv2
Version: 0.22.0
Release: 3%{?dist}
Summary: A LV2 Plugin Bundle
Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/OpenMusicKontrollers/midi_matrix.lv2

Source0: https://github.com/OpenMusicKontrollers/midi_matrix.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: meson

%description
A LV2 Plugin Bundle

%prep
%setup -qn %{name}-%{commit0}

%build

LDFLAGS="${LDFLAGS:-%{build_ldflags}} -z muldefs" ; export LDFLAGS
VERBOSE=1 meson --prefix=/usr build
cd build

DESTDIR=%{buildroot} VERBOSE=1 ninja

%install

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_libdir}/lv2/*

%changelog
* Thu Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.22.0-3
- fix for Fedora 32

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.22.0-2
- update to 0.22.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to latest master

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.18.0
- Initial build
