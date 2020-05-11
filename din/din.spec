%global debug_package %{nil}

Summary: DIN is a synth of a 3rd kind
Name:    din
Version: 46.2.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://dinisnoise.org/

Source0: https://archive.org/download/dinisnoise_source_code/din-46.2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: tcl-devel
BuildRequires: SDL-devel
BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils

%description
DIN is a synth of a 3rd kind.
It forgets history,
To not repeat it.
It doesnt hide analog music hardware,
In digital music software.
You had pulse, sine, triangle and sawtooth,
And went forth and made electronic music.

%prep
%setup -qn %{name}-46.2

%build
CFLAGS="-D__UNIX_JACK__ -D__LINUX_ALSA__" CXXFLAGS="-D__UNIX_JACK__ -D__LINUX_ALSA__" LDFLAGS=-ljack ./configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__make} DESTDIR=%{buildroot} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications pixmaps/din.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG BUGS INSTALL NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/din.desktop
%{_datadir}/icons/hicolor/scalable/apps/din.svg
%{_datadir}/pixmaps/din.png

%changelog
* Mon May 11 2020 Yann Collette <ycollette dot nospam at free.fr> 46.2.0-1
- Initial spec file
