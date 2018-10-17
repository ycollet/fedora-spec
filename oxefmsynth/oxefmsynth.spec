# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 fe078ea036991081c3a28bb388a3fecd0e8e3a5d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    oxefmsynth
Version: 1.3.5.%{shortcommit0}
Release: 1%{?dist}
Summary: A FM synthetized

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/oxesoft/oxefmsynth
Source0: https://github.com/oxesoft/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: wget
BuildRequires: unzip

%description
A FM synthetizer

%prep
%setup -qn %{name}-%{commit0}

%build

tar xvfj %{SOURCE1}
export VSTSDK_PATH=vst/vstsdk2.4/

make 

%install 

%__install -m 755 -d %{buildroot}%{_libdir}/vst/
%__install -m 644 *.so %{buildroot}/%{_libdir}/vst/

%__install -m 755 -d %{buildroot}%{_libdir}/vst/skins/default/
%__install -m 755 -d %{buildroot}%{_libdir}/vst/skins/dx7/
%__install -m 755 -d %{buildroot}%{_libdir}/vst/skins/lcd/
%__install -m 755 -d %{buildroot}%{_libdir}/vst/skins/snow/
%__install -m 755 -d %{buildroot}%{_libdir}/vst/skins/totolitoto/
%__install -m 755 -d %{buildroot}%{_libdir}/vst/skins/tx802/

%__install -m 644 skins/default/*    %{buildroot}/%{_libdir}/vst/skins/default/
%__install -m 644 skins/dx7/*        %{buildroot}/%{_libdir}/vst/skins/dx7/
%__install -m 644 skins/lcd/*        %{buildroot}/%{_libdir}/vst/skins/lcd/
%__install -m 644 skins/snow/*       %{buildroot}/%{_libdir}/vst/skins/snow/
%__install -m 644 skins/totolitoto/* %{buildroot}/%{_libdir}/vst/skins/totolitoto/
%__install -m 644 skins/tx802/*      %{buildroot}/%{_libdir}/vst/skins/tx802/

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc/
%__install -m 644 README.md %{buildroot}/%{_datadir}/%{name}/doc/
%__install -m 644 LICENSE   %{buildroot}/%{_datadir}/%{name}/doc/

%files
%{_libdir}/*
%{_datadir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.3.5
- update for Fedora 29
- update to fe078ea036991081c3a28bb388a3fecd0e8e3a5d

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 1.3.5

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.3.4
- Initial build
