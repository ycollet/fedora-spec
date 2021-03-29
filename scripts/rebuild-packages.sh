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
# din
# BespokeSynth
# Carla
# ecasound
# element
# drumgizgmo
# fluxus
# glava
# gigedit
# gxtuner
# hydrogen-drumkits
# infamous-plugins
# kmidimon
# kpp
# mamba
# miniaudicle
# zrythm
# rack-v1-voxglitch 
# veejay-server
# veejay-gui
# rack-v1-TheXOR
# sonic-pi
# surge
# supercollider
# rack-v1-rcm
# sonobus
# snd
# SocaLabs-plugins
# rack-v1-luckyxxl
# rack-v1-MindMeldModular
# rivendell
# rack-v1-JE
# rack-v1-ImpromptuModular
#

# Reorder srpm file in FILELIST: dependencies first

FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-34-x86_64 linuxmao $Files
done

