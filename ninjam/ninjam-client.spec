# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:    ninjam-client
Version: 0.0.1
Release: 1%{?dist}
Summary: A realtime network sound client

Group:   Applications/Multimedia
License: GPLv2+

URL:     http://www.cockos.com/ninjam/
Source0: http://www.cockos.com/ninjam/downloads/src/cclient_src_v0.01a.tar.gz

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

cd ninjam/cursesclient
make OPTFLAGS=-fpermissive %{?_smp_mflags}

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 ninjam/cursesclient/cninjam %{buildroot}%{_bindir}/

%files
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1
- Initial build
