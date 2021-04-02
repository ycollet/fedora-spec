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
# veejay-core before veejay-server before veejay-gui
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

# sonic-pi a problem due to ruby 3.0
# SocaLabs-plugins pb with projucer resave project
# BespokeSynth doesn't build anymore ...
# infamous-plugins pb with lv2-1.18.0
# abNinjam pb with template ...
# kpp faust required
# rivendell - pb with null ptr comparison

# Reorder srpm file in FILELIST: dependencies first

FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-34-x86_64 linuxmao $Files
done

