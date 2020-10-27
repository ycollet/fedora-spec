Name:    zplugins
Version: 0.1.7
Release: 1%{?dist}
Summary: A collection of audio DSP LV2 plugins
License: GPLv2+
URL:     https://git.zrythm.org/cgit/zplugins

Source0: https://git.zrythm.org/cgit/zplugins/snapshot/zplugins-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: ztoolkit
BuildRequires: librsvg2-devel
BuildRequires: meson
BuildRequires: libsndfile-devel

%description
A collection of audio DSP LV2 plugins

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export CFLAGS="-fPIC $CFLAGS"

%meson -Dlv2dir=%{_lib}/lv2
%meson_build 

%install 

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Tue Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- Initial build
