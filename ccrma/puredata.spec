# 
# Pure Data vanilla build
#
# http://msp.ucsd.edu/Software/pd-0.47-1.src.tar.gz
# replicate the package structure used by Debian

%define pdver 0.47-1
%define pkgver 0.47.1

Summary: Pure Data
Name: puredata
Version: %{pkgver}
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://msp.ucsd.edu/software.html
Source0: http://msp.ucsd.edu/Software/pd-%{pdver}.src.tar.gz

# in f27 we are getting leftover debuginfo packages that kill the build
# this is a hack
%global debug_package %{nil}

# additional files for the gui package
# desktop file
Source10: puredata.desktop
# icon
Source11: puredata.xpm
# /usr/bin/pd-gui
Source12: pd-gui
# pd-gui man page
Source13: pd-gui.1
# pd-gui plugin (needs python3)
Source14: pd-gui-plugin
# pd gui plugins readme
Source15: README
# mime stuff
Source16: puredata-gui.sharedmimeinfo

# add relevant debian patches
Patch0: debian_system_portaudio.patch
Patch1: fix_spelling_errors.patch
Patch2: debian_pd2puredata.patch
Patch3: debian_usrlibpd_path.patch
Patch4: debian_helpbrowser_puredata-doc.patch
Patch5: debian_remove_timestamp-macros.patch
Patch6: debian_etc-gui-plugins.patch
Patch7: utf8.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf automake libtool
BuildRequires: alsa-lib-devel jack-audio-connection-kit-devel portaudio-devel
BuildRequires: gettext-devel desktop-file-utils

# the main package requires everything else by default (except -devel)
Requires: puredata-core puredata-doc puredata-extra 
Requires: puredata-gui puredata-utils
# for the gui plugin
Requires: python3

%description
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing. Pd's audio functions
are built-in; graphical computations require separate packages such as
gem (Graphics Environment for Multimedia) or pd-pdp (Pd Packet).

%package core
Summary: Pure Data Core

%description core
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package only provides the core infrastructure. Most likely you
will want to install the puredata-gui as well

%package devel
Summary: Pure Data Development files
Requires: puredata-core

%description devel
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides the header-files for compiling externals
(plugins) for puredata.

%package doc
Summary: Pure Data documentation
Requires: puredata-core

%description doc
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides the documentation for Pure Data. Most likely you
will want to install "puredata" as well.

%package extra
Summary: Pure Data extra
Requires: puredata-core

%description extra
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides extra objects that come with Pd, e.g. for signal
analysis (fiddle~, sigmund~, bonk~), expression evaluation (expr~) and
more

%package gui
Summary: Pure Data GUI
Requires: puredata-core

%description gui
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides the graphical user-interface for Pure Data. Most
likely you will want to install "puredata-core" (or even "puredata")
as well.

%package utils
Summary: Pure Data utilities
Requires: puredata-core

%description utils
Pure Data (also known as Pd) is a real-time graphical programming
environment for audio and graphics processing.

This package provides utility applications for puredata, namely pdsend
and pdreceive, for sending and receiving FUDI over the net.

%prep
%setup -q -n pd-%{pdver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
# utf8 support does not currently patch cleanly
# %patch7 -p1

%build
# fix hardwired lib dir in startup file (why the heck is this hardwired?)
perl -p -i -e "s|\"/lib|\"/%{_lib}|g" src/s_main.c
# fix path of pd-externals
perl -p -i -e "s|/usr/local/lib|%{_libdir}|g" src/s_path.c

# now do the build, use "puredata" as the program name
./autogen.sh
%configure --enable-alsa --enable-jack --program-transform-name 's/pd$$/puredata/'
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# add additional stuff needed by the gui package
# create plugins enabled directory
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pd/plugins-enabled
# add desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE10}
perl -p -i -e "s|/lib/|/%{_lib}/|g" $RPM_BUILD_ROOT%{_datadir}/applications/puredata.desktop

# add desktop icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
# pd-gui script and plugin
install -m 755 %{SOURCE12} $RPM_BUILD_ROOT%{_bindir}/pd-gui
perl -p -i -e "s|/lib/|/%{_lib}/|g" $RPM_BUILD_ROOT%{_bindir}/pd-gui
install -m 755 %{SOURCE14} $RPM_BUILD_ROOT%{_bindir}/pd-gui-plugin
# pd-gui man page
install -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_mandir}/man1/pd-gui.1
# REAMDE for plugins
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{_sysconfdir}/pd/plugins-enabled/README
# documentation, intro
mkdir -p $RPM_BUILD_ROOT%{_datadir}/puredata-gui
install -m 644 doc/1.manual/1.introduction.txt $RPM_BUILD_ROOT%{_datadir}/puredata-gui
# mime stuff
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages/
install -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{_datadir}/mime/packages/puredata.xml

