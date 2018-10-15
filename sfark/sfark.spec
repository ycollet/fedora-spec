# Global variables for github repository
%global commit0 cf9f324a16751812105f1f7613b799e65e43b91f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Summary: sfArk tool
Name:    sfarkxtc
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/raboof/sfarkxtc
Source0: https://github.com/raboof/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  sfark-0001-fix-install-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: sfArkLib-devel
BuildRequires: zlib-devel

%description
sfArk extractor, console version

Converts soundfonts in the legacy sfArk v2 file format to sf2

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1

%build

%{__make} DESTDIR=%{buildroot} BIN_PATH=%{_bindir} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} BIN_PATH=%{_bindir} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- update for Fedora 29
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- Initial release of spec file for 0.1
