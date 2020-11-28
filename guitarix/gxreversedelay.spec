# Global variables for github repository
%global commit0 c45294df6b45016f6c2ec2e44840af9a948f06db
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lv2-GxReverseDelay
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Digital reverse delay LV2 plugin
License: GPLv2+
URL:     https://github.com/brummer10/GxReverseDelay.lv2

Source0: https://github.com/brummer10/GxReverseDelay.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  gxreversedelay-0001-cleanup-flags.patch
%if 0%{?fedora} <= 32
Patch1:  gxreversedelay-0002-Revert-allow-building-against-latest-LV2.patch
%endif

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
Digital reverse delay LV2 plugin.

%prep
%autosetup -p1 -n GxReverseDelay.lv2-%{commit0}

%build

%set_build_flags

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/gx_reversedelay.lv2/*

%changelog
* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
