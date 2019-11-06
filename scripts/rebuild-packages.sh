#!/bin/bash

# The first packages to be built:
# premake*
# jmatcontrol
# jnoisemeter
# libgig
# linuxsampler
# liblscp
# lvtk
# redkit
# nanomsg
# yaml-cpp03
# midimsg
# sfArkLib
# cwiid
# non-ntk

# linuxsampler before liblscp
# non-ntk before ensemble-chorus

# In Fedora now:
# Carla
# Cadence

# FAILED:
#
# sonic-pi-3.1.0/app/server/ruby/vendor/rugged-0.26.0/lib/rugged.rb:14:in `require_relative': cannot load such file
#Creating ../../server/ruby/bin/../rb-native/2.6.0
#Compiling native extension in /builddir/build/BUILD/sonic-pi-3.1.0/app/server/ruby/vendor/rugged-0.28.0/ext/rugged
#*** extconf.rb failed ***
#Could not create Makefile due to some reason, probably lack of necessary
#libraries and/or headers.  Check the mkmf.log file for more details.  You may
#need configuration options.

# Reorder srpm file in FILELIST: dependencies first
FILELIST="linuxsampler-2.1.0-1.fc30.src.rpm
	liblscp-0.5.8-1.fc30.src.rpm
	lvtk-2.0.0.6bfe981-1.fc30.src.rpm
	planetccrma-rt-permissions-2012.09.19-1.fc30.src.rpm
	redkite-0.6.2-1.fc30.src.rpm
	sfArkLib-2.24.e558feb-1.fc30.src.rpm
	nanomsg-1.1.2-1.fc30.src.rpm
	yaml-cpp03-0.3.0-14.fc30.src.rpm
	midimsg-lv2-0.0.4.9920257-1.fc30.src.rpm
	supercollider-3.10.3-2.fc30.src.rpm
	supercollider-sc3-plugins-3.7.1-2.296.g42a1bc6.fc30.src.rpm
	6PM-0.9-1.fc30.src.rpm
	adlplug-1.0.1-3.fc30.src.rpm
	aeolus-0.9.7-1.fc30.src.rpm
	aliki-0.3.0-1.fc30.src.rpm
	ams-lv2-1.2.1.0f60ee0-1.fc30.src.rpm
	amsynth-1.9.0.71544e4-1.fc30.src.rpm
	amuc-1.7.355f024-2.fc30.src.rpm
	azr3-jack-1.2.3-1.fc30.src.rpm
	BatLib-0.1-1.fc30.src.rpm
	beatslash-lv2-1.0.5.45044ce-1.fc30.src.rpm
	brutefir-1.0k-1.fc30.src.rpm
	caps-lv2-0.9.26.250844a-1.fc30.src.rpm
	chuck-1.4.0.0-1.fc30.src.rpm
	common-music-3.10.2-2.fc30.src.rpm
	deteriorate-lv2-1.0.6.3104774-1.fc30.src.rpm
	dgedit-0.1-2.fc30.src.rpm
	DISTRHO-Ports-1.0.0.a82fff0-3.fc30.src.rpm
	dragonfly-reverb-2.0.0-1.fc30.src.rpm
	drc-3.2.3-1.fc30.src.rpm
	drumgizmo-0.9.18.1-1.fc30.src.rpm
	enscribe-0.1.0-1.fc30.src.rpm
	ensemble-chorus-0.0.1-1.fc30.src.rpm
	eteroj.lv2-0.4.0-2.fc30.src.rpm
	fasttracker2-0.1b166-1.fc30.src.rpm
	FoxDot-0.8.3-1.fc30.src.rpm
	FoxDotQuark-0.1-1.fc30.src.rpm
	geonkick-1.9.0-1.fc30.src.rpm
	gigedit-1.1.0-2.fc30.src.rpm
	goatracker-2.75-1.fc30.src.rpm
	GrandOrgue-0.3.1.2294-2.fc30.src.rpm
	GxPlugins-0.7.2625ee0-1.fc30.src.rpm
	gxtuner-3.0.792d453-2.fc30.src.rpm
	harvid-0.8.3.d71921b-1.fc30.src.rpm
	helm-1.0.0.abdedd5-3.fc30.src.rpm
	horgand-1.15.0-1.fc30.src.rpm
	hydrogen-0.9.7-11.fc30.src.rpm
	IanniX-0.9.20.1294f84-2.fc30.src.rpm
	infamousPlugins-0.3.0-1.fc30.src.rpm
	jack_delay-0.4.2-1.fc30.src.rpm
	jack_utils-0.0.1-1.fc30.src.rpm
	jalv_select-1.3.0.c8f5320-2.fc30.src.rpm
	jm2cv-0.1-1.fc30.src.rpm
	klystrack-1.7.6-1.fc30.src.rpm
	lebiniou-3.31-1.fc30.src.rpm
	lebiniou-data-3.28-1.fc30.src.rpm
	lenmus-5.4.2.0e5819a-1.fc30.src.rpm
	libprojectM-2.1.0-10.fc30.src.rpm
	lmms-mao-1.1.3-8.fc30.src.rpm
	loudness-scanner-0.5.1-1.fc30.src.rpm
	lsp-plugins-1.1.10-1.fc30.src.rpm
	lv2-avldrums-x42-plugin-0.4.0.4900e7f-1.fc30.src.rpm
	lv2-BShapr-0.4.0-1.fc30.src.rpm
	lv2-BSlizr-1.2.0-1.fc30.src.rpm
	lv2-fil-plugins-2.0-13.fc30.src.rpm
	lv2-screcord-plugin-0.1.36fbff9-2.fc30.src.rpm
	mda-lv2-0.9.3d6dd09-2.fc30.src.rpm
	midi_matrix.lv2-0.20.0-2.fc30.src.rpm
	midizap-1.0.0.dc62671-1.fc30.src.rpm
	miniaudicle-1.3.5.2-1.fc30.src.rpm
	mod-pitchshifter-0.9.d404edc-1.fc30.src.rpm
	mv-6pm-0.5.0-1.fc30.src.rpm
	mx44-0.44.2-1.fc30.src.rpm
	ninjam-client-0.0.1-1.fc30.src.rpm
	ninjam-server-0.0.1-1.fc30.src.rpm
	noise-repellent-lv2-0.1.4.3f704d7-2.fc30.src.rpm
	noise-suppression-for-voice-0.2.0-2.fc30.src.rpm
	opl3bankeditor-1.5.0-1.fc30.src.rpm
	orbit.lv2-0.1.0-2.fc30.src.rpm
	osc2midi-1.0.0.5f37886-1.fc30.src.rpm
	oxefmsynth-1.3.5.fe078ea-1.fc30.src.rpm
	patchmatrix-0.12.0-2.fc30.src.rpm
	performer-1.0.2-1.fc30.src.rpm
	plebtracker-0.1-1.fc30.src.rpm
	plujain-ramp-1.1.3-1.fc30.src.rpm
	polyphone-2.1.3-1.fc30.src.rpm
	postfish-19646.svn-2.fc30.src.rpm
	projectM-extra-presets-1.0.0-1.fc30.src.rpm
	protracker-2.3r191-2.fc30.src.rpm
	protrekkr-1.0.0-1.fc30.src.rpm
	psi-plugins-doc-0.0.1-2.fc30.src.rpm
	puredata-0.50.0-1.fc30.src.rpm
	qsampler-0.4.2-1.fc30.src.rpm
	qutecsound-0.9.6b-1.fc30.src.rpm
	r128gain-0.9.3-1.fc30.src.rpm
	Rack-0.6.2c-6.fc30.src.rpm
	rack-21kHz-0.6.1-2.fc30.src.rpm
	rack-8Mode-0.6.1-2.fc30.src.rpm
	rack-Aaron-MicroTools-0.6.0-2.fc30.src.rpm
	rack-Alikin-0.6.2-2.fc30.src.rpm
	rack-AmalgamatedHarmonics-0.6.3-2.fc30.src.rpm
	rack-aP-Modules-0.6.0-2.fc30.src.rpm
	rack-ArableInstruments-0.6.0-2.fc30.src.rpm
	rack-arjo_modules-0.6.0-2.fc30.src.rpm
	rack-AS-0.6.12-2.fc30.src.rpm
	rack-AudibleInstruments-0.6.0-2.fc30.src.rpm
	rack-BaconPlugs-0.6.2-2.fc30.src.rpm
	rack-Bark-0.6.3-2.fc30.src.rpm
	rack-BeckstromResearch-0.6.0-2.fc30.src.rpm
	rack-Befaco-0.6.0-2.fc30.src.rpm
	rack-Bidoo-0.6.22-2.fc30.src.rpm
	rack-Bogaudio-0.6.10-2.fc30.src.rpm
	rack-BOKONTEPByteBeatMachine-0.6.1-2.fc30.src.rpm
	rack-Bridge-0.6.0-2.fc30.src.rpm
	rack-CatroModulo-0.6.4-2.fc30.src.rpm
	rack-cf-0.6.8-2.fc30.src.rpm
	rack-CharredDesert-0.6.4-2.fc30.src.rpm
	rack-Circlefade-0.6.2-2.fc30.src.rpm
	rack-ComputerScare-0.6.4-2.fc30.src.rpm
	rack-com-soundchasing-stochasm-0.6.1-2.fc30.src.rpm
	rack-CountModula-0.6.0-2.fc30.src.rpm
	rack-dBiz-0.6.1-2.fc30.src.rpm
	rack-DHE-0.6.3-2.fc30.src.rpm
	rack-DrumKit-0.6.4-2.fc30.src.rpm
	rack-Edge-0.6.3-2.fc30.src.rpm
	rack-EH_modules-0.6.1-2.fc30.src.rpm
	rack-Erratic-0.6.2-2.fc30.src.rpm
	rack-ESeries-0.6.0-2.fc30.src.rpm
	rack-ExpertSleepers-Encoders-0.6.0-2.fc30.src.rpm
	rack-FrankBussFormula-0.6.2-2.fc30.src.rpm
	rack-Fundamental-0.6.1-2.fc30.src.rpm
	rack-Geodesics-0.6.4-2.fc30.src.rpm
	rack-Gratrix-0.6.0-2.fc30.src.rpm
	rack-HetrickCV-0.6.0-2.fc30.src.rpm
	rack-HolonicSystems-Free-0.6.1-2.fc30.src.rpm
	rack-huaba-0.6.3-2.fc30.src.rpm
	rack-ImpromptuModular-0.6.10-2.fc30.src.rpm
	rack-IO-Simple-0.6.0-2.fc30.src.rpm
	rack-JW-Modules-0.6.3-2.fc30.src.rpm
	rack-KarateSnoopy-0.6.1-2.fc30.src.rpm
	rack-Koralfx-Modules-0.6.9-2.fc30.src.rpm
	rack-LabSeven-0.6.1-2.fc30.src.rpm
	rack-LFSR-0.6.21-2.fc30.src.rpm
	rack-LOGinstruments-0.6.0-2.fc30.src.rpm
	rack-LRTRack-0.6.4-2.fc30.src.rpm
	rack-luckyxxl-0.6.1-2.fc30.src.rpm
	rack-mental-0.6.3-2.fc30.src.rpm
	rack-MicMusic-0.6.0-2.fc30.src.rpm
	rack-ML_modules-0.6.3-2.fc30.src.rpm
	rack-moDllz-0.6.6-2.fc30.src.rpm
	rack-modular80-0.6.3-2.fc30.src.rpm
	rack-ModularFungi-0.6.2-2.fc30.src.rpm
	rack-MrLumps-0.6.0-2.fc30.src.rpm
	rack-mtsch-plugins-0.6.0-2.fc30.src.rpm
	rack-NauModular-0.6.1-2.fc30.src.rpm
	rack-NocturnalEncoder-0.6.1-2.fc30.src.rpm
	rack-Nohmad-0.6.0-2.fc30.src.rpm
	rack-NonLinearInstruments-0.6.0-2.fc30.src.rpm
	rack-noobhour-0.6.2-2.fc30.src.rpm
	rack-Ohmer-0.6.4-2.fc30.src.rpm
	rack-PG-Instruments-0.6.4-2.fc30.src.rpm
	rack-PulsumQuadratum-SDR-0.6.1-2.fc30.src.rpm
	rack-PvC-0.6.0-2.fc30.src.rpm
	rack-Quadraphonics-0.6.3-2.fc30.src.rpm
	rack-QuantalAudio-0.6.2-2.fc30.src.rpm
	rack-Qwelk-0.6.0-2.fc30.src.rpm
	rack-rcm-0.6.9-2.fc30.src.rpm
	rack-RJModules-0.6.1-2.fc30.src.rpm
	rack-RODENTMODULES-0.6.1-2.fc30.src.rpm
	rack-sb-StochKit-0.6.2-2.fc30.src.rpm
	rack-Sculpt-O-Sound-0.6.0-2.fc30.src.rpm
	rack-SerialTracker-0.6.1-2.fc30.src.rpm
	rack-SkJack-0.6.6-2.fc30.src.rpm
	rack-Skylights-0.6.2-2.fc30.src.rpm
	rack-s-ol-0.6.1-2.fc30.src.rpm
	rack-SonusModular-0.6.2-2.fc30.src.rpm
	rack-Southpole-0.6.0-2.fc30.src.rpm
	rack-Southpole-parasites-0.6.0-2.fc30.src.rpm
	rack-squinkyVCV-0.6.5b-2.fc30.src.rpm
	rack-Starling_Via-0.6.0-2.fc30.src.rpm
	rack-STS-0.6.0.2-2.fc30.src.rpm
	rack-SubmarineFree-0.6.8-2.fc30.src.rpm
	rack-SubmarinePrototype-0.6.1-2.fc30.src.rpm
	rack-SubmarineUtility-0.6.2-2.fc30.src.rpm
	rack-SynthKit-0.6.2-2.fc30.src.rpm
	rack-TheXOR-0.6.2-2.fc30.src.rpm
	rack-tnorris-BostonBrightonModules-0.6.0-2.fc30.src.rpm
	rack-TorpedoDemo-0.6.1-2.fc30.src.rpm
	rack-TriggerFish-Elements-0.6.4-2.fc30.src.rpm
	rack-TrowaSoft-0.6.4-2.fc30.src.rpm
	rack-UnforgettableLuncheon-0.6.2-2.fc30.src.rpm
	rack-unless_modules-0.6.2-2.fc30.src.rpm
	rack-Valley-0.6.14-2.fc30.src.rpm
	rack-VCV-Rack-Plugins-0.6.3-2.fc30.src.rpm
	rack-WhatTheRack-0.6.2-2.fc30.src.rpm
	rack-ZZC-0.6.4-2.fc30.src.rpm	
	raffosynth-0.1.0-1.fc30.src.rpm
	rakarrack-0.6.2-2.fc30.src.rpm	
	RaySession-0.8.1-1.fc30.src.rpm
	rkrlv2-0.0.1.d8c17d3-2.fc30.src.rpm
	scarlett-mixer-0.1.0-1.fc30.src.rpm
	schismtracker-20190805-1.fc30.src.rpm
	sfarkxtc-0.1.cf9f324-1.fc30.src.rpm	
	sherlock.lv2-0.16.0-2.fc30.src.rpm
	sonic-pi-3.1.0-3.fc30.src.rpm
	spectmorph-0.5.0-1.fc30.src.rpm
	stone-phaser-0.1.2-1.fc30.src.rpm
	stretchplayer-0.0.1.5e807a8-1.fc30.src.rpm
	swh-lv2-0.9.810b427-1.fc30.src.rpm
	synthpod-0.1.0-2.fc30.src.rpm
	tap-lv2-0.9.cab6e0d-2.fc30.src.rpm
	tetraproc-0.8.2-1.fc30.src.rpm
	timemachine-0.3.4-2.fc30.src.rpm
	traverso-0.49.6-1.fc30.src.rpm
	vopa-lv2-1.0.0-1.fc30.src.rpm
	wolf-shaper-0.1.7-1.fc30.src.rpm
	xjadeo-0.8.9-1.fc30.src.rpm
	yass-0.1.0-1.fc30.src.rpm
	zam-plugins-3.11-2.fc30.src.rpm
	zita-ajbridge-0.7.0-1.fc30.src.rpm
	zita-bls1-0.3.3-1.fc30.src.rpm
	zita-dpl1-0.3.3-1.fc30.src.rpm
	zita-lrx-0.1.0-1.fc30.src.rpm
	zita-mu1-0.2.2-1.fc30.src.rpm
	zita-njbridge-0.4.2-1.fc30.src.rpm
	zytrax-0.9.0.97b79d1-1.fc30.src.rpm
	ebumeter-0.4.0-1.fc30.src.rpm
	glava-1.5.8.426f70f-1.fc30.src.rpm
	hydrogen-drumkits-0.9.6-2.fc30.src.rpm
	milkytracker-1.02.00-1.fc30.src.rpm
	non-daw-1.2.0-9.gitc15bfa85.fc29.src.rpm"

for Files in $FILELIST
do
    copr-cli build --chroot fedora-31-x86_64 linuxmao $Files
done

