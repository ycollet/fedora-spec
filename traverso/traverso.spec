Name:    traverso
Version: 0.49.6
Release: 3%{?dist}
Summary: Traverso: A Multitrack Audio Recorder and Editor
URL:     https://savannah.nongnu.org/projects/traverso/
License: GPLv2+

# ./traverso-source.sh <tag>
# ./traverso-source.sh master

Source0: traverso.tar.gz
Source1: traverso-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: filesystem
BuildRequires: libsndfile-devel
BuildRequires: wavpack-devel
BuildRequires: flac-devel 
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: fftw-devel
BuildRequires: libmad-devel
BuildRequires: libsamplerate-devel
BuildRequires: lilv-devel

%description
Traverso: A Multitrack Audio Recorder and Editor

%prep
%autosetup -n %{name}

%build

%cmake

%cmake_build

%install

%cmake_install

%files
%{_bindir}/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.49.6-3
- fix debug build

* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.49.6-2
- fix for fedora 32

* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 0.49.6-1
- update to 0.49.6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.49.1-1
- update for Fedora 29

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.49.1-1
- inital release
