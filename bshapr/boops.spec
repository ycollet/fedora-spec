Summary: Audio glitch effect sequencer LV2 plugin
Name:    lv2-BOops
Version: 1.2.2
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BOops

Source0: https://github.com/sjaehn/BOops/archive/%{version}.tar.gz#/BOops-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Audio glitch effect sequencer LV2 plugin

%prep
%autosetup -n BOops-%{version}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Dec 27 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-1
- update to 1.2.2-1 

* Sat Dec 5 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- update to 1.2.0-1 

* Sat Nov 07 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- initial release 
