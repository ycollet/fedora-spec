# Global variables for github repository
%global commit0 4a5f5b445bfb3cd23a797c172dfbcb42e0cf114f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:    Cadence
Version: 1.0.0.%{shortcommit0}
Release: 5%{?dist}
Summary: JACK control center

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/falkTX/Cadence
Source0: https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  cadence_001_fedora_support.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3-qt4-devel
BuildRequires: python3-qt5-devel
BuildRequires: qt-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-module-jack
BuildRequires: python3-dbus
BuildRequires: a2jmidid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: jack_capture

Requires:      jack-audio-connection-kit-dbus
Requires:      python3-dbus
Requires:      python3-qt4
Requires:      python3-qt5
Requires:      jack_capture
Requires:      a2jmidid


%description
A JACK control center

%prep
%setup -qn %{name}-%{commit0}
%patch0 -p1

%build
make PREFIX=/usr DESTDIR=%{buildroot} %{?_smp_mflags}

%install 
make PREFIX=/usr DESTDIR=%{buildroot} %{?_smp_mflags} install

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
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/cadence/*
%{_datadir}/icons/*
%{_sysconfdir}/*

%changelog
* Thu Jan 3 2019 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - master
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master + qt5

* Sun May 06 2018 Tom Nguyen <tom81094@gmail.com> - master
- added required dependencies to run minimally

* Sun May 06 2018 Tom Nguyen <tom81094@gmail.com> - master
- added Qt5 dependencies

* Sun May 06 2018 Tom Nguyen <tom81094@gmail.com> - master
- update to latest master and fixed fedora patch

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - master
- Initial build
