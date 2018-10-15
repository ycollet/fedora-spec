%global debug_package %{nil}

Summary: An A/B convertor and the metering and monitoring. 
Name:    tetraproc
Version: 0.8.2
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: libsndfile-devel fftw-devel libpng-devel libXft-devel libX11-devel
#BuildRequires: -lsndfile -lfftw3f -lclxclient -lclthreads -ljack -lpng -lXft -lX11 -lrt

%description
Tetraproc consists of two parts: the A/B convertor and the
metering and monitoring. Tetrafile only has the A/B conversion
part which is otherwise identical.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
make PREFIX=%{_prefix} LDLIBS="-lpthread -lsndfile -lfftw3f -lclxclient -lclthreads -ljack -lpng -lXft -lX11 -lrt"
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README* 
%{_bindir}/tetra*
%{_datadir}/tetraproc/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- first release
