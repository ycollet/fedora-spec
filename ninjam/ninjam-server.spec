# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:    ninjam-server
Version: 0.0.1
Release: 1%{?dist}
Summary: A realtime network sound server

Group:   Applications/Multimedia
License: GPLv2+

URL:     http://www.cockos.com/ninjam/
Source0: http://www.cockos.com/ninjam/downloads/src/ninjam_server_0.06.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel

%description
A realtime network sound client

%prep
%setup -q -c %{name}

%build

cd ninjam_server_0.06/ninjam/server
make %{?_smp_mflags}

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 ninjam_server_0.06/ninjam/server/ninjamsrv %{buildroot}%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_datadir}/ninjam/
%__install -m 644 ninjam_server_0.06/ninjam/server/cclicense.txt %{buildroot}%{_datadir}/ninjam/
%__install -m 644 ninjam_server_0.06/ninjam/server/example.cfg %{buildroot}%{_datadir}/ninjam/
%__install -m 644 ninjam_server_0.06/ninjam/server/license.txt %{buildroot}%{_datadir}/ninjam/

%files
%{_bindir}/*
%{_datadir}/ninjam/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1
- Initial build
