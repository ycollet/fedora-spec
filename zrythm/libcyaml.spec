Name: libcyaml
Version: 0.1.0
Release: 1%{?dist}
Summary: C library for reading and writing YAML

Group: Applications/Multimedia
License: ISC
Packager: Alexandros Theodotou

URL:     https://git.zrythm.org/git/libcyaml
Source0: https://git.zrythm.org/cgit/libcyaml/snapshot/libcyaml-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libyaml-devel
BuildRequires: gcc
BuildRequires: pkgconfig

%description
LibCYAML is a C library for reading and writing structured YAML documents.
It is written in ISO C11 and licensed under the ISC licence.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -q

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_includedir}
%{__make} install DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=lib64

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Adjustment for Fedora

* Mon Feb 4 2019 Alexandros Theodotou <alex at zrythm dot org> 0.1.0-1
- Bump to official v0.1.0 release

* Tue Jan 22 2019 Alexandros Theodotou <alex at zrythm dot org> 0.1.0-1
- RPM release
