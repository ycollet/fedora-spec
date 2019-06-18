%global debug_package %{nil}

# Global variables for github repository
%global commit0 e3b3d2a9c20f56662043e4645f651ea707f6553d
%global gittag0 v0.8.9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Jack Video Monitor
Name:    xjadeo
Version: 0.8.9
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://xjadeo.sourceforge.net/
Source0: https://github.com/x42/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: xjadeo.desktop

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gettext-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libltc-devel
BuildRequires: liblo-devel
BuildRequires: freetype-devel
BuildRequires: ffmpeg-devel
BuildRequires: libXv-devel
BuildRequires: SDL2-devel
BuildRequires: libXpm-devel

%description
xjadeo is a simple video player that gets sync from jack.
Please refer to the documentation in the doc folder for any details,
or visit http://xjadeo.sf.net/

%prep
%setup -qn %{name}-%{commit0}

%build

./autogen.sh
%configure --without-portmidi --libdir=%{_libdir}

sed -i -e 's/-lporttime//g' src/Makefile
sed -i -e 's/-lporttime//g' src/xjadeo/Makefile

cd src/xjadeo
%{__make} PREFIX=/usr paths.h
cd ../..
%{__make} DESTDIR=%{buildroot} PREFIX=/usr %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} PREFIX=/usr install

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/xjadeo/
%__install -m 644 src/xjadeo/icons/xjadeoH128.png %{buildroot}/%{_datadir}/icons/xjadeo/
%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# desktop file categories
BASE="X-PlanetCCRMA X-Fedora Application AudioVideo"
XTRA="X-MIDI X-Jack"
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%clean
%{__rm} -rf %{buildroot}

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/xjadeo >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/xjadeo >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/xjadeo >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/xjadeo &>/dev/null || :

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog INSTALL NEWS README xjadeo.lsm
%license COPYING
%{_bindir}/*
%{_datadir}/man/*
%{_datadir}/xjadeo/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%changelog
* Fri May 3 2019 Yann Collette <ycollette dot nospam at free.fr> 0.8.9-1
- update to 0.8.9-1

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.8.7-1
- update for Fedora 29

* Mon Apr 2 2018 Yann Collette <ycollette dot nospam at free.fr> 0.8.7-1
- Initial release of spec file
