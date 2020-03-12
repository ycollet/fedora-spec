%global debug_package %{nil}

Name:    libaudec-devel
Version: 0.2
Release: 1%{?dist}
Summary: libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://git.zrythm.org/git/libaudec

Source0: https://git.zrythm.org/cgit/libaudec/snapshot/libaudec-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: ffmpeg-devel
BuildRequires: meson

%description
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading
and resampling audio files, based on Robin Gareus' 'audio_decoder' code

%prep
%setup -qn libaudec-%{version}

%build

mkdir build
DESTDIR=%{buildroot} VERBOSE=1 meson --prefix=/usr build

cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 

cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja install

%files
%doc COPYING README.md
%{_libdir}/*
%{_includedir}/audec/*

%changelog
* Thu Mar 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- update to 0.2

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
