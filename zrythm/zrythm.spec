%global debug_package %{nil}

Name:    zrythm
Version: 0.6.384
Release: 2%{?dist}
Summary: Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use.

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://git.zrythm.org/git/zrythm

Source0: https://download.savannah.nongnu.org/releases/zrythm/zrythm-%{version}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: libyaml-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: gtk3-devel
BuildRequires: portaudio-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fftw-devel
BuildRequires: libgtop2-devel
BuildRequires: meson
BuildRequires: help2man
BuildRequires: python3-sphinx

%description
Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use. Zrythm sets itself apart from other DAWs by allowing extensive automation via built-in LFOs and envelopes and intuitive MIDI or audio editing and arranging via clips.
In the usual Composing -> Mixing -> Mastering workflow, Zrythm puts the most focus on the Composing part. It allows musicians to quickly lay down and process their musical ideas without taking too much time for unnecessary work.
It is written in C and uses the GTK+3 toolkit, with bits and pieces taken from other programs like Ardour and Jalv.
More info at https://www.zrythm.org

%prep
%setup -qn zrythm-%{version}

sed -i -e "s/sphinx_build,/'sphinx-build-3',/g" doc/user/meson.build

%build

mkdir build
cd build
DESTDIR=%{buildroot} VERBOSE=1 meson .. -Dmanpage=true -Duser_manual=true --buildtype release --prefix /usr

DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 
cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Sep 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.384-2
- update to 0.6.384

* Sun Sep 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.323-1
- update to 0.6.323

* Wed Aug 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.039-1
- update to 0.6.039

* Sun Jul 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.162-1
- Initial build
