#!/bin/bash

spectool -g sonic-pi.spec

#Install osmid (for MIDI support)
OSMID_VERSION=v0.6.8
git clone --recurse https://github.com/llloret/osmid.git
cd osmid
git checkout ${OSMID_VERSION}
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz osmid.tar.gz osmid/*
rm -rf osmid
