# Global variables for github repository
%global commit0 03cee1d80bf4022d4df65a9cfcb54fdb01d5025b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Multi channel MIDI step sequencer LV2 plugin with a variable matrix
Name:    lv2-BSEQuencer
Version: 1.4.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sjaehn/BSEQuencer

Source0: https://github.com/sjaehn/BSEQuencer/archive/%{commit0}.tar.gz#/BSEQuencer-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Multi channel MIDI step sequencer LV2 plugin with a variable matrix

%prep
%setup -qn BSEQuencer-%{commit0}

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
* Thu May 7 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- update to 1.4.0-1

* Sat Dec 29 2019 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- initial release 
