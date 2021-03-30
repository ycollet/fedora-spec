#!/bin/bash

# To get the API key required to use copr-cli, go to:
# https://copr.fedorainfracloud.org/api/

# The first packages to be built:
# premake*
# jmatcontrol
# jnoisemeter
# libgig
# linuxsampler
# liblscp
# libaudec
# libcyaml
# libreproc
# libsmf
# libbacktrace-devel
# libcoverart
# lvtk
# redkit
# midimsg
# qscintilla
# sfArkLib
# cwiid
# non-ntk
# yaml-cpp03
# faust
# BatLib
# nanomsg
# ulfius
# ztoolkit

# libgig before linuxsampler before liblscp
# non-ntk before ensemble-chorus
# veejay-server before veejay-gui
# sonic-pi after supercollider

# In Fedora now:
# Carla
# Cadence

################
# Package List #
################

#######################
# End of Package List #
#######################

# HS
# faust
# abNinjam
# ecasound
# element
# fluxus
# glava
# hydrogen-drumkits
# kmidimon
# kpp
# miniaudicle
# rivendell

# Maybe a preprocessor bug related to freetype-config output.
# veejay-server
# veejay-gui
# sonic-pi a problem due to ruby 3.0
# Mamba problem with template and C code ...
# sonobus pb with Juce and the use of deleted function
# SocaLabs-plugins pb with projucer resave project
# BespokeSynth doesn't build anymore ...
# infamous-plugins pb with lv2-1.18.0

# OK - rack-v1-JE
# OK - rack-v1-luckyxxl
# OK - rack-v1-MindMeldModular
# OK - rack-v1-ImpromptuModular
# OK - rack-v1-voxglitch 
# OK - rack-v1-TheXOR
# OK - rack-v1-rcm
# OK - supercollider
# OK - zrythm
# OK - din
# OK - snd
# OK - surge
# OK - gxtuner
# OK - gigedit
# OK - drumgizgmo

# Reorder srpm file in FILELIST: dependencies first

FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-34-x86_64 linuxmao $Files
done

