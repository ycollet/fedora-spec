# Global variables for github repository
%global commit0 a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

# git clone https://github.com/brummer10/GxPlugins.lv2.git
# mv GxPlugins.lv2 GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5
# cd GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5
# git submodule init
# git submodule update
# cd ..
# tar cvfz GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5.tar.gz GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5

Name:           lv2-GxBottleRocket-plugin
Version:        0.3.%{shortcommit0}
Release:        1%{?dist}
Summary:        LV2 Analogue simulation of a tube preamp

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/brummer10/GxPlugins.lv2
SOURCE0:        GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5.tar.gz

BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: git

%description
LV2 Analogue simulation of a tube preamp

%package -n lv2-GxGuvnor-plugin
Summary: LV2 Overdrive/distortion pedal simulation from Guitarix
Group:   Applications/Multimedia
%description -n lv2-GxGuvnor-plugin
LV2 Overdrive/distortion pedal simulation from Guitarix

%package -n lv2-GxHotBox-plugin
Summary: Analogue simulation of a tube preamp with overdrive and interactive tone control
Group:   Applications/Multimedia
%description -n lv2-GxHotBox-plugin
Analogue simulation of a tube preamp with overdrive and interactive tone control

%package -n lv2-GxHyperion-plugin
Summary: Simulation of the Hyperion Fuzz Pedal
Group:   Applications/Multimedia
%description -n lv2-GxHyperion-plugin
Simulation of the Hyperion Fuzz Pedal

%package -n lv2-GxQuack-plugin
Summary: Envelope controlled wah pedal with some extra features
Group:   Applications/Multimedia
%description -n lv2-GxQuack-plugin
Envelope controlled wah pedal with some extra features

%package -n lv2-GxSaturator-plugin
Summary: A LV2 saturation plugin
Group:   Applications/Multimedia
%description -n lv2-GxSaturator-plugin
A LV2 saturation plugin

%package -n lv2-GxSD1-plugin
Summary: Super Overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxSD1-plugin
Super Overdrive pedal simulation

%package -n lv2-GxSD2Lead-plugin
Summary: SD2 overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxSD2Lead-plugin
SD2 overdrive pedal simulation

%package -n lv2-GxSlowGear-plugin
Summary: Automatic pedal volume
Group:   Applications/Multimedia
%description -n lv2-GxSlowGear-plugin
Automatic pedal volume

%package -n lv2-GxSuperFuzz-plugin
Summary: Analog simulation of the UniVox (*) SuperFuzz pedal as LV2 plugin.
Group:   Applications/Multimedia
%description -n lv2-GxSuperFuzz-plugin
Analog simulation of the UniVox (*) SuperFuzz pedal as LV2 plugin.

%package -n lv2-GxSuppaToneBender-plugin
Summary: Analog simulation of the Vox (*) Suppa Tone Bender pedal as LV2 plugin.
Group:   Applications/Multimedia
%description -n lv2-GxSuppaToneBender-plugin
Analog simulation of the Vox (*) Suppa Tone Bender pedal as LV2 plugin.

%package -n lv2-GxSVT-plugin
Summary: Tube based Bass preamp simulation 
Group:   Applications/Multimedia
%description -n lv2-GxSVT-plugin
Tube based Bass preamp simulation

%package -n lv2-GxToneMachine-plugin
Summary: Analogous simulation of the Foxx(*) Tone Machine Pedal as LV2 plugin
Group:   Applications/Multimedia
%description -n lv2-GxToneMachine-plugin
Analogous simulation of the Foxx(*) Tone Machine Pedal as LV2 plugin

%package -n lv2-GxUVox720k-plugin
Summary: Analog simulation of the UniVox (*) 720k solid state amp as LV2 plugin.
Group:   Applications/Multimedia
%description -n lv2-GxUVox720k-plugin
Analog simulation of the UniVox (*) 720k solid state amp as LV2 plugin.

%package -n lv2-GxVBassPreAmp-plugin
Summary: Analog Simulation of the 1984 (*) Vox Venue Bass 100 Pre Amp Section.
Group:   Applications/Multimedia
%description -n lv2-GxVBassPreAmp-plugin
Analog Simulation of the 1984 (*) Vox Venue Bass 100 Pre Amp Section.

%package -n lv2-GxVintageFuzzMaster-plugin
Summary: Simulation of the Vintage Fuzz Master Pedal
Group:   Applications/Multimedia
%description -n lv2-GxVintageFuzzMaster-plugin
Simulation of the Vintage Fuzz Master Pedal

%package -n lv2-GxVmk2-plugin
Summary: ??
Group:   Applications/Multimedia
%description -n lv2-GxVmk2-plugin
??

%package -n lv2-GxVoodoFuzz-plugin
Summary: Simulation impressed by the Voodoo Lab (*) SuperFuzz pedal.
Group:   Applications/Multimedia
%description -n lv2-GxVoodoFuzz-plugin
Simulation impressed by the Voodoo Lab (*) SuperFuzz pedal.

%prep
%setup -qn GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5

%build

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 install

%files -n lv2-GxGuvnor-plugin
%{_libdir}/lv2/gx_guvnor.lv2/*

%files -n lv2-GxHotBox-plugin
%{_libdir}/lv2/gx_hotbox.lv2/*

%files -n lv2-GxHyperion-plugin
%{_libdir}/lv2/gx_hyperion.lv2/*

%files -n lv2-GxQuack-plugin
%{_libdir}/lv2/gx_quack.lv2/*

%files -n lv2-GxSaturator-plugin
%{_libdir}/lv2/gx_saturate.lv2/*

%files -n lv2-GxSD1-plugin
%{_libdir}/lv2/gx_sd1sim.lv2/*

%files -n lv2-GxSD2Lead-plugin
%{_libdir}/lv2/gx_sd2lead.lv2/*

%files -n lv2-GxSlowGear-plugin
%{_libdir}/lv2/gx_slowgear.lv2/*

%files -n lv2-GxSuperFuzz-plugin
%{_libdir}/lv2/gx_sfp.lv2/*

%files -n lv2-GxSuppaToneBender-plugin
%{_libdir}/lv2/gx_vstb.lv2/*

%files -n lv2-GxSVT-plugin
%{_libdir}/lv2/gx_ampegsvt.lv2/*

%files -n lv2-GxToneMachine-plugin
%{_libdir}/lv2/gx_tonemachine.lv2/*

%files -n lv2-GxUVox720k-plugin
%{_libdir}/lv2/gx_uvox.lv2/*

%files -n lv2-GxVBassPreAmp-plugin
%{_libdir}/lv2/gx_voxbass.lv2/*

%files -n lv2-GxVintageFuzzMaster-plugin
%{_libdir}/lv2/gx_vfm.lv2/*

%files -n lv2-GxVmk2-plugin
%{_libdir}/lv2/gx_vmk2d.lv2/*

%files -n lv2-GxVoodoFuzz-plugin
%{_libdir}/lv2/gx_voodoo.lv2/*

%files
%{_libdir}/lv2/gx_bottlerocket.lv2/*

%changelog
* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3
- Initial build
