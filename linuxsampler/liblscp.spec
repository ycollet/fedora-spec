Summary: LinuxSampler Control Protocol library
Name: liblscp
Version: 0.5.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://qsampler.sourceforge.net/qsampler-index.html
Distribution: Planet CCRMA
Vendor: Planet CCRMA

Source0: http://download.linuxsampler.org/packages/liblscp-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: automake, autoconf, libtool
BuildRequires: linuxsampler-devel
BuildRequires: gcc gcc-c++

%description
LinuxSampler Control Protocol library

%package devel
Summary: LinuxSampler Control Protocol library developer resources
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
LinuxSampler Control Protocol library developer resources

%prep
%setup -q
if [ -f Makefile.cvs ]; then make -f Makefile.cvs; fi

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_libdir}/liblscp.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/lscp
%{_libdir}/liblscp.so
%{_libdir}/liblscp.a
%exclude %{_libdir}/liblscp.la
%{_libdir}/pkgconfig/lscp.pc

%changelog
* Mon Nov 5 2018 Yann Collette <ycollette.nospam@free.fr> 0.5.8-1
- update to 0.5.8

* Sun Aug 28 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.7-1
- update to 0.5.7

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.6-1
- updated to 0.5.6

* Tue Jul  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.5-1
- updated to 0.5.5

* Tue Jul  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.3-1
- updated to 0.5.3

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.2-1
- updated to 0.4.2

* Mon Jun 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.3-1
- updated to 0.3.3

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.0-1
- updated to 0.3.0

* Thu May 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.9-1
- updated to 0.2.9

* Thu Jan 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.4-1
- initial build.
