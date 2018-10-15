%global debug_package %{nil}

# Global variables for github repository
%global commit0 e558feb824132d71004af82cc3a235566b89bec8
%global gittag0 2.24
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: sfArk library
Name:    sfArkLib
Version: 2.24.%{shortcommit0}
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/raboof/sfArkLib
Source0: https://github.com/raboof/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  libsfark-0001-fix-install-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: zlib-devel

%description
Library for decompressing sfArk soundfonts.

A simple command-line tool to convert sfArk files to sf2
based on this library can be found at https://github.com/raboof/sfArkXTm

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1

%build

%{__make} DESTDIR=%{buildroot} LIB_PATH=%{_libdir} INC_PATH=%{_includedir} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} LIB_PATH=%{_libdir} INC_PATH=%{_includedir} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 2.24-1
- update for Fedora 29

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 2.24-1
- Initial release of spec file for 2.24
