Summary: Software Synthesizer
Name:    drumgizmo
Version: 0.9.15
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://git.drumgizmo.org/drumgizmo.git
Source0: http://www.drumgizmo.org/releases/drumgizmo-%version/drumgizmo-%version.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig

# Drumgizmo LV2 plugin
BuildRequires: lv2-devel
BuildRequires: zita-resampler-devel
BuildRequires: libsndfile-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel

# Drumgizmo command-line tools
BuildRequires: expat-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsmf-devel
BuildRequires: alsa-lib-devel

%description
DrumGizmo is an open source, multichannel, multilayered, cross-platform drum plugin and stand-alone application. It enables you to compose drums in midi and mix them with a multichannel approach. It is comparable to that of mixing a real drumkit that has been recorded with a multimic setup.

%prep
%setup -qn %{name}-%version

%build

%configure --enable-lv2 --libdir=%{_libdir} 
# --disable-cli --with-lv2dir=

%{__make} DESTDIR=%{buildroot} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

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
* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 0.9.14-2
* Mon Oct 23 2017 Yann Collette <ycollette dot nospam at free.fr> 0.9.14-1
* Thu May 12 2016 Yann Collette <ycollette dot nospam at free.fr> 0.9.10-1
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.9.8.1-1
- Initial release of spec fil to 0.9.8.1
