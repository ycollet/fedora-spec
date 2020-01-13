# Global variables for github repository
%global commit0 ae4ed89f3adb54b0b665e2778c81c73ee03827c1
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    kpp
Version: 1.1.0
Release: 1%{?dist}
Summary: A set of plugins for guitar sound processing
URL:     https://github.com/olegkapitonov/Kapitonov-Plugins-Pack
Group:   Applications/Multimedia
License: GPLv2+

Source0: https://github.com/olegkapitonov/Kapitonov-Plugins-Pack/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ sed
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: ladspa-devel
BuildRequires: libxcb-devel
BuildRequires: cairo-devel
BuildRequires: zita-resampler-devel
BuildRequires: zita-convolver-devel
BuildRequires: faust
BuildRequires: meson

%description
A set of plugins for guitar sound processing

%prep
%setup -qn Kapitonov-Plugins-Pack-%{commit0}

sed -i -e "s/-archdir//g" meson.build

%build

VERBOSE=1 meson --prefix=/usr build
cd build

DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Jan 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- inital release
