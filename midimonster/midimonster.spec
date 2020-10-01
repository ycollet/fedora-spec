# Global variables for github repository
%global commit0 c0bb55ff08faf2f89af947090d1c9bc412927d9f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    midimonster
Version: 0.5
Release: 2%{?dist}
Summary: Multi-protocol translation software (ArtNet, MIDI, OSC, JACK MIDI/CV ...)
License: BSD
URL:     https://github.com/cbdevnet/midimonster

Source0: https://github.com/cbdevnet/midimonster/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: lua-devel
BuildRequires: libevdev-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: openssl-devel
BuildRequires: python3-devel

%description
Named for its scary math, the MIDIMonster is a universal control and translation
tool for multi-channel absolute-value-based control and/or bus protocols.

%prep
%setup -qn %{name}-%{version}

sed -i -e "s/lua53/lua/g" backends/Makefile

%build

%make_build PREFIX=/usr PLUGINS=%{_libdir}/midimonster

%install

%make_install PREFIX=/usr PLUGINS=%{_libdir}/midimonster

%files
%{_bindir}/*
%{_libdir}/%{name}/*
%{_datadir}/%{name}/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to version 0.5.0-2 - fix for fedora 33

* Mon May 4 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to version 0.5.0-1

* Thu Mar 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- initial spec file -  version 0.4.0-1
