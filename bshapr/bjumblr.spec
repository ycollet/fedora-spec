# Global variables for github repository
%global commit0 af32cc761feb79d929d006306ded975a01e4f4ac
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Pattern-controlled audio stream / sample re-sequencer LV2 plugin
Name:    lv2-BJumblr
Version: 1.4.0
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BJumblr

Source0: https://github.com/sjaehn/BJumblr/archive/%{commit0}.tar.gz#/BJumblr-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
BJumblr is a pattern-controlled audio stream / sample re-sequencer LV2 plugin

%prep
%autosetup -n BJumblr-%{commit0}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Jul 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- updata to 1.4.0-2

* Fri Jun 25 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-2
- updata to 1.2.2-2

* Sat May 16 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-2
- update to 1.2.0-2

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial release 
