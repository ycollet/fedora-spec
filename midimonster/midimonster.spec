# Global variables for github repository
%global commit0 5f4b349aff49be0a5f6895631a93c47fcafcff93
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    midimonster
Version: 0.4.0
Release: 1%{?dist}
Summary: Multi-protocol translation software (ArtNet, MIDI, OSC, JACK MIDI/CV ...)

Group:   Applications/Multimedia
License: BSD
URL:     https://github.com/cbdevnet/midimonster

Source0: https://github.com/cbdevnet/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
%setup -qn %{name}-%{commit0}

sed -i -e "s/lua53/lua/g" backends/Makefile

%build
make clean
make DESTDIR=%{buildroot} PREFIX=/usr PLUGINS=%{_libdir}/midimonster

%install

make DESTDIR=%{buildroot} PREFIX=/usr PLUGINS=%{_libdir}/midimonster install

%files
%{_bindir}/*
%{_libdir}/%{name}/*
%{_datadir}/%{name}/*

%changelog
* Thu Mar 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- initial spec file -  version 0.4.0-1
