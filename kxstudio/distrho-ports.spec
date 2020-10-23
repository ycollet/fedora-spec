# Global variables for github repository
%global commit0 a953bed05844d4a0ba349f75c75b56a430c8b11a
%global gittag0 2020-07-14
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    DISTRHO-Ports
Version: 1.0.1.%{shortcommit0}
Release: 4%{?dist}
Summary: A set of LV2 plugins
License: GPLv2+
URL:     https://github.com/DISTRHO/DISTRHO-Ports

Source0: https://github.com/DISTRHO/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: meson

%description
A set of LV2 plugins

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "/-Wl,--strip-all/d" meson.build

%build

%set_build_flags

%meson -Dbuild-lv2=true -Dbuild-vst3=true
%meson_build 

%install 

%meson_install

%files
%doc README.md
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-5
- fix debug build

* Tue Jul 14 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-4
- update to 2020-07-14 (1.0.1)

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-4
- update to 7e62235e809e59770d0d91d2c48c3f50ce7c027a

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update to a82fff059baafc03f7c0e8b9a99f383af7bfbd79

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-2
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
