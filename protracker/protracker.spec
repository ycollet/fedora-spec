%global debug_package %{nil}

Summary: ProTracker is a chiptune tracker for making chiptune-like music on a modern computer.
Name:    protracker
Version: 2.3r167
Release: 2%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://16-bits.org/pt.php
Source0: protracker-r167.tar.gz

# svn export -r 167 https://svn.code.sf.net/p/protracker/code/ protracker-r167
# tar cvfz protracker-r167.tar.gz protracker-r167/*

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
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

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack protracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse protracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

%__cp trunk/release/other/%{name} %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
%__install -m 644 screenshot.png %{buildroot}/%{_datadir}/icons/%{name}/%{name}.png

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}
%__cp COPYING.txt readme.txt trunk/release/help.txt trunk/release/other/protracker.ini %{buildroot}%{_datadir}/%{name}

%clean

%{__rm} -rf %{buildroot}

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/%{name} >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/%{name} >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/%{name} >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/icons/*

%changelog
* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r167-2
- Add pulse and jack script

* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r167-1
- Initial release of spec file
