#!/bin/bash

# ./matrixmixer-source.sh <tag>
# ./matrixmixer-source.sh v0.3.0

git clone https://github.com/x42/matrixmixer.lv2
cd matrixmixer.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz matrixmixer.lv2.tar.gz matrixmixer.lv2/*
rm -rf matrixmixer.lv2
