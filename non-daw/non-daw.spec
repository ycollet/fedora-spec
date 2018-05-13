# Version: 5ae43bb27c42387052a73e5ffc5d33efb9d946a9

Name:           non-daw
Version:        1.2.0
Release:        8.git3946d39%{?dist}
Summary:        A digital audio workstation for JACK

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://non.tuxfamily.org/
Source0:        non-20180512-git5ae43bb27c42387052a73e5ffc5d33efb9d946a9.tar.gz
# sh non-snapshot.sh 1904aba516341287ac297cefbbcd185f643e5538
#Source1:        non-snapshot.sh
# notified upstream of the following along with incorrect FSF address headers
#Patch2:         non-daw-0001-add-lib64-in-ladspa-search-path.patch

BuildRequires:  non-ntk-devel
BuildRequires:  non-ntk-fluid
BuildRequires:  liblo-devel
BuildRequires:  libsndfile-devel
BuildRequires:  fltk-fluid
BuildRequires:  fltk-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXpm-devel
BuildRequires:  ladspa-devel
BuildRequires:  liblrdf-devel
BuildRequires:  python2

%description
Non-daw is a digital audio workstation for JACK

%package -n non-mixer
Summary:        A digital audio mixer for JACK
Group:          Applications/Multimedia

%description -n non-mixer
non-mixer is a powerful, reliable and fast modular Digital Audio Mixer

%package -n non-session-manager
Summary:        A session manager for JACK
Group:          Applications/Multimedia

%description -n non-session-manager
non-session-manager is an audio project session manager. It preserves
application state including JACK and MIDI connections between audio sessions.

%package -n non-sequencer
Summary:        A MIDI sequencer for JACK
Group:          Applications/Multimedia

%description -n non-sequencer
non-sequencer is a powerful, lightweight, real-time, pattern-based MIDI 
sequencer

%prep
%setup -q -n non-daw-20120722

#%patch2 -p1

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags} -std=c++11" ./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-debug
./waf -j4 -v 

%install 
./waf install --destdir=%{buildroot} --docdir=%{buildroot}/%{_docdir}/
for i in %{buildroot}%{_datadir}/applications/*.desktop; do
    sed -i -e 's|\/usr\/bin\/||' $i
    desktop-file-validate $i;
done;
# correct permissions
chmod 755 %{buildroot}%{_bindir}/*

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc COPYING
%{_bindir}/import*
%{_bindir}/%{name}
%{_bindir}/non-timeline
%{_docdir}/non-timeline
%{_bindir}/jackpatch
%{_datadir}/applications/non-timeline.desktop
%{_datadir}/icons/hicolor/*/apps/non-timeline*
%{_datadir}/pixmaps/non-timeline

%files -n non-mixer
%{_bindir}/non-mixer
%{_bindir}/non-mixer-noui
%{_bindir}/non-midi-mapper
%{_docdir}/non-mixer
%{_datadir}/applications/non-mixer.desktop
%{_datadir}/icons/hicolor/*/apps/non-mixer*
%{_datadir}/pixmaps/non-mixer

%files -n non-session-manager
%{_bindir}/nsm*
%{_bindir}/non-session-manager
%{_docdir}/non-session-manager
%{_datadir}/applications/non-session-manager.desktop
%{_datadir}/icons/hicolor/*/apps/non-session-manager*
%{_datadir}/pixmaps/non-session-manager

%files -n non-sequencer
%{_bindir}/non-sequencer
%{_docdir}/non-sequencer
%{_datadir}/non-sequencer
%{_datadir}/applications/non-sequencer.desktop
%{_datadir}/icons/hicolor/*/apps/non-sequencer*
%{_datadir}/pixmaps/non-sequencer

%changelog
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-7.git5ae43bb
- update to 20180512-git5ae43bb27c42387052a73e5ffc5d33efb9d946a9

* Tue Oct 24 2017  Yann Collette <ycollette.nospam@free.fr> - 1.2.0-7.git43e5538
- update to non-20171023-git1904aba516341287ac297cefbbcd185f643e5538

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7.git13c3ca8w
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-5.git13c3ca8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-4.git13c3ca8
- rebuild (fltk)
- non-session-manager: omit non-sensical Obsoletes
- fix Release: tag

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3.1.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2.1.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-0.5.git9fba8a8
- New source, adding additional sub packages, non-mixer
- obsoletes non-session-manager, non-sequencer

* Mon Aug 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-0.4.gitae6b78cf
- Unversioned doc dir changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.3.gitae6b78cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.2.gitae6b78cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-0.1.gitae6b78cf
- Initial build
