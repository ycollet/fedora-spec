# Global variables for github repository
%global commit0 4dff4d6e48e2b95a188755facddbe373932ae8b1
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    moony.lv2
Version: 0.34.0
Release: 1%{?dist}
Summary: Realtime Lua as programmable glue in LV2
URL:     https://github.com/OpenMusicKontrollers/moony.lv2
License: GPLv2+

Source0: https://github.com/OpenMusicKontrollers/moony.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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

VERBOSE=1 meson --prefix=/usr -Dlv2libdir=%{_lib}/lv2 build
cd build
VERBOSE=1 %ninja_build 

%install
cd build
VERBOSE=1 %ninja_install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.34.0-1
- Initial spec file
