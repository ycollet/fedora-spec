# Global variables for github repository
%global commit0 7a240470926e7929048121f0b67938851d712b6c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Pattern-controlled audio stream / sample re-sequencer LV2 plugin
Name:    lv2-BJumblr
Version: 1.2.0
Release: 2%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sjaehn/BJumblr

Source0: https://github.com/sjaehn/BJumblr/archive/%{commit0}.tar.gz#/BJumblr-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
BJumblr is a pattern-controlled audio stream / sample re-sequencer LV2 plugin

%prep
%setup -qn BJumblr-%{commit0}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install
%{__rm} -rf %{buildroot}
make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC" install

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
%{_libdir}/lv2/*

%changelog
* Sat May 16 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-2
- update to 1.2.0

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial release 
