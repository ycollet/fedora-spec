%global debug_package %{nil}

# Global variables for github repository
%global commit0 f1c3f4b94ea04a991c201bbe6a19336471b5f37e
%global gittag0 v0.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lv2-GxMatchEQ
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Matching Equalizer to apply EQ curve from on source to a other source

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/brummer10/GxMatchEQ.lv2
Source0: https://github.com/brummer10/GxMatchEQ.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
Matching Equalizer to apply EQ curve from on source to a other source.

%prep
%setup -qn GxMatchEQ.lv2-%{commit0}

%build

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 install

%files
%{_libdir}/lv2/gx_matcheq.lv2/*

%changelog
* Fri May 22 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
