# Global variables for github repository
%global commit0 cab6e0dfb2ce20e4ad34b067d1281ec0b193598a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           tap-lv2
Version:        0.9.%{shortcommit0}
Release:        2%{?dist}
Summary:        TAP LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/tap-lv2
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel

%description
TAP LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial build
