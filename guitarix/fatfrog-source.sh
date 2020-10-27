#!/bin/bash

# ./fatfrog-source.sh <tag>
# ./fatfrog-source.sh v1.0

git clone https://github.com/brummer10/FatFrog.lv2
cd FatFrog.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz FatFrog.lv2.tar.gz FatFrog.lv2/*
rm -rf FatFrog.lv2
