#!/bin/bash

# Reorder srpm file in FILELIST: dependencies first
FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-31-x86_64 linuxmao $Files
done

