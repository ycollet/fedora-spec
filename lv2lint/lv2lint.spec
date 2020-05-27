Name:    lv2lint
Version: 0.2.0
Release: 4%{?dist}
Summary: Check whether a given LV2 plugin is up to the specification

License: Artistic License 2.0
URL:     https://gitlab.com/drobilla/lv2lint

Source0: https://gitlab.com/drobilla/lv2lint/-/archive/%{version}/lv2lint-%{version}.tar.gz
Patch0:  lv2lint-0001-fix-multiple-symbol.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: libcurl-devel
BuildRequires: elfutils-libelf-devel

%description
An LV2 lint-like tool that checks whether a given plugin and its UI(s) match up
with the provided metadata and adhere to well-known best practices.
Run it as part of your continuous integration pipeline together with
lv2/sord_validate to reduce the likelihood of shipping plugins with major flaws
in order to prevent unsatisfied users.

%prep
%autosetup

%build

%set_build_flags

mkdir build
VERBOSE=1 meson --buildtype release --prefix=/usr build

cd build
VERBOSE=1 %ninja_build 

%install 

cd build
VERBOSE=1 %ninja_install

%files
%doc README.md ChangeLog VERSION
%license COPYING
%{_bindir}/*
%{_mandir}/*

%changelog
* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-4
- fix spec file

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-3
- update for Fedora 32

* Sat Dec 28 2019 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial build
