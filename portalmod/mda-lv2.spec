# Global variables for github repository
%global commit0 3d6dd099146b72c1fe88e06679034715fb999a5b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:    mda-lv2
Version: 0.9.%{shortcommit0}
Release: 2%{?dist}
Summary: MDA LV2 set of plugins from portalmod

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/portalmod/mda-lv2
Source0: https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python2

%description
MDA LV2 set of plugins synth from portalmod

%prep
%setup -qn %{name}-%{commit0}

# For Fedora 29
%if 0%{?fedora} >= 29
  find . -type f -exec sed -i -e "s/env python/env python2/g" {} \;
%endif

%build
./waf configure --libdir=%{buildroot}%{_libdir}
./waf

%install 
./waf -j1 install

%files
%{_libdir}/lv2/*

%changelog
* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.2
- fix for Fedora 31

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- update for Fedora 29

* Sat May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- fix f27 / f28 build

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial build
