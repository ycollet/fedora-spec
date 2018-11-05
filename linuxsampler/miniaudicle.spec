Summary: Light weight ChucK development environment
Name:    miniaudicle
Version: 1.3.5.2
Release: 1%{?dist}
License: LGPL
Group:   Applications/Multimedia
URL:     http://audicle.cs.princeton.edu/mini/
Source0: http://audicle.cs.princeton.edu/mini/release/files/miniAudicle-%{version}%{?beta:-%{?beta}}.tgz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Packager:     Fernando Lopez-Lezcano
Vendor:       Planet CCRMA
Distribution: Planet CCRMA

BuildRequires: gcc gcc-c++ perl
BuildRequires: bison flex qt-devel qscintilla-devel
BuildRequires: jack-audio-connection-kit-devel alsa-lib-devel
BuildRequires: libsndfile-devel pulseaudio-libs-devel

%description
The miniAudicle is a light-weight integrated development environment
for the ChucK digital audio programming language. It can be used as a
standalone ChucK development + runtime + on-the-fly programming
environment, or in conjunction with traditional command-line modes of
'chuck' operation and with other chuck tools.

%prep
%setup -q -n miniAudicle-%{version}%{?beta:-%{?beta}}

%build
# build alsa version
cd src

# insert rpm flags in qmake profile
perl -p -i -e "s|QMAKE_LFLAGS \+=|QMAKE_LFLAGS \+= %{__global_ldflags}|g" miniAudicle.pro
perl -p -i -e "s|CFLAGS \+=|CFLAGS \+= %{optflags}|g" miniAudicle.pro

# write proper lib path in default preferences
perl -p -i -e "s|/usr/local/lib/chuck|%{_libdir}/chuck|g" chuck/src/chuck_dl.cpp

# build alsa version
%{__make} linux-alsa
%{__mv} miniAudicle miniAudicle-alsa

# build pulse version
%{__make} clean
%{__make} linux-pulse
%{__mv} miniAudicle miniAudicle-pulse

# build jack version
%{__make} clean
%{__make} linux-jack

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
cd src
# install jack version (last built)
%{__install} -m 755 miniAudicle %{buildroot}%{_bindir}/miniAudicle
# install alsa version
%{__install} -m 755 miniAudicle-alsa %{buildroot}%{_bindir}/miniAudicle-alsa
# install pulse version
%{__install} -m 755 miniAudicle-pulse %{buildroot}%{_bindir}/miniAudicle-pulse

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc BUGS COPYING README.linux VERSIONS
%{_bindir}/miniAudicle*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Sun Dec  3 2017 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add rpm CFLAGS/LDFLAGS to qmake profile

* Mon Oct 17 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- fix default lib path for chugins

* Wed Oct 12 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.6.0-1.220a
- update to experimental 1.3.6.0 (released for the 220a class)

* Tue Jan 14 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1-1
- update to 1.3.1, add pulse build

* Sun Sep 29 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.0a-1
- updated to 1.3.0a

* Sat Sep 14 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add optflags for proper build on arm

* Thu Aug 29 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-0.1.beta15
- updated to the latest beta-15 test release, use qt-devel now

* Tue Oct  2 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2c-1
- udpated to 0.2.2c

* Mon Sep 24 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2b-1
- updated to 0.2.2b

* Mon Sep 10 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-1
- updated to 0.2.2, now compiles and works on x86_64

* Wed Aug 29 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.1b-1
- updated to 0.2.1b

* Sat Aug 25 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.1-1
- updated to 0.2.1

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add patch to link chuck with -lpthread for fc13/gcc4.4.4

* Mon Oct 12 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.0-1
- updated to 0.2.0

* Fri Sep  4 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3.8b-2
- include newer version of chuck to make it build on fc11, add
  -fno-strict-aliasing so chuck gets compiled with the right
  options for fc11

* Wed Jul  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- build fixes for gcc4.3 on fc9

* Mon Oct  8 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3.8b-1
- unofficial update/fix release
- make clean does not work, also make clean the chuck subdirectory

* Thu Oct  4 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3.8-1
- update to 0.1.3.8, build for alsa only and jack

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3.6-2
- build for fc6

* Fri Sep 22 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3.6-1
- update to 0.1.3.6

* Thu Aug 17 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3.5-1
- initial build
