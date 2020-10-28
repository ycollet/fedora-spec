Name:    minicomputer
Summary: Minicomputer is a standalone Linux software synthesizer
Version: 1.4
Release: 1%{?dist}
License: GPL
URL:     http://minicomputer.sourceforge.net/

Source0: https://sourceforge.net/projects/minicomputer/files/minicomputer/version%20%{version}/MinicomputerV%{version}.tar.gz
Source1: minicomputer-SConstruct

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: fltk-devel
BuildRequires: scons

%description
Minicomputer is a standalone Linux softwaresynthesizer for creating experimental electronic sounds as its often
used in but not limited to Industrial music, IDM, EBM, Glitch, sound design and minimal electronic.
It is monophonic but can produce up to 8 different sounds at the same time.
It uses Jack as realtime audio infrastructure and can be controlled via Midi.

%prep
%autosetup -cn %{name}-%{version}

cp %{SOURCE1} SConstruct
sed -i -e "/unistd/a#include<unistd.h>" editor/Memory.h

%build

%set_build_flags
scons DESTDIR="%{buildroot}" Prefix=/usr

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/

cp minicomputerManual.pdf %{buildroot}/%{_datadir}/%{name}/doc/
cp minicomputer.xpm       %{buildroot}/%{_datadir}/pixmaps/
cp minicomputer           %{buildroot}/%{_bindir}/
cp minicomputerCPU        %{buildroot}/%{_bindir}/
cp -r factoryPresets/*    %{buildroot}/%{_datadir}/%{name}/presets/

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*

%changelog
* Wed Oct 28 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4-1
- initial release
