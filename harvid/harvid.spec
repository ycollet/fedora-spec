# Global variables for github repository
%global commit0 d71921ba52efd1362973df850213eebe97a7ecc6
%global gittag0 0.8.3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    harvid
Version: 0.8.3.%{shortcommit0}
Release: 1%{?dist}
Summary: harvid -- HTTP Ardour Video Daemon
URL:     https://github.com/x42/harvid.git
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://github.com/x42/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: libXrender-devel
BuildRequires: libX11-devel
BuildRequires: ffmpeg-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: vim-common
BuildRequires: libpng-devel

%description
Harvid decodes still images from movie files and serves them via HTTP.
Its intended use-case is to efficiently provide frame-accurate data and
act as second level cache for rendering the video-timeline in Ardour - http://ardour.org.

%prep
%setup -qn %{name}-%{commit0}

%build

make CFLAGS="%{build_cxxflags}" DESTDIR=%{buildroot} PREFIX=/usr

%install

make CFLAGS="%{build_cxxflags}" DESTDIR=%{buildroot} PREFIX=/usr install

%files
%doc README.md COPYING ChangeLog

%{_bindir}/*
%{_mandir}/*
%{_datadir}/*

%changelog
* Sun Dec 2 2018 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-1
- initial spec file
