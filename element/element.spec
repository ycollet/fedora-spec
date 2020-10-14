Name:    element
Version: 0.44.0
Release: 1%{?dist}
Summary: This is the community version of Element, a modular AU/LV2/VST/VST3 audio plugin host.
URL:     https://github.com/kushview/Element
License: GPL3

# ./element-source.sh 0.44.0

Source0: Element.tar.gz
Source1: GitVersion.h
Source2: element-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: lua-devel
BuildRequires: boost-devel
BuildRequires: ladspa-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: libcurl-devel
BuildRequires: gtk2-devel
BuildRequires: readline-devel
BuildRequires: python3

%description
This is the community version of Element, a modular AU/LV2/VST/VST3 audio plugin host.
Create powerful effects, racks and instruments by connecting nodes to one another.
Integrates with your existing hardware via standard protocols such as MIDI.

%prep

%autosetup -n Element

mkdir -p build/include/
cp %{SOURCE1} build/include/

sed -i -e "s|/usr/bin/env python|/usr/bin/env python3|g" waf

%build

./waf configure --debug --prefix=%{_prefix} --libdir=%{_libdir} 
./waf %{?__smp_mflags}

%install

./waf install --destdir=%{buildroot}

sed -i -e "s/;Sound//g" %{buildroot}%{_datadir}/applications/net.kushview.element.desktop

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/net.kushview.element.desktop

%files
%doc README.md AUTHORS.md CODE_OF_CONDUCT.md  CONTRIBUTING.md 
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/*
%{_datadir}/element/*

%changelog
* Wed Oct 14 2020 Yann Collette <ycollette.nospam@free.fr> - 0.44.0-1
- Initial spec file
