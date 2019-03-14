%global debug_package %{nil}

Summary: ProTracker is a chiptune tracker for making chiptune-like music on a modern computer.
Name:    protracker
Version: 2.3r167
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://16-bits.org/pt.php
Source0: protracker-r167.tar.gz

# svn export -r 167 https://svn.code.sf.net/p/protracker/code/ protracker-r167
# tar cvfz protracker-r167.tar.gz protracker-r167/*

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: SDL2-devel

%description
ProTracker is a chiptune tracker for making chiptune-like music on a modern computer.

%prep
%setup -qn %{name}-r167

%build

cd trunk
%{__make} DESTDIR=%{buildroot} PREFIX=/usr

%install

%{__rm} -rf %{buildroot}

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__cp trunk/release/other/%{name} %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
%__install -m 644 screenshot.png %{buildroot}/%{_datadir}/icons/%{name}/%{name}.png

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}
%__cp COPYING.txt readme.txt trunk/release/help.txt trunk/release/other/protracker.ini %{buildroot}%{_datadir}/%{name}

%clean

%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/icons/*

%changelog
* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r176-1
- Initial release of spec file
