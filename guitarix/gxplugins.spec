# Global variables for github repository
%global commit0 63f19485984c002caddec734a9ee94faad2acb55
%global gittag0 v0.6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

# git clone https://github.com/brummer10/GxPlugins.lv2.git
# mv GxPlugins.lv2 GxPlugins.lv2.63f19485984c002caddec734a9ee94faad2acb55
# cd GxPlugins.lv2.63f19485984c002caddec734a9ee94faad2acb55
# git checkout 63f19485984c002caddec734a9ee94faad2acb55
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz GxPlugins.lv2.63f19485984c002caddec734a9ee94faad2acb55.tar.gz GxPlugins.lv2.63f19485984c002caddec734a9ee94faad2acb55

Name:    GxPlugins
Version: 0.6.%{shortcommit0}
Release: 1%{?dist}
Summary: LV2 Analogue simulation of a tube preamp

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/brummer10/GxPlugins.lv2
SOURCE0: GxPlugins.lv2.%{commit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
Guitarix LV2 plugins

%package -n lv2-GxBottleRocket-plugin
Summary: LV2 Analogue simulation of a tube preamp
Group:   Applications/Multimedia
%description -n lv2-GxBottleRocket-plugin
LV2 Analogue simulation of a tube preamp.

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

%package -n lv2-AxisFace-plugin
Summary: Simulation of the Axis Face Silicon Pedal
Group:    Applications/Multimedia
%description -n lv2-AxisFace-plugin
Simulation of the Axis Face Silicon Pedal

%package -n lv2-DOP250-plugin
Summary: Overdrive Preamp Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-DOP250-plugin
Overdrive Preamp Pedal simulation

%package -n lv2-Heathkit-plugin
Summary: Distortion Booster Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-Heathkit-plugin
Distortion Booster Pedal simulation

%package -n lv2-KnightFuzz-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-KnightFuzz-plugin
This is a really nasty Fuzz Pedal,
which act at lower/ moderate settings as a ultra dark fuzz,
when settings get cranked up, it becomes more and more high harmonics.

%package -n lv2-liquiddrive-plugin
Summary: Liquid Drive provides a tonal response with a warm mild to aggressive overdrive, which can do anything from Blues to Hard Rock
Group:   Applications/Multimedia
%description -n lv2-liquiddrive-plugin
Liquid Drive provides a tonal response with a warm mild to aggressive overdrive, which can do anything from Blues to Hard Rock

%package -n lv2-maestro_fz1b-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-maestro_fz1b-plugin
Vintage Fuzz Pedal simulation

%package -n lv2-maestro_fz1s-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-maestro_fz1s-plugin
Vintage Fuzz Pedal simulation

%package -n lv2-MicroAmp-plugin
Summary: The MicroAmp is designed to be a transparent clean volume booster.
Group:   Applications/Multimedia
%description -n lv2-MicroAmp-plugin
The MicroAmp is designed to be a transparent clean volume booster.

%package -n lv2-quack-plugin
Summary: Envelope controlled wah pedal with some extra features
Group:   Applications/Multimedia
%description -n lv2-quack-plugin
Envelope controlled wah pedal with some extra features

%package -n lv2-SunFace-plugin
Summary: A classic fuzz face with some light modifications
Group:   Applications/Multimedia
%description -n lv2-SunFace-plugin
A classic fuzz face with some light modifications

%package -n lv2-TubeDistortion-plugin
Summary: Simulation of a Tube based Distortion Pedal.
Group:   Applications/Multimedia
%description -n lv2-TubeDistortion-plugin
Simulation of a Tube based Distortion Pedal.

%package -n lv2-GxBoobTube-plugin
Summary: The BoobTube is a little tube boost pedal simulation.
Group:   Applications/Multimedia
%description -n lv2-GxBoobTube-plugin
The BoobTube is a little tube boost pedal simulation, it's a variation of the ValveCaster. It adds some overdrive and tube compression along with boosting the signal.

%package -n lv2-GxCreamMachine-plugin
Summary: Simulation, based on a tube power amp circuit.
Group:   Applications/Multimedia
%description -n lv2-GxCreamMachine-plugin
Simulation, based on a tube power amp circuit.

%package -n lv2-GxValveCaster-plugin
Summary: The ValveCaster is a little tube boost pedal simulation.
Group:   Applications/Multimedia
%description -n lv2-GxValveCaster-plugin
The ValveCaster is a little tube boost pedal simulation. It adds some overdrive and tube compression along with boosting the signal.

%prep
%setup -qn GxPlugins.lv2.%{commit0}

%build

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 install

%files -n lv2-AxisFace-plugin
%{_libdir}/lv2/gx_AxisFace.lv2/*

%files -n lv2-DOP250-plugin
%{_libdir}/lv2/gx_DOP250.lv2/*

%files -n lv2-Heathkit-plugin
%{_libdir}/lv2/gx_Heathkit.lv2/*

%files -n lv2-KnightFuzz-plugin
%{_libdir}/lv2/gx_KnightFuzz.lv2/*

%files -n lv2-liquiddrive-plugin
%{_libdir}/lv2/gx_liquiddrive.lv2/*

%files -n lv2-maestro_fz1b-plugin
%{_libdir}/lv2/gx_maestro_fz1b.lv2/*

%files -n lv2-maestro_fz1s-plugin
%{_libdir}/lv2/gx_maestro_fz1s.lv2/*

%files -n lv2-MicroAmp-plugin
%{_libdir}/lv2/gx_MicroAmp.lv2/*

%files -n lv2-quack-plugin
%{_libdir}/lv2/gx_quack.lv2/*

%files -n lv2-SunFace-plugin
%{_libdir}/lv2/gx_SunFace.lv2/*

%files -n lv2-TubeDistortion-plugin
%{_libdir}/lv2/gx_TubeDistortion.lv2/*

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

%files -n lv2-GxBoobTube-plugin
%{_libdir}/lv2/gx_boobtube.lv2/*

%files -n lv2-GxCreamMachine-plugin
%{_libdir}/lv2/gx_CreamMachine.lv2/*

%files -n lv2-GxValveCaster-plugin
%{_libdir}/lv2/gx_valvecaster.lv2/*

%files -n lv2-GxBottleRocket-plugin
%{_libdir}/lv2/gx_bottlerocket.lv2/*

%changelog
* Tue Jan 22 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6
- Update to v0.6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4
- update for Fedora 29

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4

* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3
- Initial build
