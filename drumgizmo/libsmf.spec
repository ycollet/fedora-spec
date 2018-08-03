# Global variables for github repository
%global commit0 692e728d2c13caa3896880216f19f5565ea03886
%global gittag0 libsmf-1.3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: MIDI library
Name: libsmf
Version: 1.3.%{shortcommit0}
Release: 3%{?dist}
License: BSD
Group: Applications/Multimedia
URL:            https://github.com/stump/libsmf
Source0:        https://github.com/stump/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: glib2-devel

%description
LibSMF is a BSD-licensed C library for handling SMF ("*.mid") files. It transparently handles conversions between time and pulses, tempo map handling etc. The only dependencies are C compiler and glib. Full API documentation and examples are included.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}

%build

autoreconf --force --install
%configure
%{__make} %{_smp_mflags}
%{__make} DESTDIR=%{buildroot} install

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/*
%{_libdir}/*
%{_datadir}/man/*

%files devel
%{_includedir}/*

%changelog
* Sat Jun 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-3
- update to commit 692e728
* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-2
- update to commit fd5abd50
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.3-1
- Initial release of spec file for 1.3
