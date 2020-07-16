%global debug_package %{nil}

Name:    receivemidi
Version: 1.0.6
Release: 1%{?dist}
Summary: A command line tool to receive MIDI event
License: GPLv3

URL:     https://github.com/gbevin/ReceiveMIDI
Source0: https://github.com/gbevin/ReceiveMIDI/archive/%{version}.tar.gz#/ReceiveMIDI-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel

%description
ReceiveMIDI is a multi-platform command-line tool makes it very easy to quickly
receive and monitor MIDI messages from MIDI devices on your computer.

%prep
%autosetup -n ReceiveMIDI-%{version}

%build

%set_build_flags

cd Builds/LinuxMakefile

%make_build STRIP=true

%install 

cd Builds/LinuxMakefile

%__install -m 755 -d %{buildroot}%{_bindir}/
%__install -m 644 -p build/receivemidi %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%changelog
* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-1
- Initial spec file
