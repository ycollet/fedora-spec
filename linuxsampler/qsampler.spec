%define	desktop_vendor planetccrma

Summary: LinuxSampler GUI front-end
Name: qsampler
Version: 0.6.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://qsampler.sourceforge.net/qsampler-index.html
Distribution: Planet CCRMA
Vendor: Planet CCRMA

Source0: https://download.sf.net/qsampler/qsampler-%{version}.tar.gz
Source1: qsampler.desktop

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: linuxsampler
Requires: hicolor-icon-theme

BuildRequires: qt5-qtbase-devel qt5-linguist qt5-qtx11extras-devel
BuildRequires: libgig-devel liblscp-devel desktop-file-utils
BuildRequires: libtool automake autoconf
BuildRequires: gcc gcc-c++

%description
QSampler is a LinuxSampler GUI front-end application written in C++
around the Qt5 toolkit using Qt Designer. At the moment it just wraps
as a client reference interface for the LinuxSampler Control Protocol
(LSCP).

%prep
%setup -q

if [ -f Makefile.svn ]; then make -f Makefile.svn; fi

%build
./autogen.sh
%configure --enable-debug

# fix location of include file
find . -type f -exec grep '<gig.h>' {} \; \
               -exec perl -p -i -e "s|<gig.h>|<libgig/gig.h>|g" {} \;
find . -type f -exec grep '\"gig.h\"' {} \; \
               -exec perl -p -i -e "s|\"gig.h\"|\"libgig/gig.h\"|g" {} \;

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# desktop file categories
BASE="Application AudioVideo Audio"
XTRA="X-Jack X-MIDI X-Synthesis Midi"

%{__mkdir} -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{SOURCE1}

%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/qsampler
%{_datadir}/icons/hicolor/32x32/apps/qsampler.png
%{_datadir}/icons/hicolor/scalable/apps/qsampler.svg
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-qsampler-session.png
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-qsampler-session.svg
%{_datadir}/mime/packages/qsampler.xml
%{_datadir}/applications/%{desktop_vendor}-qsampler.desktop
%exclude %{_datadir}/applications/qsampler.desktop
%{_datadir}/metainfo/qsampler.appdata.xml
%{_mandir}/man1/qsampler.1.gz
%{_mandir}/man1/qsampler.fr.1.gz
%{_datadir}/qsampler/translations/qsampler_cs.qm
%{_datadir}/qsampler/translations/qsampler_ru.qm
%{_datadir}/qsampler/translations/qsampler_fr.qm

%changelog
* Thu Mar 26 2020 Yann Collette <ycollette.nospam@free.fr> 0.6.2-1
- update to 0.6.2

* Mon Nov 5 2018 Yann Collette <ycollette.nospam@free.fr> 0.4.2-1
- update to 0.4.2

* Fri Jul  1 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- update to latest for fc24 build
- add patch to build with new gcc (from Debian)

* Fri Dec 12 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-1
- update to latest version for fc21 build
- fix location of include file, add new files to list

* Wed May 30 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-2.svn527
- update to latest svn for fc17 build

* Thu Sep 16 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-2.svn507
- update to latest svn for Fedora 13, fixes segfault on startup

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add patch to link with -lX11 for fc13/gcc4.4.4

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-1
- updated to 0.2.2

* Tue Jul  8 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.1-1
- updated to 0.2.1
- add qmake to the path (otherwise the default is named qmake-qt4
  and is not found)

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.5-1
- updated to version 0.1.5
- updated desktop categories, ignore original desktop file

* Tue Jul  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.4-1
- updated to 0.1.4

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-2
- build for fc6, spec file tweaks

* Sun Jul 30 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-2
- built with libgig support

* Mon Jun 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-1
- updated to 0.1.3
- added Planet CCRMA categories to desktop file, moved icon to proper
  freedesktop location

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.2-1
- updated to 0.1.2

* Thu May 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- updated to 0.1.0, made explicit dependency on linuxsampler
- added menu entry

* Thu Jan 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.4-1 
- initial build.
