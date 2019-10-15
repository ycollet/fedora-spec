%global debug_package %{nil}
%global __python %{__python3}

# Global variables for github repository
%global commit0 f1d112de328c1c591da3c56d0394996e97e27e1e
%global gittag0 0.8.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    RaySession
Version: 0.8.0
Release: 1%{?dist}
Summary: A JACK session manager

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/Houston4444/RaySession

Source0: https://github.com/Houston4444/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python3-qt5-devel
BuildRequires: python3
BuildRequires: qtchooser
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: gtk-update-icon-cache

Requires(pre): python3-qt5
Requires(pre): python3-pyliblo

%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour, Carla, QTractor, Non-Timeline, etc...
It uses the same API as Non Session Manager, so programs compatible with NSM are also compatible with Ray Session.
As Non Session Manager, the principle is to load together audio programs, then be able to save or close all documents together.

%prep
%setup -qn %{name}-%{commit0}

%build
make DESTDIR=%{buildroot} PREFIX=/usr %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} PREFIX=/usr %{?_smp_mflags} install

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
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/raysession/*

%changelog
* Tue Oct 15 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Wed Jul 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.2-1
- update to 0.7.2-1

* Sat May 4 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- Initial spec file
