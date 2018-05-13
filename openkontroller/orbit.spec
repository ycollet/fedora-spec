# Global variables for github repository
%global commit0 55c1e1438222e1e56ef692576bf0a8ce3389c3a5
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:         orbit.lv2
Version:      0.1.0
Release:      2%{?dist}
Summary:      LV2 Event Looper
URL:          https://github.com/OpenMusicKontrollers/orbit.lv2
Source0:      https://github.com/OpenMusicKontrollers/orbit.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel
BuildRequires: cmake
BuildRequires: zlib-devel

%description
LV2 Event Looper

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DPLUGIN_DEST:Path=%{_lib}/lv2/orbit.lv2 .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_libdir}/lv2/*

%changelog
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial build
