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
# midimsg
# sfArkLib
# cwiid
# non-ntk
# yaml-cpp03
# faust

# linuxsampler before liblscp
# non-ntk before ensemble-chorus
# veejay-server before veejay-gui

# In Fedora now:
# Carla
# Cadence

# Reorder srpm file in FILELIST: dependencies first
FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-33-x86_64 linuxmao $Files
done

