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

Name:           lv2-GxPlugins-plugins
Version:        0.3.%{shortcommit0}
Release:        1%{?dist}
Summary:        GxPlugins LV2 set of plugins from Guitarix

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
GxPlugins LV2 set of plugins from Guitarix

%prep
%setup -qn GxPlugins.lv2.a4a3477c856416a0b62b060dcf6b8d44c9b2fdd5

%build

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%install 

#%make_install INSTALL_DIR=%{buildroot}%{_libdir}/lv2
make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 install

# GxGuvnor.lv2: Overdrive/distortion pedal simulation
# GxHotBox.lv2: Analogue simulation of a tube preamp with overdrive and interactive tone control
# GxHyperion.lv2: Simulation of the Hyperion Fuzz Pedal
# GxQuack.lv2: envelope controlled wah pedal with some extra features
# GxSaturator.lv2: A LV2 saturation plugin
# GxSD1.lv2: Super Overdrive pedal simulation
# GxSD2Lead.lv2: SD2 overdirve pedal simulation
# GxSlowGear.lv2: Automatic pedal volume
# GxSuperFuzz.lv2: Analog simulation of the UniVox (*) SuperFuzz pedal as LV2 plugin.
#  In this simulation the trim pot, which is usualy in the housing,
#  is exposed as control parameter. It adjust the amount of harmonics
# GxSuppaToneBender.lv2: Analog simulation of the Vox (*) Suppa Tone Bender pedal as LV2 plugin.
# GxSVT.lv2: Tube based Bass preamp simulation 
# GxToneMachine.lv2: Analogous simulation of the Foxx(*) Tone Machine Pedal as LV2 plugin
# GxUVox720k.lv2: Analog simulation of the UniVox (*) 720k solid state amp as LV2 plugin.
# GxVBassPreAmp.lv2: Analog Simulation of the 1984 (*) Vox Venue Bass 100 Pre Amp Section.
# GxVintageFuzzMaster.lv2: Simulation of the Vintage Fuzz Master Pedal
# GxVmk2.lv2: ??
# GxVoodoFuzz.lv2: simulation impressed by the Voodoo Lab (*) SuperFuzz pedal.

%files
%{_libdir}/lv2/*

%changelog
* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3
- Initial build
