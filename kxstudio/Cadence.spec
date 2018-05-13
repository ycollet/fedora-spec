# Global variables for github repository
%global commit0 b82db9af8d0beb5c89731fee6f8de2d9db87e263
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           Cadence
Version:        1.0.0.%{shortcommit0}
Release:        4%{?dist}
Summary:        A JACK control center

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/falkTX/Cadence
Source0:        https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         cadence_001_fedora_support.patch

BuildRequires: python3-qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-module-jack
BuildRequires: python3-dbus
BuildRequires: a2jmidid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: jack_capture

Requires(pre): python3-qt5
Requires(pre): jack_capture
Requires(pre): a2jmidid

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
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master + qt5
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - master
- Initial build
