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

# linuxsampler before liblscp
# non-ntk before ensemble-chorus

# In Fedora now:
# Carla
# Cadence

# Reorder srpm file in FILELIST: dependencies first
FILELIST="cwiid-0.6.00-36.20100505gitfadf11e.fc31.src.rpm
yaml-cpp03-0.3.0-14.fc31.src.rpm
premake3-3.7-2.fc31.src.rpm
premake4-4.4beta5-1.fc31.src.rpm
premake5-5.0.0alpha13-1.fc31.src.rpm
jmatconvol-0.3.3-1.fc31.src.rpm
jnoisemeter-0.2.2-1.fc31.src.rpm
non-ntk-1.3.1000-0.2.20190925gitdae1771.fc31.src.rpm
JUCE-5.4.6.1e71c07-3.fc31.src.rpm
libaudec-devel-0.2-1.fc31.src.rpm
libcyaml-1.0.1-1.fc31.src.rpm
libgig-4.1.0-1.fc31.src.rpm
liblscp-0.5.8-1.fc31.src.rpm
lv2lint-0.2.0-2.fc31.src.rpm
lvtk-2.0.0.6bfe981-1.fc31.src.rpm
faust-2.14.4-18.fc31.src.rpm
midimsg-lv2-0.0.5.46beb48-1.fc31.src.rpm
planetccrma-rt-permissions-2012.09.19-1.fc31.src.rpm
Rack-v1-1.1.6-8.fc31.src.rpm
redkite-0.6.3-1.fc31.src.rpm
sfArkLib-2.24.e558feb-1.fc31.src.rpm
supercollider-3.10.4-2.fc31.src.rpm
zita-ajbridge-0.7.0-1.fc31.src.rpm
zita-bls1-0.3.3-1.fc31.src.rpm
zita-dpl1-0.3.3-1.fc31.src.rpm
zita-lrx-0.1.0-1.fc31.src.rpm
zita-mu1-0.2.2-1.fc31.src.rpm
zita-njbridge-0.4.2-1.fc31.src.rpm
supercollider-sc3-plugins-3.7.1-2.296.g42a1bc6.fc31.src.rpm"

for Files in $FILELIST
do
    copr-cli build --chroot fedora-32-x86_64 linuxmao $Files
done

