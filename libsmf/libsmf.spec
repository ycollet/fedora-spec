Summary: MIDI library
Name:    libsmf
Version: 1.3
Release: 4%{?dist}
License: BSD
URL:     https://github.com/stump/libsmf

Source0: https://github.com/stump/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: glib2-devel

%description
LibSMF is a BSD-licensed C library for handling SMF ("*.mid") files.
It transparently handles conversions between time and pulses,
tempo map handling etc. The only dependencies are C compiler and glib.
Full API documentation and examples are included.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package static
Summary:  Static library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static library for %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build

autoreconf --force --install
%configure
%make_build

%install

%make_install

%files
%doc NEWS
%license COPYING
%{_bindir}/smfsh
%{_libdir}/libsmf.so.*
%{_datadir}/man/man1/smfsh.*

%files devel
%{_includedir}/*
%{_libdir}/libsmf.so
%{_libdir}/libsmf.la
%{_libdir}/pkgconfig/smf.pc

%files static
%{_libdir}/libsmf.a

%changelog
* Fri Nov 06 2020 Yann Collette <ycollette dot nospam at free.fr> 1.3-4
- fix spec file

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-3
- update for Fedora 29

* Sat Jun 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-3
- update to commit 692e728

* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-2
- update to commit fd5abd50

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.3-1
- Initial release of spec file for 1.3
