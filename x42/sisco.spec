Name:    sisco.lv2
Version: 0.9.2
Release: 1%{?dist}
Summary: A LV2 oscilloscope
License: GPLv2+
URL:     https://github.com/x42/sisco.lv2

# ./sisco-source.sh <tag>
# ./sisco-source.sh v0.9.2

Source0: sisco.lv2.tar.gz
Source1: sisco-source.sh

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
%autosetup -n %{name}

%build

%set_build_flags

%make_build PREFIX=/usr LV2DIR=%{_libdir}/lv2 sisco_VERSION=%{version} STRIP=true

%install 

%make_install PREFIX=/usr LV2DIR=%{_libdir}/lv2 sisco_VERSION=%{version} STRIP=true

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Wed Apr 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- update to 0.9.2-1

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- update to 0.9.0-1 + fix debug build

* Fri May 8 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-1
- update to 0.8.6-1

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.5
- update to 0.8.5

* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.1
- update to 0.8.1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.7.3
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.7.3
- update to 0.7.3

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.6.7
- Initial build
