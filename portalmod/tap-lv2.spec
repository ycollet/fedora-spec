# Global variables for github repository
%global commit0 de26a3c8c8c2227e6d7fba3dcb54ec5fe2def258
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           tap-lv2
Version:        0.9.%{shortcommit0}
Release:        1%{?dist}
Summary:        TAP LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/tap-lv2
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         tap-0001-fix-misleading-indent.patch

BuildRequires: lv2-devel

%description
TAP LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}
%patch0 -p1

%build
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
