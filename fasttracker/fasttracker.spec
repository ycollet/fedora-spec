Name:    fasttracker2
Version: 1.35
Release: 3%{?dist}
Summary: Module tracker software for creating music
License: GPLv3+
URL:     https://16-bits.org/ft2.php

Source0: https://github.com/8bitbubsy/ft2-clone/archive/v%{version}.tar.gz#/ft2-clone-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake

%description
FastTracker 2 is a music tracker created by Fredrik "Mr. H" Huss and Magnus "Vogue" Högdahl, two members of the demogroup Triton
(who later founded Starbreeze Studios) which set about releasing their own tracker after breaking into the scene in 1992 and winning several demo competitions.
The source code of FastTracker 2 is written in Pascal using Borland Pascal 7 and TASM. The program works natively under MS-DOS.

%prep
%autosetup -n ft2-clone-%{version}

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build

%install

%cmake_install

mv %{buildroot}/%{_bindir}/ft2-clone %{buildroot}/%{_bindir}/fasttracker2

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack fasttracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse fasttracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa fasttracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

%files
%doc README.md
%license LICENSE LICENSES.txt
%{_bindir}/*

%changelog
* Mon Sep 28 2020 Yann Collette <ycollette.nospam@free.fr> - 1.35-3
- update to 1.35-3

* Thu Sep 10 2020 Yann Collette <ycollette.nospam@free.fr> - 1.34-3
- update to 1.34-3

* Mon Sep 7 2020 Yann Collette <ycollette.nospam@free.fr> - 1.33-3
- update to 1.33-3

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.32-3
- update to 1.32-3

* Sun Aug 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.31-3
- update to 1.31-3

* Sun Aug 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.30-3
- update to 1.30-3

* Sun Aug 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.28-3
- update to 1.28-3

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.27-3
- update to 1.27-3

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.26-3
- update to 1.26-3

* Fri Jun 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.25-3
- update to 1.25-3

* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.24-3
- update to 1.24-3

* Mon May 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.23-3
- update to 1.23-3

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.21-3
- update to 1.21-3

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.17-3
- update to 1.17-3

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.17-1
- update to 1.17

* Thu Apr 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.15-1
- update to 1.15

* Wed Mar 18 2020 Yann Collette <ycollette.nospam@free.fr> - 1.13-1
- update to 1.13

* Sat Mar 14 2020 Yann Collette <ycollette.nospam@free.fr> - 1.12-1
- update to 1.12

* Tue Mar 3 2020 Yann Collette <ycollette.nospam@free.fr> - 1.10-1
- update to 1.10

* Sun Feb 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.09-1
- update to 1.09

* Sat Feb 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.08-1
- update to 1.08

* Fri Jan 31 2020 Yann Collette <ycollette.nospam@free.fr> - 1.07-1
- update to 1.07

* Thu Jan 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.06-1
- update to 1.06

* Sun Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.05-1
- update to 1.05

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.01-1
- update to 1.01

* Sat Aug 17 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b166-1
- update to 0.1b166

* Mon Aug 5 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b164-1
- update to 0.1b164

* Thu Feb 21 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b137-1
- initial spec file
