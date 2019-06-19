# Global variables for github repository
%global commit0 b23201bb1a566d7e4ea84b76b3dcf2efcc025dac
%global gittag0 v2.10
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: JSON library
Name:    jansson
Version: 2.10.%{shortcommit0}
Release: 1%{?dist}
License: GPL
Group:   Development/Libraries

URL:     https://github.com/akheron/jansson
Source0: https://github.com/akheron/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
Jansson_ is a C library for encoding, decoding and manipulating JSON data.
Its main features and design principles are:

- Simple and intuitive API and data model
- Comprehensive documentation
- No dependencies on other libraries
- Full Unicode support (UTF-8)
- Extensive test suite

Jansson is licensed under the MIT license; see LICENSE in the source distribution for details.

%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}

%build

%ifarch x86_64 amd64 ia32e
%cmake -DJANSSON_INSTALL_LIB_DIR=/usr/lib64 -DJANSSON_INSTALL_CMAKE_DIR=/usr/lib64/cmake .
%else
%cmake .
%endif

%{__make} VERBOSE=1 %{?_smp_mflags}

%install

%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.rst
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 2.10-1
- update for Fedora 29

* Mon Sep 18 2017 Yann Collette <ycollette dot nospam at free.fr> 2.10-1
- Initial release of spec file for 2.10-1
