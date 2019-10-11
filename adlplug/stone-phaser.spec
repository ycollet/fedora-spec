%global debug_package %{nil}

# Global variables for github repository
%global commit0 8ae2fc7544259525027ee4496e7fa0c7527f71e7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    stone-phaser
Version: 0.1.2
Release: 1%{?dist}
Summary: A classic analog phaser effect
URL:     https://github.com/jpcima/stone-phaser
Group:   Applications/Multimedia

License: BSL-1.0

# git clone https://github.com/jpcima/stone-phaser
# git checkout v0.1.2
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz stone-phaser.tar.gz stone-phaser/*
# rm -rf stone-phaser

Source0: stone-phaser.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel libXft-devel
BuildRequires: fltk-devel fltk-fluid
BuildRequires: cairo-devel libpng-devel

%description
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone. It has a color switch, which makes the phasing stronger when on, and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.

%package -n ladspa-stone-phaser
Summary:        stone-phaser LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-stone-phaser
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone. It has a color switch, which makes the phasing stronger when on, and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.
stone-phaser LADSPA plugin

%package -n vst-stone-phaser
Summary:        stone-phaser VST plugin
Group:          Applications/Multimedia

%description -n vst-stone-phaser
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone. It has a color switch, which makes the phasing stronger when on, and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.
stone-phaser VST plugin

%package -n lv2-stone-phaser
Summary:        stone-phaser LV2 plugin
Group:          Applications/Multimedia

%description -n lv2-stone-phaser
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone. It has a color switch, which makes the phasing stronger when on, and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.
stone-phaser LV2 plugin

%prep

%setup -qn stone-phaser

%build

make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_libdir} %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_libdir} install

%files
%doc LICENSE README.md
%files -n lv2-stone-phaser
%{_libdir}/lv2/*
%files -n vst-stone-phaser
%{_libdir}/vst/*
%files -n ladspa-stone-phaser
%{_libdir}/ladspa/*

%changelog
* Fri Oct 11 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