# hardlink pd-* binaries
ln -f $RPM_BUILD_ROOT%{_libdir}/puredata/bin/pd $RPM_BUILD_ROOT%{_bindir}/pd
ln -f $RPM_BUILD_ROOT%{_libdir}/puredata/bin/pd-watchdog $RPM_BUILD_ROOT%{_bindir}/pd-watchdog

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create /usr/share/icons/hicolor &> /dev/null || :
/bin/touch --no-create /usr/share/mime/packages &> /dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create /usr/share/icons/hicolor &>/dev/null
    /bin/touch --no-create /usr/share/mime/packages &>/dev/null
    /usr/bin/gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
    /usr/bin/update-mime-database -n /usr/share/mime &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
/usr/bin/update-mime-database -n /usr/share/mime &> /dev/null || :

%files
%defattr(-,root,root,-)
%doc README.txt INSTALL.txt LICENSE.txt

%files core
%defattr(-,root,root,-)
%{_bindir}/pd
%{_bindir}/pd-watchdog
%{_libdir}/puredata/bin/pd
%{_libdir}/puredata/bin/pd-watchdog
%{_sysconfdir}/pd/plugins-enabled
%{_libdir}/puredata/doc/5.reference
%{_libdir}/puredata/doc/7.stuff
%{_mandir}/man1/pd.1*
%{_datadir}/pixmaps/puredata.xpm

%files doc
%defattr(-,root,root,-)
%{_libdir}/puredata/doc/1.manual/
%{_libdir}/puredata/doc/2.control.examples/
%{_libdir}/puredata/doc/3.audio.examples/
%{_libdir}/puredata/doc/4.data.structures/
%{_libdir}/puredata/doc/6.externs/
%{_libdir}/puredata/doc/sound/

%files devel
%defattr(-,root,root,-)
%{_includedir}/m_pd.h
%{_includedir}/pd/
%{_libdir}/pkgconfig/pd.pc

%files extra
%defattr(-,root,root,-)
%{_libdir}/puredata/extra/

%files gui
%defattr(-,root,root,-)
%{_bindir}/pd-gui
%{_bindir}/pd-gui-plugin
%{_bindir}/pd-gui.tcl
%{_libdir}/puredata/tcl/
%{_libdir}/puredata/po
%{_datadir}/applications/puredata.desktop
%{_mandir}/man1/pd-gui*
%{_sysconfdir}/pd/plugins-enabled
%{_datadir}/puredata-gui
%{_datadir}/mime/packages/puredata.xml

%files utils
%defattr(-,root,root,-)
%{_bindir}/pdreceive
%{_bindir}/pdsend
%{_mandir}/man1/pdreceive.1.gz
%{_mandir}/man1/pdsend.1.gz

%changelog
* Wed Nov 23 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 
- do not create symlinks to documentation
- finish adding all the pd-gui stuff from Debian
- borrow pre/post scripts from ardour5 spec file

* Tue Nov 22 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.47.1-1
- initial build, start from scratch with pd vanilla
- replicate Debian package structure, add most patches, many thanks
  to IOhannes m zmolnig (Debian/GNU)
