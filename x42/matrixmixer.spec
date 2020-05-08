# Global variables for github repository
%global commit0 dd4617a05ea14294abf4ac753c5c0e52f1003b92
%global gittag0 v0.3.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    matrixmixer.lv2
Version: 0.3.0
Release: 1%{?dist}
Summary: A LV2 matrix mixer

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/x42/matrixmixer.lv2
Source0: matrixmixer.lv2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A LV2 matrix mixer

%prep
%setup -qn %{name}

%build

make DESTDIR=%{buildroot} PREFIX=/usr LV2DIR=%{_libdir}/lv2 matrixmixer_VERSION=%{version} LDFLAGS=-lpthread %{?_smp_mflags}

%install 

make DESTDIR=%{buildroot} PREFIX=/usr LV2DIR=%{_libdir}/lv2 matrixmixer_VERSION=%{version} LDFLAGS=-lpthread %{?_smp_mflags} install

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Fri May 8 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
