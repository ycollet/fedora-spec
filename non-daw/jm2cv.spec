# Global variables for github repository
%global commit0 8bddbd13468b3d8497a9d8a19871293e3088f614
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    jm2cv
Version: 0.1
Release: 1%{?dist}
Summary: Jack Midi to Control Voltage
URL:     https://github.com/harryhaaren/jm2cv
Group:   Applications/Multimedia
License: GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

# original tarfile can be found here:
Source0: https://github.com/harryhaaren/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake

%description
This tool allows converting JACK MIDI signals into JACK audio signals.

This tool was created for use with non-mixer, to allow MIDI controller mapping to non-mixer controls. The non-mixer manual has the details, specifically the section on control voltages.

%prep
%setup -qn %{name}-%{commit0}

%build
%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/config/
%__install -m 644 example.cfg %{buildroot}%{_datadir}/%{name}/config/

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- update for Fedora 29

* Sat May 30 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial release
