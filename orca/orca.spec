%global commitid 3a92c8e3b3b75598ed762aee4aa34e689f1471a5
%global commitidshort 3a92c8e3

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:    orca
Version: 0.1.0.%{commitidshort}
Release: 1%{?dist}
Summary: An esoteric programming language

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://git.sr.ht/~rabbits/orca
Source0: orca.tar.gz
# From https://github.com/hundredrabbits/Orca
Source1: Orca-doc.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: portmidi-devel

%description
Orca is an esoteric programming language, designed to create procedural sequencers in which each letter of the alphabet is an operation,
where lowercase letters operate on bang, uppercase letters operate each frame.
The application is not a synthesiser, but a flexible livecoding environment capable of sending MIDI,
OSC & UDP to your audio interface, like Ableton, Renoise, VCV Rack or SuperCollider. 

%prep
%setup -qn %{name}

tar xvfz %{SOURCE1}

%build

make %{?_smp_mflags}

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 build/orca %{buildroot}%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -r examples  %{buildroot}/%{_datadir}/%{name}/examples
cp -r Orca-doc/resources %{buildroot}/%{_datadir}/%{name}/documentation

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/%{name}/*

%changelog
* Sat May 9 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.3a92c8e3-1
- Initial spec file
