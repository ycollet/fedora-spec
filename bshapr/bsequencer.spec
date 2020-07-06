# Global variables for github repository
%global commit0 27a8aef5002f3ec5477fba9f389121cfa89f0422
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Multi channel MIDI step sequencer LV2 plugin with a variable matrix
Name:    lv2-BSEQuencer
Version: 1.6.0
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BSEQuencer

Source0: https://github.com/sjaehn/BSEQuencer/archive/%{commit0}.tar.gz#/BSEQuencer-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Multi channel MIDI step sequencer LV2 plugin with a variable matrix

%prep
%autosetup -n BSEQuencer-%{commit0}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC" install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Jul 6 2020 Yann Collette <ycollette dot nospam at free.fr> 1.6.0-1
- update to 1.6.0-1

* Mon May 18 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.2-1
- update to 1.4.2-1

* Thu May 7 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- update to 1.4.0-1

* Sat Dec 29 2019 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- initial release 
