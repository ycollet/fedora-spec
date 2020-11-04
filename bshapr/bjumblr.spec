Summary: Pattern-controlled audio stream / sample re-sequencer LV2 plugin
Name:    lv2-BJumblr
Version: 1.4.2
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BJumblr

Source0: https://github.com/sjaehn/BJumblr/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
BJumblr is a pattern-controlled audio stream / sample re-sequencer LV2 plugin

%prep
%autosetup -n BJumblr-%{version}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Wed Nov 4 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.2-2
- updata to 1.4.2-2

* Fri Jul 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- updata to 1.4.0-2

* Thu Jun 25 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-2
- updata to 1.2.2-2

* Sat May 16 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-2
- update to 1.2.0-2

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial release 
