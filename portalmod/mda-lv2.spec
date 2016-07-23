# Global variables for github repository
%global commit0 3d6dd099146b72c1fe88e06679034715fb999a5b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           mda-lv2
Version:        0.9.%{shortcommit0}
Release:        1%{?dist}
Summary:        MDA LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/mda-lv2
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: python

%description
MDA LV2 set of plugins synth from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
./waf configure --libdir=%{buildroot}%{_libdir}
./waf

%install 
./waf -j1 install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
