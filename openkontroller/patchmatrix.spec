# Global variables for github repository
%global commit0 f379aad8146a2a6e45db7966b0657beb61bc1ac2
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         patchmatrix
Version:      0.12.0
Release:      1%{?dist}
Summary:      A JACK patchbay in flow matrix style
URL:          https://github.com/OpenMusicKontrollers/patchmatrix
Source0:      https://github.com/OpenMusicKontrollers/patchmatrix/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: cmake

%description
A JACK patchbay in flow matrix style

%prep
%setup -qn %{name}-%{commit0}

%build

mkdir build
cd build
%cmake ..

make VERBOSE=1 %{?_smp_mflags}

%install

cd build
make DESTDIR=%{buildroot} install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.20.0
- inital release
