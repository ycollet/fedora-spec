# Global variables for github repository
%global commit0 0f58f7b60413d3f81a54de6c7faeddc81d46817e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         sherlock.lv2
Version:      0.16.0
Release:      1%{?dist}
Summary:      An investigative LV2 plugin bundle
URL:          https://github.com/OpenMusicKontrollers/sherlock.lv2
Source0:      https://github.com/OpenMusicKontrollers/sherlock.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel
BuildRequires: sratom-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: cmake
BuildRequires: flex

%description
An investigative LV2 plugin bundle

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DPLUGIN_DEST:Path=%{_lib}/lv2/sherlock.lv2 .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_libdir}/lv2/*

%changelog
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.16.0
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.12.0
- Initial build
