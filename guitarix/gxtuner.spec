# Global variables for github repository
%global commit0 281b21af1e9003c1780eacd58cdeba0f5dc59577
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           gxtuner
Version:        3.0.%{shortcommit0}
Release:        1%{?dist}
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
* Tue Dec 25 2017 Yann Collette <ycollette.nospam@free.fr> - 3.0
- Initial build
