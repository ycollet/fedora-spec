Name:    sonobus
Version: 1.4.1
Release: 3%{?dist}
Summary: A peer to peer audio application
License: GPLv2+
URL:     https://github.com/essej/sonobus

Source0: https://github.com/essej/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: opus-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel

%description
SonoBus is an easy to use application for streaming high-quality,
low-latency peer-to-peer audio between devices over the internet or a local network.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

sed -i -e "s/-march=native//g" Builds/LinuxMakefile/Makefile

%set_build_flags

export HOME=`pwd`
mkdir -p .vst3

cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true VST3 Standalone

%install 

install -m 755 -d %{buildroot}/%{_libdir}/vst3/sonobus.vst3/
install -m 755 -d %{buildroot}/%{_bindir}/

install -m 755 -p Builds/LinuxMakefile/build/sonobus %{buildroot}/%{_bindir}/
cp -ra Builds/LinuxMakefile/build/sonobus.vst3/* %{buildroot}/%{_libdir}/vst3/sonobus.vst3/
chmod a+x %{buildroot}/%{_libdir}/vst3/sonobus.vst3/Contents/x86_64-linux/sonobus.so

mkdir -p %{buildroot}/%{_datadir}/applications
cp  Builds/LinuxMakefile/sonobus.desktop %{buildroot}/%{_datadir}/applications/sonobus.desktop
chmod +x %{buildroot}/%{_datadir}/applications/sonobus.desktop

mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp  images/sonobus_logo@2x.png %{buildroot}/%{_datadir}/pixmaps/sonobus.png

cp deps/aoo/LICENSE LICENSE-aoo
cp deps/ff_meters/LICENSE.md LICENSE-ff_meters.md
cp deps/juce/LICENSE.md LICENSE-juce.md

%files
%doc README.md
%license LICENSE LICENSE-aoo LICENSE-ff_meters.md LICENSE-juce.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Mar 23 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-3
- update to 1.4.1-3

* Tue Mar 23 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-3
- update to 1.4.0-3

* Fri Mar 12 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.2-2
- Fix invalid binaries

* Sun Feb 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.2-1
- Initial spec file
