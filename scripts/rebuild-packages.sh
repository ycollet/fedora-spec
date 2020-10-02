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

# premake3-3.7-2.fc32.src.rpm
# premake4-4.4beta5-1.fc32.src.rpm
# premake5-5.0.0alpha15-1.fc32.src.rpm
# jmatconvol-0.3.3-1.fc32.src.rpm
# jnoisemeter-0.2.2-1.fc32.src.rpm
# libgig-4.1.0-1.fc32.src.rpm
# linuxsampler-2.1.0-1.fc32.src.rpm
# liblscp-0.5.8-1.fc32.src.rpm
# libsmf-1.3.692e728-3.fc32.src.rpm
# libaudec-devel-0.2.3-1.fc32.src.rpm
# libcoverart-1.0.0-1.fc32.src.rpm
# libcyaml-1.1.0-1.fc32.src.rpm
# lvtk-2.0.0.6bfe981-2.fc32.src.rpm
# redkite-1.0.3-2.fc32.src.rpm
# midimsg-lv2-0.0.5.46beb48-1.fc32.src.rpm
# sfArkLib-2.24.e558feb-1.fc32.src.rpm
# cwiid-0.6.00-36.20100505gitfadf11e.fc32.src.rpm
# non-ntk-1.3.1000-0.3.20190925gitdae1771.fc32.src.rpm
# yaml-cpp03-0.3.0-14.fc32.src.rpm
# faust-2.27.2-22.fc32.src.rpm
# lv2lint-0.2.0-4.fc32.src.rpm
# nanomsg-1.1.5-3.fc32.src.rpm
# veejay-server-1.5.57-2.fc32.src.rpm
# veejay-gui-1.5.57-2.fc32.src.rpm
# qscintilla-2.11.2-10.fc32.src.rpm
# JUCE

# In Fedora now:
# Carla
# Cadence

# Reorder srpm file in FILELIST: dependencies first
FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-33-x86_64 linuxmao $Files
done

