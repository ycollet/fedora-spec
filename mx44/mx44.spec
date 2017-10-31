%global debug_package %{nil}

Name:         mx44
Version:      0.44.2
Release:      1%{?dist}
Summary:      A JACK patchbay in flow matrix style
URL:          http://web.comhem.se/luna/
Source0:      http://web.comhem.se/luna/Mx44.2.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gtk2-devel
BuildRequires: alsa-lib-devel

%description
Mx44 is a polyphonic multichannel midi realtime software synthesizer.

%prep
%setup -qn Mx44.2

%build

cd src
make %{?_smp_mflags}

%install

cd src

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 mx44 %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_datadir}/Mx44/
%__install -m 644 ../data/mx44patch %{buildroot}/%{_datadir}/Mx44/
%__install -m 644 ../data/gtk-2.0/gtkrc %{buildroot}/%{_datadir}/Mx44/

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.44.2
- inital release
