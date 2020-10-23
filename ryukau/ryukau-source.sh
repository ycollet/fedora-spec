#!/bin/bash

# ./ryukau-source.sh <tag>
# ./ryukau-source.sh master

git clone --recursive https://github.com/ryukau/LV2Plugins/
cd LV2Plugins
find . -name .git -exec rm -rf {} \;
cd ..
mv LV2Plugins ryukau
tar cvfz ryukau.tar.gz ryukau/*
rm -rf ryukau
