%define _lto_cflags %{nil}

Summary: Beat / envelope shaper LV2 plugin
Name:    lv2-BShapr
Version: 0.12
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BShapr

Source0: https://github.com/sjaehn/BShapr/archive/v%{version}.tar.gz#/BShapr-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Beat / envelope shaper LV2 plugin

%prep
%autosetup -n BShapr-%{version}

%build

%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Wed Mar 17 2021 Yann Collette <ycollette dot nospam at free.fr> 0.12.0-1
- update to 0.12.0-1

* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 0.11.0-1
- update to 0.11.0-1

* Sun Feb 7 2021 Yann Collette <ycollette dot nospam at free.fr> 0.10.0-1
- update to 0.10.0-1

* Mon May 25 2020 Yann Collette <ycollette dot nospam at free.fr> 0.9.0-1
- update to 0.9.0-1

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.8.0-1
- update to 0.8.0-1

* Thu Jan 16 2020 Yann Collette <ycollette dot nospam at free.fr> 0.7.0-1
- update to 0.7.0-1

* Sat Nov 30 2019 Yann Collette <ycollette dot nospam at free.fr> 0.6.0-1
- update to 0.6.0-1

* Sun Oct 13 2019 Yann Collette <ycollette dot nospam at free.fr> 0.4.0-1
- update to 0.4.0-1

* Sat Aug 24 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.2-1
- initial release 
