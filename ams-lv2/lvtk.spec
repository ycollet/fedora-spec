# Global variables for github repository
%global commit0 6bfe981dfb5b27ea199dd4f6801b5305ca0355f9
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           lvtk
Version:        2.0.0.%{shortcommit0}
Release:        1%{?dist}
Summary:        LV2 Toolkit

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/lvtk/lvtk
Source0:        https://github.com/lvtk/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: python

%description
This software package contains libraries that wrap the LV2 C API and
extensions into easy to use C++ classes. The original work for this
was mostly done by Lars Luthman in lv2-c++-tools.

%prep
%setup -qn %{name}-%{commit0}

%build
./waf configure --destdir=%{buildroot} --prefix=%{_prefix} --libdir=%{_libdir}
./waf %{?_smp_mflags} -v

%install 
./waf install --destdir=%{buildroot} -v

%files
%{_libdir}/*
%{_includedir}/*

%changelog
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 2.0.0
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.2.0
- Initial build
