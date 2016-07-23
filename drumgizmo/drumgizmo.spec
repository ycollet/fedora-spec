Summary: Software Synthesizer
Name: drumgizmo
Version: 0.9.10
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL:            http://git.drumgizmo.org/drumgizmo.git
Source0:        drumgizmo-%version.tar.gz
Source1:        drumgizmo_autogen.sh

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: zita-resampler-devel
BuildRequires: expat-devel
BuildRequires: libpng-devel
BuildRequires: cppunit-devel
BuildRequires: libsmf-devel
BuildRequires: gettext-devel
BuildRequires: libxcb-devel
BuildRequires: mesa-libGLU-devel

%description
DrumGizmo is an open source cross-platform drum plugin and stand-alone application. It is comparable to several commercial drum plugin products. 

%prep
%setup -qn %{name}-%version

%build

cp %{SOURCE1} .
./drumgizmo_autogen.sh
%configure --enable-lv2 --libdir=%{_libdir}

%{__make} DESTDIR=%{buildroot} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# desktop file categories
BASE="X-PlanetCCRMA X-Fedora Application AudioVideo"
XTRA="X-Synthesis X-MIDI X-Jack"
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/drumgizmo
%{_libdir}/*
%{_datadir}/man/*
%exclude %{_bindir}/dgreftest

%changelog
* Thu May 12 2016 Yann Collette <ycollette dot nospam at free.fr> 0.9.10-1
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.9.8.1-1
- Initial release of spec fil to 0.9.8.1
