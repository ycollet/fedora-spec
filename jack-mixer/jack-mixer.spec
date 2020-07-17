Name:    jack_mixer
Version: 13
Release: 1%{?dist}
Summary: jack_mixer is GTK (2.x) JACK audio mixer with look similar to it`s hardware counterparts
URL:     https://repo.or.cz/jack_mixer.git

License: GPLv2+

# ./sources.sh release-13

Source0: jack_mixer.tar.gz
Source1: python.m4

BuildRequires: gcc
BuildRequires: autoconf automake libtool
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: glib2-devel
BuildRequires: python3-devel
BuildRequires: python3-cairo
BuildRequires: python3-gobject-base

Requires: python3-cairo
Requires: python3-gobject-base

%description
jack_mixer is Gtk Jack audio mixer with look similar to it`s hardware counterparts.
It has lot of useful features, apart from being able to mix multiple Jack audio streams. 

%prep
%autosetup -n %{name}

# Remove unsupported desktop Categories
sed -i -e "s/GTK;GNOME;//g" data/jack_mixer.desktop
sed -i -e "s/Player;//g"    data/jack_mixer.desktop
sed -i -e "45,46d" autogen.sh

%build

%set_build_flags

cp %{SOURCE1} m4/python.m4
./autogen.sh
PYTHON=%{__python3} ./configure --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir}

%make_build

%install

%make_install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/jack_mixer.desktop

%files
%doc NEWS AUTHORS README.md
%license COPYING
%{_bindir}/*
%{_usr}/lib/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/jack_mixer/*

%changelog
* Fri Jul 17 2020 Yann Collette <ycollette.nospam@free.fr> - 13-1
- Initial spec file
