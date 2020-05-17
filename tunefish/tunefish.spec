%global debug_package %{nil}

# Global variables for github repository
%global commit0 a199cb0270b22b9f0361438fd257b66a02d8e8ce
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    tunefish
Version: 4.1.0.%{shortcommit0}
Release: 1%{?dist}
Summary: Tunefish virtual analog synthesizer as a VST plugin

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/paynebc/tunefish

Source0: https://github.com/paynebc/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  tunefish_juce-pixel.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libXinerama-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
Tunefish is a very tiny virtual analog synthesizer.
It is developed to fit into about 10kb of compressed machine code while still producing an audio quality that can compete with commercial synthesizers. 

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1

%build

cd src/tunefish4/Builds/LinuxMakefile
make CONFIG=Release CPPFLAGS="%{build_cxxflags}" %{?_smp_mflags}

%install 

cd src/tunefish4/Builds/LinuxMakefile

%__install -m 755 -d %{buildroot}%{_libdir}/vst/
%__install -m 644 build/*.so %{buildroot}/%{_libdir}/vst/

%files
%{_libdir}/*

%changelog
* Sun May 17 2020 Yann Collette <ycollette.nospam@free.fr> - 4.1.0.a199cb02-1
- Initial spec file
