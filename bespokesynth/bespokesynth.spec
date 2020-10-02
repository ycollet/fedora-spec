# Global variables for github repository
%global commit0 ecb84aaf0016bfd2f2c1b7b3934fda857141cf95
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%define _lto_cflags %{nil}

Name:    BespokeSynth
Version: 0.0.1
Release: 5%{?dist}
Summary: A software modular synth
License: GPLv2+
URL:     https://github.com/awwbees/BespokeSynth

Source0: https://github.com/awwbees/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: vst.tar.bz2
# Replace python-config by python2-config
Source2: Makefile.bespokesynth
Source3: Bespoke-GLSLfix.sh

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: JUCE
BuildRequires: python2-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libglvnd-devel
BuildRequires: libusbx-devel
BuildRequires: libpng-devel

%description
A software modular synth

%prep
%autosetup -n %{name}-%{commit0}

tar xvfj %{SOURCE1}
cp %{SOURCE2} Builds/LinuxMakefile/Makefile

sed -i -e "s/\.\.\/\.\.\/MacOSX\/build\/Release\/data/\/usr\/share\/BespokeSynth\/data/g" Source/OpenFrameworksPort.cpp

%build

export CURRENTDIR=`pwd`
cd Builds/LinuxMakefile
%{make_build} V=1 DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_libdir} CONFIG=Release CPPFLAGS="%{build_cxxflags}" CXXFLAGS="-I$CURRENTDIR/vst/vstsdk2.4/ -I/usr/include/freetype2" %{?_smp_mflags}

%install 

cd Builds/LinuxMakefile
%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 build/BespokeSynth %{buildroot}/%{_bindir}/
%__install -m 755 %{SOURCE3} %{buildroot}/%{_bindir}/Bespoke-GLSLfix
chmod a+x %{buildroot}/%{_bindir}/Bespoke-GLSLfix

cd ../..
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/data
cp -r Builds/MacOSX/build/Release/data/* %{buildroot}/%{_datadir}/%{name}/data

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update for fedora 33

* Wed Sep 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to v0.0005-pre

* Wed Aug 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to v0.0004-pre - dc51a8783f71fc5a8f019beb0783d35d9ec5474c

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- Fix install

* Tue May 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
