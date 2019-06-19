# Global variables for github repository
%global commit0 38df4d733fff1a9438a89ec8797bc6b6810adfa7
%global gittag0 v0.8.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    sisco.lv2
Version: 0.8.1
Release: 1%{?dist}
Summary: A LV2 oscilloscope

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/x42/sisco.lv2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A LV2 oscilloscope

%prep

[ ! -d build-sisco.lv2 ] && git clone https://github.com/x42/sisco.lv2.git build-sisco.lv2

%build
cd build-sisco.lv2
git checkout %{gittag0}
make submodules
make DESTDIR=%{buildroot} PREFIX=/usr LV2DIR=%{_libdir}/lv2 sisco_VERSION=%{version} LDFLAGS=-lpthread %{?_smp_mflags}

%install 
cd build-sisco.lv2
make DESTDIR=%{buildroot} PREFIX=/usr LV2DIR=%{_libdir}/lv2 sisco_VERSION=%{version} LDFLAGS=-lpthread %{?_smp_mflags} install

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.1
- update to 0.8.1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.7.3
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.7.3
- update to 0.7.3

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.6.7
- Initial build
