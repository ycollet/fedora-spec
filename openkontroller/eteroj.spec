# Global variables for github repository
%global commit0 1c9811a4986683e66805d3642de3e331d2ccc463
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:         eteroj.lv2
Version:      0.4.0
Release:      1%{?dist}
Summary:      OSC injection/ejection from/to UDP/TCP/Serial for LV2
URL:          https://github.com/OpenMusicKontrollers/eteroj.lv2
Source0:      https://github.com/OpenMusicKontrollers/eteroj.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel
BuildRequires: libuv-devel
BuildRequires: sratom-devel
BuildRequires: cmake

%description
OSC injection/ejection from/to UDP/TCP/Serial for LV2

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DPLUGIN_DEST:Path=%{_lib}/lv2/eteroj.lv2 .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_libdir}/lv2/*

%changelog
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.4.0
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.2.0
- Initial build
