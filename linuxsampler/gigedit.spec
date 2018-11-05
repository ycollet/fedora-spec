Summary: Instrument editor for gig files
Name: gigedit
Version: 1.1.0
Release: 1%{?dist}
License: GPL2
Group: Applications/Multimedia
URL: http://www.linuxsampler.org/
Source0: http://download.linuxsampler.org/packages/gigedit-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: hicolor-icon-theme
Packager: Fernando Lopez-Lezcano
Distribution: Planet CCRMA
Vendor: Planet CCRMA

BuildRequires: intltool gtkmm30-devel libgig-devel libsndfile-devel
BuildRequires: linuxsampler-devel libxslt-devel docbook-style-xsl
BuildRequires: gcc gcc-c++

%description
Gigedit is an instrument editor for gig files. Gig files are
used by software samplers such as LinuxSampler and GigaStudio.

With gigedit it is possible to modify existing gig files and also to
create completely new instruments from scratch. Gigedit can be run as
a stand-alone application, or as a plugin to LinuxSampler.

Please note that this is an early version that only includes the most
basic features needed to create and edit gig files. There is still a
lot to do, fix and improve. Be sure to backup your original gig files
before editing them in gigedit.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/quickstart/*html doc/quickstart/*png doc/quickstart/*css
%{_bindir}/gigedit
%exclude %{_libdir}/gigedit/libgigedit.a
%exclude %{_libdir}/gigedit/libgigedit.la
%{_libdir}/gigedit/libgigedit.so*
%exclude %{_libdir}/linuxsampler/plugins/libgigeditlinuxsamplerplugin.a
%exclude %{_libdir}/linuxsampler/plugins/libgigeditlinuxsamplerplugin.la
%{_libdir}/linuxsampler/plugins/libgigeditlinuxsamplerplugin.so
%exclude %{_datadir}/doc/gigedit
%{_datadir}/gigedit
%{_datadir}/locale/de/LC_MESSAGES/gigedit.mo
%{_datadir}/locale/sv/LC_MESSAGES/gigedit.mo

%changelog
* Mon Nov 5 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0

* Sun Aug 28 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.0-1
- update to 1.0.0
- add libxslt-devel build requirement

* Sat Jul 10 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 
- remove and relink libtool with proper binary

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.0-1
- add check for libsigc++ so that proper link libraries are used for
  fc13/gcc4.4.4

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.0-1
- updated to 0.2.0

* Sat Oct 18 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.1
- initial build.
