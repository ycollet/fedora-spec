# Global variables for github repository
%global commit0 366ad8f409b079afb714970a024bdd2c47f31c0e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: An audio stream chopping LV2 plugin
Name:    lv2-BChoppr
Version: 1.6.4
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BChoppr

Source0: https://github.com/sjaehn/BChoppr/archive/%{commit0}.tar.gz#/BChoppr-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
BChoppr cuts the audio input stream into a repeated sequence of up to 16 chops.
Each chop can be leveled up or down (gating). BChoppr is the successor of BSlizr

%prep
%autosetup -n BChoppr-%{commit0}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Jun 25 2020 Yann Collette <ycollette dot nospam at free.fr> 1.6.4-2
- updata to 1.6.4

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- initial release 
