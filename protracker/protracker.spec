Summary: Chiptune tracker for making chiptune-like music on a modern computer.
Name:    protracker2
Version: 1.12
Release: 3%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://16-bits.org/pt.php
Source0: https://github.com/8bitbubsy/pt2-clone/archive/v%{version}.tar.gz#/pt2-clone-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: SDL2-devel

%description
ProTracker2 is a chiptune tracker for making chiptune-like music on a modern computer.

Obsoletes: protracker

%prep
%setup -qn pt2-clone-%{version}

%build

LDFLAGS="${LDFLAGS:-%{build_ldflags}} -z muldefs" ; export LDFLAGS
mkdir -p build
cd build
%cmake -DCMAKE_BUILD_TYPE=RELEASE ..

make DESTDIR=%{buildroot} PREFIX=/usr %{?_smp_mflags}

%install

%{__rm} -rf %{buildroot}

cd build
make DESTDIR=%{buildroot} PREFIX=/usr install

mv %{buildroot}/%{_bindir}/pt2-clone %{buildroot}/%{_bindir}/protracker2

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack protracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse protracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa protracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
%__install -m 644 ../src/gfx/pt2-clone.ico %{buildroot}/%{_datadir}/icons/%{name}/%{name}.ico

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}
%__cp ../release/effects.txt ../release/help.txt ../release/keybindings.txt ../release/LICENSES.txt ../release/other/protracker.ini %{buildroot}%{_datadir}/%{name}

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
* Mon May 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.12-3
- update to 1.12-3

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.10-3
- update to 1.10-3

* Fri Apr 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.08-3
- fix for Fedora 32

* Mon Apr 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.08-2
- update to 1.08-2

* Wed Apr 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.07-2
- update to 1.07-2

* Mon Feb 17 2020 Yann Collette <ycollette.nospam@free.fr> - 1.06-2
- update to 1.06-2

* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.04-2
- update to 1.04-2

* Fri Jan 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.03-2
- update to 1.03-2

* Mon Jan 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.02-2
- update to 1.02-2

* Sun Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.01-2
- update to 1.01-2. Rename protracker to protracker2

* Sat Aug 17 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r191-2
- update to revision 191

* Wed Jul 17 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r188-2
- update to revision 188

* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r167-2
- Add pulse and jack script

* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r167-1
- Initial release of spec file
