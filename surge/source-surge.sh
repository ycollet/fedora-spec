#!/bin/bash

# Usage: ./source-surge.sh <tag>
#        ./source-surge.sh 1.6.6

git clone https://github.com/surge-synthesizer/surge
cd surge
git checkout origin/release/$1
git submodule init
git submodule update
cd vst3sdk
git submodule init
git submodule update
cd ..
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz surge.tar.gz surge/*
rm -rf surge
