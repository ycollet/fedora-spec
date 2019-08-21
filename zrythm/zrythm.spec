%global debug_package %{nil}

# Global variables for github repository
%global commit0 a6b47628866798d3bed9f293abfbb485cb9635ae
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    zrythm
Version: 0.6.039.%{shortcommit0}
Release: 1%{?dist}
Summary: Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use.

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://git.zrythm.org/git/zrythm

Source0: https://git.zrythm.org/cgit/zrythm/snapshot/zrythm-%{commit0}.tar.gz

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

%description
Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use. Zrythm sets itself apart from other DAWs by allowing extensive automation via built-in LFOs and envelopes and intuitive MIDI or audio editing and arranging via clips.
In the usual Composing -> Mixing -> Mastering workflow, Zrythm puts the most focus on the Composing part. It allows musicians to quickly lay down and process their musical ideas without taking too much time for unnecessary work.
It is written in C and uses the GTK+3 toolkit, with bits and pieces taken from other programs like Ardour and Jalv.
More info at https://www.zrythm.org

%prep
%setup -qn zrythm-%{commit0}

%build

DESTDIR=%{buildroot} VERBOSE=1 meson --prefix=/usr build

cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 
cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Wed Aug 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.039-1
- update to 0.6.039

* Sun Jul 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.162-1
- Initial build
