# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 474637b9e1afbcc87cd4c73b1a0e74c1baf061ab
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    protrekkr
Version: 1.0.0
Release: 1%{?dist}
Summary: A jack tracker

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/falkTX/protrekkr
Source0: https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Patch0:  protrekkr-0001-fix-system-libraries.patch

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: SDL-devel
BuildRequires: zlib-devel
BuildRequires: tinyxml-devel

%description
A jack tracker

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1 

%build
make DESTDIR=%{buildroot} -f makefile.linux %{?_smp_mflags}

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=protrekkr
Comment=Mod tracker
Exec=protrekkr
Icon=protrekkr
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 release/distrib/ptk_linux %{buildroot}%{_bindir}/%{name}

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/instruments/
%__install -m 644 release/distrib/instruments/* %{buildroot}%{_datadir}/%{name}/instruments/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/modules/
%__install -m 644 release/distrib/modules/* %{buildroot}%{_datadir}/%{name}/modules/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/
%__install -m 644 release/distrib/presets/* %{buildroot}%{_datadir}/%{name}/presets/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/reverbs/
%__install -m 644 release/distrib/reverbs/* %{buildroot}%{_datadir}/%{name}/reverbs/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/skins/
%__install -m 644 release/distrib/skins/* %{buildroot}%{_datadir}/%{name}/skins/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 protrekkr.jpg %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.jpg

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
%{_datadir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
