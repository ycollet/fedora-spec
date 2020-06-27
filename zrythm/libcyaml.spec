%global commit0 47075327890518596e5a6fe1bd8a759ac8dc8669
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:     libcyaml
Version:  1.1.0
Release:  1%{?dist}
Summary:  C library for reading and writing YAML

License:  ISC
Packager: Alexandros Theodotou

URL:     https://git.zrythm.org/cgit/zrythm-cyaml/
Source0: https://git.zrythm.org/cgit/zrythm-cyaml/snapshot/zrythm-cyaml-%{commit0}.tar.bz2

BuildRequires: libyaml-devel
BuildRequires: gcc
BuildRequires: pkgconfig

%description
LibCYAML is a C library for reading and writing structured YAML documents.
It is written in ISO C11 and licensed under the ISC licence.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n zrythm-cyaml-%{commit0}

%build

%make_build PREFIX=/usr LIBDIR=%{_lib}

%install

mkdir -p %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_includedir}
%make_install PREFIX=/usr LIBDIR=%{_lib}

%files
%defattr(-,root,root,-)
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Sat Jun 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Adjustment for Fedora

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Adjustment for Fedora

* Mon Feb 4 2019 Alexandros Theodotou <alex at zrythm dot org> 0.1.0-1
- Bump to official v0.1.0 release

* Tue Jan 22 2019 Alexandros Theodotou <alex at zrythm dot org> 0.1.0-1
- RPM release
