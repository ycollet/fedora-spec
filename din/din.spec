Summary: DIN is a synth of a 3rd kind
Name:    din
Version: 50.0.0
Release: 1%{?dist}
License: GPL
URL:     https://dinisnoise.org/

Source0: https://archive.org/download/dinisnoise_source_code/din-50.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
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
%autosetup -n %{name}-50

# __line conflict with std c++ headers
sed -i -e "s/__line/__dinline/g" src/line.h

%build
%set_build_flags

# To select an api:
# __UNIX_JACK__
# __LINUX_ALSA__

CFLAGS="-D__UNIX_JACK__ $CFLAGS" CXXFLAGS="-D__UNIX_JACK__ $CXXFLAGS" LDFLAGS="-ljack $LDFLAGS" ./configure --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

%install
%make_install

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  pixmaps/din.desktop

%files
%doc AUTHORS CHANGELOG BUGS INSTALL NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/din.desktop
%{_datadir}/icons/hicolor/scalable/apps/din.svg
%{_datadir}/pixmaps/din.png

%changelog
* Sun Mar 14 2021 Yann Collette <ycollette dot nospam at free.fr> 50.0.0-1
- update to 50.0.0

* Sat Jan 2 2021 Yann Collette <ycollette dot nospam at free.fr> 49.1.0-1
- update to 49.1.0

* Fri Oct 23 2020 Yann Collette <ycollette dot nospam at free.fr> 48.0.0-1
- update to 48.0.0 and fix debug build

* Mon May 11 2020 Yann Collette <ycollette dot nospam at free.fr> 46.2.0-1
- Initial spec file
