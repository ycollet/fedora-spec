# Global variables for github repository
%global commit0 b50179f06ae6c353275b48a6fd298fa73ca22a14
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           mod-distortion
Version:        0.9.%{shortcommit0}
Release:        1%{?dist}
Summary:        mod-distortion LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/mod-distortion
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel

%description
mod-distortion LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
