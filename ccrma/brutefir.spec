Summary: Generic FIR filter (convolution) engine
Name:    brutefir
Version: 1.0k
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://www.ludd.luth.se/~torger/brutefir.html
Source0: http://www.ludd.luth.se/~torger/files/brutefir-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

Packager:     Fernando Lopez-Lezcano
Vendor:       Planet CCRMA
Distribution: Planet CCRMA

BuildRequires: gcc gcc-c++ perl
BuildRequires: fftw-devel flex alsa-lib-devel jack-audio-connection-kit-devel

%description
BruteFIR is a software convolution engine, a program for applying long
FIR filters to multi-channel digital audio, either offline or in
realtime. Its basic operation is specified through a configuration
file, and filters, attenuation and delay can be changed in runtime
through a simple command line interface.

%prep
%setup -q

%build
%if 0%{?fedora} >= 8
# add linker --build-id
%{__perl} -p -i -e "s|= ld|= ld --build-id |g" Makefile
%endif
%ifarch x86_64
%{__perl} -p -i -e "s|/lib/brutefir|/lib64/brutefir|g" Makefile
%endif

%{__make} INSTALL_PREFIX=%{_prefix} LIBPATHS= INCLUDE= \
          DEFINE="${RPM_OPT_FLAGS}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_libdir}/brutefir
%{__make} INSTALL_PREFIX=%{buildroot}%{_prefix} LIBPATHS= INCLUDE= install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES GPL-2.0 LICENSE README 
%{_libdir}/brutefir
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Tue Nov 24 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0k-1
- updated to 1.0k

* Tue Feb  5 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- fixed build on x86_64

* Sun Apr 15 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0i-2
- added --build-id to the linker call so that debuginfo is properly
  generated (see: http://fedoraproject.org/wiki/Releases/FeatureBuildId)

* Sun Apr 15 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0i-1
- updated to 1.0i, build on fc6

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0e-1
- Mario Torre fixed compilation problems on fc4, later fixed 
  upstream in new version

* Fri Dec 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- use rpm optimization flags

* Tue Dec 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup

* Fri Apr 23 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0-1
- initial build.

