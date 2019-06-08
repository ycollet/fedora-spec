# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 97b79d17b390f70890928cebf74bb28acf32ecea
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    zytrax
Version: 0.9.0.%{shortcommit0}
Release: 1%{?dist}
Summary: ZyTrax is an easy to use music sequencer with an interface heavily inspired by 90's tracker software 
URL:     https://github.com/reduz/zytrax.git
Group:   Applications/Multimedia

License: GPLv2+

Source0: https://github.com/reduz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: SConstruct-zytrax

BuildRequires: gcc gcc-c++
BuildRequires: make scons
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gtkmm30-devel
BuildRequires: freetype-devel
BuildRequires: rtmidi-devel
BuildRequires: pulseaudio-libs-devel

%description
ZyTrax is an easy to use music sequencer with an interface heavily
inspired by 90's "tracker" software.

While contemporary software that uses this approach exists, it
usually has a high entry barrier because it maintains compatibility
with old formats.

In contrast to this, ZyTrax starts afresh with an user friendly
approach (no hex numbers, pure plugin-based architecture, inlined
automation envelopes, smart automations, zoomable patterns and a
simple pattern/orderlist layout).

%prep
%setup -qn %{name}-%{commit0}

cp %{SOURCE1} SConstruct

%build

export XDG_CURRENT_DESKTOP="kde"

scons 

cat > zytrax.desktop << EOF
[Desktop Entry]
Name=Zytrax
Comment=An audio tracker
Exec=/usr/bin/zytrax
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/zytrax.png
Categories=Audio;
EOF

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 bin/zytrax %{buildroot}%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
%__install -m 644 zytrax.png %{buildroot}/%{_datadir}/pixmaps/
%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 zytrax.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/zytrax.desktop

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%files
%doc README.md LICENSE
%{_bindir}/*
%{_datadir}/applications/zytrax.desktop
%{_datadir}/pixmaps/zytrax.png

%changelog
* Sat Jun 08 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- Initial spec file 1.0alpha-1
