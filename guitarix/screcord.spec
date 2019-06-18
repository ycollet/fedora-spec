# Global variables for github repository
%global commit0 36fbff9a02cb7c6e9296da00ac0fdd18fdda08c4
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    lv2-screcord-plugin
Version: 0.1.%{shortcommit0}
Release: 2%{?dist}
Summary: A simple Lv2 capture plugin

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/brummer10/screcord.lv2
Source0: https://github.com/brummer10/screcord.lv2/archive/%{commit0}.tar.gz#/screcord.lv2-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel

%description
A simple Lv2 capture plugin

%prep
%setup -qn screcord.lv2-%{commit0}

%build

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 install

%files
%{_libdir}/lv2/sc_record.lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to latest master

* Tue Nov 21 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
