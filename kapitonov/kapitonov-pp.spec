# Global variables for github repository
%global commit0 828dcf7ede9260da6d65ab6896d99d694f7f12af
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    kpp
Version: 1.2.1
Release: 1%{?dist}
Summary: A set of plugins for guitar sound processing
URL:     https://github.com/olegkapitonov/Kapitonov-Plugins-Pack
Group:   Applications/Multimedia
License: GPLv2+

Source0: https://github.com/olegkapitonov/Kapitonov-Plugins-Pack/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ sed
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: ladspa-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: cairo-devel
BuildRequires: zita-resampler-devel
BuildRequires: zita-convolver-devel
BuildRequires: boost-devel
BuildRequires: faust
BuildRequires: faust-osclib-devel
BuildRequires: fftw-devel
BuildRequires: meson

%description
A set of plugins for guitar sound processing

%package -n lv2-kpp-plugins
Summary: A set of plugins for guitar sound processing - LV2 version
License:GPLv2+

%description -n lv2-kpp-plugins
Kapitonov plugins pack.
A set of plugins for guitar sound processing - LV2 version

%package -n ladspa-kpp-plugins
Summary: A set of plugins for guitar sound processing - LADSPA version
License:GPLv2+

%description -n ladspa-kpp-plugins
Kapitonov plugins pack.
A set of plugins for guitar sound processing - LADSPA version

%prep
%setup -qn Kapitonov-Plugins-Pack-%{commit0}

%build

CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" VERBOSE=1 meson --prefix=/usr -Dlv2dir=%{_lib}/lv2 -Dladspadir=%{_lib}/ladspa build
cd build

DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install

cd build
DESTDIR=%{buildroot} ninja install

%files -n ladspa-kpp-plugins
%{_libdir}/ladspa/*

%files -n lv2-kpp-plugins
%{_libdir}/lv2/*

%changelog
* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- update to 1.2.1-1

* Mon Jan 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- initial release
