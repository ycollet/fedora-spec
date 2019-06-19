# svn co https://svn.linuxsampler.org/svn/libgig/trunk libgig
# define svn 3425

Summary: C++ library for loading Gigasampler files and DLS Level 1/2 files.
Name:    libgig
Version: 4.1.0
Release: 1%{?svn:.svn%{svn}.1}%{?dist}
License: GPL
Group:   System Environment/Libraries
Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Source0: http://download.linuxsampler.org/packages/libgig-%{version}%{?svn:-svn%{svn}}.tar.bz2
URL:     http://www.linuxsampler.org/libgig/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: libsndfile-devel audiofile-devel doxygen
%if 0%{?fedora} >= 12
BuildRequires: libuuid-devel
%else
BuildRequires: e2fsprogs-devel
%endif

%description
C++ library for loading Gigasampler files and DLS Level 1/2 files.

%package devel
Summary: C++ library for loading Gigasampler files and DLS Level 1/2 files.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
C++ library for loading Gigasampler files and DLS Level 1/2 files.

%prep
%setup -q -n libgig%{!?svn:-%{version}}
if [ -f Makefile.cvs ]; then make -f Makefile.cvs; fi

%build
%configure
%{__make} %{?__smp_mflags}
%{__make} docs

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}
%{makeinstall}

# move libgig.* to /usr/_libdir/
mv %{buildroot}%{_libdir}/libgig/lib* %{buildroot}%{_libdir}/
rmdir %{buildroot}%{_libdir}/libgig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO doc/html
%license COPYING
%{_bindir}/*
%{_libdir}/libgig.so*
%{_libdir}/libakai.so*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%doc doc/html/*
%{_libdir}/libgig.a
%{_libdir}/libakai.a
%exclude %{_libdir}/libgig.la
%exclude %{_libdir}/libakai.la
%{_libdir}/pkgconfig/gig.pc
%{_libdir}/pkgconfig/akai.pc
%{_includedir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free dot fr> 4.1.0-1
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette dot nospam at free dot fr> 4.1.0-1
- update to 4.1.0

* Sun Aug 28 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 4.0.0-1
- update to 4.0.0

* Wed Dec 10 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.0-3.svn2680.1
- update to svn 2680 for building on fc21
- added libakai.* and akai.pc

* Wed May 30 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.0-3.svn2346.1
- update to svn 2346 (matches new fc17 linuxsampler)

* Wed Mar  7 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.0-3.svn2325
- update to current svn for bzf support

* Tue May 25 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.0-2
- add uuid-devel build dependency on fc >= 12

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.0-1
- updated to 3.3.0
- added e2fsprogs-devel build requirement (for uuid generation)

* Tue May 13 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.1-1
- updated to version 3.2.1
- added patch from libgig cvs to fix build on gcc 4.3 for f9

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.0-1
- updated to version 3.2.0

* Mon Jul  2 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.1.1-1
- updated to version 3.1.1

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.1.0-1
- updated to version 3.1.0

* Sat May 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.0.0-1
- updated to version 3.0.0

* Fri Nov 25 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0.2-0.1.cvs
- experimental cvs version with write support
  cvs -z3 -d:pserver:anonymous@cvs.linuxsampler.org:/var/cvs/linuxsampler co libgig

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0.1-1
- updated to 2.0.1

* Sun May 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0.0-1
- updated to 2.0.0

* Thu Jan 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- packaged for Planet CCRMA from original spec file in tarball
- spec file tweaks

* Wed Nov 24 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- prepared for 1.0.0

* Sat Jul 10 2004 Christian Schoenebeck <cuse@users.sourceforge.net>
- renamed 'libgig.pc' to 'gig.pc' as well as the pkg-config lib name

* Fri Jul 02 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Created and corrected initial libgig.spec
