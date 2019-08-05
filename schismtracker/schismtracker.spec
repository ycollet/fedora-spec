# Global variables for github repository
%global commit0 10bd1b80cd556237ebc2a7bd8890b72523849c46
%global gittag0 20190722
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    schismtracker
Version: 20190722
Release: 1%{?dist}
Summary: Module tracker software for creating music

Group:   Applications/Multimedia
License: GPLv3+

URL:     https://github.com/schismtracker/schismtracker
Source0: https://github.com/schismtracker/schismtracker/archive/%{commit0}.tar.gz#/schismtracker-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: SDL-devel
BuildRequires: python

%description
Schism Tracker is a free and open-source reimplementation of [Impulse
Tracker](https://github.com/schismtracker/schismtracker/wiki/Impulse-Tracker),
a program used to create high quality music without the requirements of
specialized, expensive equipment, and with a unique "finger feel" that is
difficult to replicate in part. The player is based on a highly modified
version of the [Modplug](https://openmpt.org/legacy_software) engine, with a
number of bugfixes and changes to [improve IT].

%prep
%setup -qn %{name}-%{commit0}

%build

autoreconf --force --install
mkdir auto
%configure
make DESTDIR=%{buildroot} %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS INSTALL README.md
%license COPYING
%{_bindir}/schismtracker
%{_datadir}/pixmaps/*
%{_datadir}/man/*
%{_datadir}/applications/*


%changelog
* Mon Aug 5 2019 Yann Collette <ycollette dot nospam at free dot fr> - 20190722-1
- update to 20190722

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20181223-1
- update to 20181223

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180810-1
- update to Fedora 29

* Sat Aug 11 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180810-1
- update to latest version

* Mon May 14 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180513-1
- update to latest version

* Sat Apr 14 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180209-1
- Initial version of the package

