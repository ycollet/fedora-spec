# Global variables for github repository
%global commit0 fe323aab08118fa99d3f2d332337d30f00a35f5a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           lv2-screcord-plugin
Version:        0.1.%{shortcommit0}
Release:        1%{?dist}
Summary:        A simple Lv2 capture plugin

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/brummer10/screcord.lv2
Source0:        https://github.com/brummer10/screcord.lv2/archive/%{commit0}.tar.gz#/screcord.lv2-%{shortcommit0}.tar.gz

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
* Tue Nov 21 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1
- Initial build
