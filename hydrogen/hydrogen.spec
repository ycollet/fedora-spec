%global debug_package %{nil}

Name:         hydrogen
Version:      0.9.7
Release:      11%{?dist}
Summary:      Advanced drum machine for GNU/Linux
URL:          http://www.hydrogen-music.org/
Group:        Applications/Multimedia

License:      GPLv2+

Source0:      %{name}-%{version}.tar.gz
# Remove the "you are using the development version" warning
# http://sourceforge.net/mailarchive/forum.php?forum_name=hydrogen-devel
# See the "0.9.5 is out" thread
#Patch1:       hydrogen-devel-warning.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: flac-devel 
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: lash-devel 
BuildRequires: liblrdf-devel
BuildRequires: libsndfile-devel
BuildRequires: libtar-devel
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: qt4-devel
BuildRequires: libarchive-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: rubberband-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: filesystem

%description
Hydrogen is an advanced drum machine for GNU/Linux. The main goal is to bring 
professional yet simple and intuitive pattern-based drum programming.

%package -n ladspa-wasp-booster
Summary:        WASP Booster LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-wasp-booster
WASP Booster LADSPA plugin

%package -n ladspa-wasp-noisifier
Summary:        WASP Noisifier LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-wasp-noisifier
WASP Noisifier LADSPA plugin

%package -n ladspa-wasp-xshaper
Summary:        WASP XShaper LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-wasp-xshaper
WASP XShaper LADSPA plugin

%prep
%setup0 -q
sed -i -e "s/Sound/X-Sound/g" linux/hydrogen.desktop
#%patch1 -p1 -b .nodevver

%build

%cmake -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DWANT_ALSA:BOOL=ON \
       -DWANT_CPPUNIT:BOOL=OFF \
       -DWANT_DEBUG:BOOL=OFF \
       -DWANT_JACK:BOOL=ON \
       -DWANT_JACKSESSION:BOOL=ON \
       -DWANT_LADSPA:BOOL=ON \
       -DWANT_LASH:BOOL=ON \
       -DWANT_LIBARCHIVE:BOOL=ON \
       -DWANT_LRDF:BOOL=OFF \
       -DWANT_NSMSESSION:BOOL=ON \
       -DWANT_OSS:BOOL=OFF \
       -DWANT_PORTAUDIO:BOOL=OFF \
       -DWANT_PORTMIDI:BOOL=OFF \
       -DWANT_PULSEAUDIO:BOOL=ON \
       -DWANT_RUBBERBAND:BOOL=ON \
       -DWANT_SHARED:BOOL=ON \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       .

make VERBOSE=1 %{?_smp_mflags}

#qmake-qt4 src/plugins/plugins.pro "CONFIG+=debug" "CFLAGS+=-ggdb"
qmake-qt4 src/plugins/plugins.pro
make -f src/plugins/Makefile

%install

make DESTDIR=%{buildroot} install

#Install the wasp plugins
%__install -m 755 -d %{buildroot}%{_libdir}/ladspa/
%__install -m 644 libwasp*.so %{buildroot}%{_libdir}/ladspa/

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Drumming \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi


%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files
%doc AUTHORS ChangeLog COPYING* README.txt
%{_bindir}/hydrogen
%{_bindir}/h2cli
%{_bindir}/h2player
%{_bindir}/h2synth
%{_datadir}/hydrogen/
%{_datadir}/applications/hydrogen.desktop
%{_datadir}/appdata/hydrogen.appdata.xml
%{_libdir}/*.so
%exclude %{_usr}/man/*
%exclude %{_includedir}/%{name}

%files -n ladspa-wasp-booster
%{_libdir}/ladspa/libwasp_booster.so 

%files -n ladspa-wasp-noisifier
%{_libdir}/ladspa/libwasp_noisifier.so 

%files -n ladspa-wasp-xshaper
%{_libdir}/ladspa/libwasp_xshaper.so 

%changelog
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9.7-11
- Remove scons

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9.6-11
- Update to version 0.9.6

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.5.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.9.5.1-8
- format-security patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-6
- Fix scons build once again

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.5.1-5
- Drop desktop vendor tag.

* Sun Jul 22 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-4
- Use pkg-config to detect cflags for liblrdf since raptor header file location changed

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-2
- Rebuilt for c++ ABI breakage

* Sun Feb 19 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-1
- Update to 0.9.5.1. Drop upstreamed patch.

* Mon Jan 16 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5-3
- gcc-4.7 compile fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 27 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5-1
- Update to 0.9.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.2-3
- Fix data directory. Fixes RHBZ#643622

* Wed Sep 29 2010 jkeating - 0.9.4.2-2
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.2-1
- Update to 0.9.4.2
- Drop all upstreamed patches

* Sat Apr 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.1-1
- Update to 0.9.4.1
- Build the wasp plugins
- Fixes ladspa plugin path on 64bit systems
- Fixes crash RHBZ#570348

* Sat Feb 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-3
- Fix DSO linking RHBZ#564719

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-2
- Add patch against portmidi-200 on F13+. Fixes RHBZ#555488

* Tue Sep 15 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-1
- Update to 0.9.4

* Sat Aug 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.7.rc2
- Update to 0.9.4-rc2

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.6.rc1.1
- Update .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.5.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.4.rc1.1
- Rebuild against new lash build on F-12 due to the e2fsprogs split

* Tue Apr 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.3.rc1.1
- Update to 0.9.4-rc1-1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.2.790svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.1.790svn
- Update to 0.9.4-beta3 (uses scons and qt4)

* Fri Apr 04 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.9.3-13
- QT3 changes by rdieter
- Fix build

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.3-12
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-11
- Previous change was not a good idea
- Adding missing includes to fix build with gcc-4.3

* Sun Oct 14 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-10
- Remove unneeded dependencies on desktop-file-utils

* Tue Oct 09 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-9
- Incorporate fixes from #190040, thanks to Hans de Goede
- Removed useless LIBDIR introduced in previous revision
- Fixed desktop file installation
- Call gtk-update-icon-cache only if it is present

* Sun Oct 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-8
- Remove -j from make to fix concurrency problems
- Handle libdir on 64bit platforms correctly
- Rename patches

* Sat Oct 06 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-7.1
- Fix desktop file
- Fix compatibility with new FLAC
- Fix linking for Build ID use

* Mon Mar 26 2007 Anthony Green <green@redhat.com> 0.9.3-7
- Improve Source0 link.
- Add %%post(un) scriptlets for MimeType update.
- Add update-desktop-database scriptlets.

* Sat Jul 22 2006 Anthony Green <green@redhat.com> 0.9.3-6
- Add hydrogen-null-sample.patch to fix crash.

* Sun Jul 02 2006 Anthony Green <green@redhat.com> 0.9.3-5
- Clean up BuildRequires.
- Configure with --disable-oss-support
- Don't run ldconfig (not needed)
- Remove post/postun scriptlets.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-4
- BuildRequire libxml2-devel.
- Remove explicit Requires for some runtime libraries.
- Set QTDIR via /etc/profile.d/qt.sh.
- Update desktop icons and icon cache in post and postun.
- Don't use __rm or __make macros.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-3
- Conditionally apply ardour-lib64-ladspa.patch.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-2
- Build fixes for x86_64.

* Wed Apr 26 2006 Anthony Green <green@redhat.com> 0.9.3-1
- Created.
