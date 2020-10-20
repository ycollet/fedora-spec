#!/bin/bash

# ./screcord-source.sh <tag>
# ./screcord-source.sh v0.2

git clone https://github.com/brummer10/screcord.lv2
cd screcord.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz screcord.lv2.tar.gz screcord.lv2/*
rm -rf screcord.lv2
