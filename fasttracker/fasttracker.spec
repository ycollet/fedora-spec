Name:          fasttracker2
Version:       1.17
Release:       2%{?dist}
Summary:       Module tracker software for creating music
Group:         Applications/Multimedia
License:       GPLv3+
URL:           https://16-bits.org/ft2.php
Source0:       https://github.com/8bitbubsy/ft2-clone/archive/v%{version}.tar.gz#/ft2-clone-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake

%description
FastTracker 2 is a music tracker created by Fredrik "Mr. H" Huss and Magnus "Vogue" Högdahl, two members of the demogroup Triton
(who later founded Starbreeze Studios) which set about releasing their own tracker after breaking into the scene in 1992 and winning several demo competitions.
The source code of FastTracker 2 is written in Pascal using Borland Pascal 7 and TASM. The program works natively under MS-DOS.

%prep
%setup -qn ft2-clone-%{version}

%build

mkdir -p build
cd build
%cmake -DCMAKE_BUILD_TYPE=RELEASE ..

make DESTDIR=%{buildroot} PREFIX=/usr %{?_smp_mflags}

%install

%{__rm} -rf %{buildroot}

cd build
make DESTDIR=%{buildroot} PREFIX=/usr install

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSES.txt
%{_bindir}/*

%changelog
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
