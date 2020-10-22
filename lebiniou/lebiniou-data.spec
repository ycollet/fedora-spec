Name:    lebiniou-data
Version: 3.42
Release: 3%{?dist}
Summary: Lebiniou is an audio spectrum visualizer - data package
URL:     https://biniou.net/
License: GPLv2+

# original tarfile can be found here:
Source0: https://gitlab.com/lebiniou/lebiniou-data/-/archive/version-%{version}/lebiniou-data-version-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: jansson-devel
BuildRequires: autoconf automake libtool

%description

This package contains data files for use with lebiniou - https://gitlab.com/lebiniou/lebiniou

%prep
%autosetup -n %{name}-version-%{version}

%build

%set_build_flags

autoreconf --install

LDFLAGS="${LDFLAGS:-%{build_ldflags}} -z muldefs" ; export LDFLAGS
%configure --prefix=%{_prefix} --libdir=%{_libdir}

%make_build

%install

%make_install

%files
%doc README.md AUTHORS ChangeLog THANKS
%license COPYING
%{_datadir}/lebiniou/*
%{_datadir}/doc/lebiniou-data/examples/sequences.tar.gz

%changelog
* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 3.42-4
- fix debug build

* Sun May 10 2020 Yann Collette <ycollette.nospam@free.fr> - 3.42-3
- update to 3.42

* Thu Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 3.40-3
- fix for Fedora 32

* Mon Feb 17 2020 Yann Collette <ycollette.nospam@free.fr> - 3.40-1
- update to 3.40

* Fri May 17 2019 Yann Collette <ycollette.nospam@free.fr> - 3.28-1
- initial spec file
