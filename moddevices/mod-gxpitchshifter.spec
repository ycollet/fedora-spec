Name:    mod-gxpitchshifter
Version: 1.0.0
Release: 1%{?dist}
Summary: Guitarix compatible mod-pitchshifter LV2 set of plugins from portalmod
License: GPLv2+
URL:     https://github.com/ycollet/mod-pitchshifter

Source0: https://github.com/ycollet/mod-pitchshifter/archive/v1.0.0.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: fftw
BuildRequires: python3
BuildRequires: python3-mpmath
BuildRequires: armadillo-devel
BuildRequires: SuperLU-devel

%description
Guitarix compatible mod-pitchshifter LV2 set of plugins from portalmod

%prep
%autosetup -n mod-pitchshifter-%{version}

sed -i -e "s/-Wl,--strip-all//" Makefile.mk

%build

%set_build_flags

%make_build INSTALL_PATH=%{_libdir}/lv2

%install

%make_install INSTALL_PATH=%{_libdir}/lv2

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Thu Nov 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
