# Global variables for github repository
%global commit0 792d453da0f3a599408008f0f1107823939d730d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           gxtuner
Version:        3.0.%{shortcommit0}
Release:        2%{?dist}
Summary:        A tuner for jack, with full jack session managment support

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/brummer10/gxtuner
Source0:        https://github.com/brummer10/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gtk3-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: fftw-devel
BuildRequires: zita-resampler-devel

%description
A tuner for jack, with full jack session managment support

%prep
%setup -qn %{name}-%{commit0}

%build

%make_build 

%install 

%make_install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 3.0-2
- update to latest master
* Mon Dec 25 2017 Yann Collette <ycollette.nospam@free.fr> - 3.0-1
- Initial build
