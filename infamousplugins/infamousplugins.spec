# Global variables for github repository
%global commit0 28b405414a5d044e576ab00b75ceaa1c0a7b8929
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    infamousPlugins
Version: 0.3.0
Release: 1%{?dist}
Summary: Live performance audio session manager using Carla
URL:     https://github.com/ssj71/infamousPlugins.git
Group:   Applications/Multimedia

Source0: https://github.com/ssj71/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

License: GPLv2+

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel
BuildRequires: non-ntk-devel
BuildRequires: non-ntk-fluid
BuildRequires: cairo-devel
BuildRequires: lv2-devel
BuildRequires: zita-resampler-devel
BuildRequires: fftw3-devel

%description
Infamous Plugins is a collection of open-source LV2 plugins. It hopefully helps fill some holes, supplying non-existing plugins for linux audio. There is little interest in creating ANOTHER compressor, or ANOTHER EQ when myriad other excellent lv2 versions of such already exist. At least until I become interested in making one of those things and feel I can do something different...

%package -n lv2-%{name}
Summary: Infamous set of LV2 Plugins
Group:   Applications/Multimedia

%description -n lv2-%{name}
Infamous Plugins is a collection of open-source LV2 plugins. It hopefully helps fill some holes, supplying non-existing plugins for linux audio. There is little interest in creating ANOTHER compressor, or ANOTHER EQ when myriad other excellent lv2 versions of such already exist. At least until I become interested in making one of those things and feel I can do something different...

%prep
%setup -qn %{name}-%{commit0}

%build

%ifarch x86_64
%cmake -DLIBDIR=lib64 .
%else
%cmake .
%endif

%make_build VERBOSE=1

%install

%make_install DESTDIR=%{buildroot}

%files -n lv2-%{name}
%doc README CHANGELOG
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*

%changelog
* Tue Apr 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial version of spec file
