# Global variables for github repository
%global commit0 e079b03bbc0cadb30e3aeae05e1cff916a13c90c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:         orbit.lv2
Version:      0.1.0
Release:      1%{?dist}
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
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0
- Initial build
