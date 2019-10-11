# Global variables for github repository
%global commit0 b400a228ace1463e78aaac56228c69cc53f43ef8
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: LV2 audio effect plugin for sequenced slicing of stereo audio input signals. Each slice can be levelled up or down to get a step sequencer-like effect.
Name:    lv2-BSlizr
Version: 1.2.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sjaehn/BSlizr

Source0: https://github.com/sjaehn/BSlizr/archive/%{commit0}.tar.gz#/BSlizr-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
LV2 audio effect plugin for sequenced slicing of stereo audio input signals. Each slice can be levelled up or down to get a step sequencer-like effect.

%prep
%setup -qn BSlizr-%{commit0}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install
%{__rm} -rf %{buildroot}
make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC" install

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
%{_libdir}/lv2/*

%changelog
* Fri Oct 11 2019 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- initial release 
