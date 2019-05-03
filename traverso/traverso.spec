# Global variables for github repository
%global debug_package %{nil}

Name:    traverso
Version: 0.49.6
Release: 1%{?dist}
Summary: Traverso: A Multitrack Audio Recorder and Editor
URL:     https://savannah.nongnu.org/projects/traverso/
Source0: traverso-0.49.6.tar.gz
Group:   Applications/Multimedia
License: GPLv2+

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

%description
Traverso: A Multitrack Audio Recorder and Editor

%prep
%setup -qn %{name}-%{version}

%build

mkdir build
cd build
%cmake ..

make VERBOSE=1 %{?_smp_mflags}

%install

cd build
make DESTDIR=%{buildroot} install

%files
%{_bindir}/*

%changelog
* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 0.49.6-1
- update to 0.49.6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.49.1-1
- update for Fedora 29

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.49.1-1
- inital release
