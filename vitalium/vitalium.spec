%define _lto_cflags %{nil}

%global commit0 65f1fe6c8917de717fe0d30f58b326f1f602ebdd
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    vitalium
Version: 1.0.0
Release: 1%{?dist}
Summary: A LV2 / VST3 / standalone wavetable synth
License: GPLv2+
URL:     https://github.com/mtytel/vital

Source0: https://github.com/mtytel/vital/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: libsecret-devel

%description
Vitalium is a spectral warping wavetable synthesizer.

%prep
%autosetup -n vital-%{commit0}

# Disable VST
sed -i -e "s/vst vst3/vst3/g" Makefile
sed -i -e "s/install_vst install_vst3/install_vst3/g" Makefile
sed -i -e "s/install_effects_vst install_effects_vst3/install_effects_vst3/g" Makefile
# Disable installation of icons
sed -i -e "s/standalone install_icons/standalone/g" Makefile
# Rename executable
find . -name "Makefile*" -exec sed -i -e "s/[vV]ial/vitalium/g" {} \;

unzip %{SOURCE1}

%build

# %set_build_flags
# %make_build CONFIG=Release STRIP=true LIBDIR=%{_libdir} PROGRAM=vitalium LIB_PROGRAM=Vitalium LIB_PROGRAM_FX=VitaliumFX
make DESTDIR=%{buildroot} CONFIG=Release CXXFLAGS=-I`pwd`/VST_SDK/VST2_SDK STRIP=true LIBDIR=%{_libdir} standalone vst3 lv2

%install

%make_install CONFIG=Release STRIP=true LIBDIR=%{_libdir} 

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst3/*

%changelog
* Wed Feb 24 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
