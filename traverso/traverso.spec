# Global variables for github repository
%global debug_package %{nil}

Name:         traverso
Version:      0.49.1
Release:      1%{?dist}
Summary:      Traverso: A Multitrack Audio Recorder and Editor
URL:          https://savannah.nongnu.org/projects/traverso/
Source0:      traverso-master.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

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
%setup -qn %{name}-master

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
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.49.1
- update for Fedora 29

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.49.1
- inital release
