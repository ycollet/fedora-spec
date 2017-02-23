# Global variables for github repository
%global commit0 810b427069441ee365c819220d1515b2d68d941b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           swh-lv2
Version:        0.9.%{shortcommit0}
Release:        1%{?dist}
Summary:        SWH LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/swh-lv2
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: libxslt

%description
SWH LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
#make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}
make %{?_smp_mflags} real-clean
make %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install-system

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
