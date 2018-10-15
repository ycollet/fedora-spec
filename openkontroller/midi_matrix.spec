# Global variables for github repository
%global commit0 7f8496d967acb8e2eb64c6cbb0853cd2c8d7844d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         midi_matrix.lv2
Version:      0.20.0
Release:      2%{?dist}
Summary:      A LV2 Plugin Bundle
URL:          https://github.com/OpenMusicKontrollers/midi_matrix.lv2
Source0:      https://github.com/OpenMusicKontrollers/midi_matrix.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: cmake

%description
A LV2 Plugin Bundle

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DPLUGIN_DEST:Path=%{_lib}/lv2/midi_matrix.lv2 .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update for Fedora 29
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to latest master
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-1
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.18.0
- Initial build
