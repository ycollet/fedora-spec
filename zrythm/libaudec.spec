%global debug_package %{nil}

Name:    libaudec-devel
Version: 0.2.3
Release: 1%{?dist}
Summary: libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files
License: GPLv2+
URL:     https://git.zrythm.org/cgit/libaudec

Source0: https://git.zrythm.org/cgit/libaudec/snapshot/libaudec-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: ffmpeg-devel
BuildRequires: meson

%description
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading
and resampling audio files, based on Robin Gareus' 'audio_decoder' code

%prep
%autosetup -n libaudec-%{version}

%build

mkdir build
DESTDIR=%{buildroot} VERBOSE=1 meson --prefix=/usr build

cd build
DESTDIR=%{buildroot} VERBOSE=1 %ninja_build 

%install 

cd build
DESTDIR=%{buildroot} VERBOSE=1 %ninja_install

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_includedir}/audec/*

%changelog
* Sat Aug 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- update to 0.2.3-1

* Sun May 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update to 0.2.2-1

* Thu Mar 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- update to 0.2

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
