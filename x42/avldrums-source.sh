#!/bin/bash

# ./avldrums-source.sh <tag>
# ./avldrums-source.sh v0.4.1

git clone https://github.com/x42/avldrums.lv2
cd avldrums.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz avldrums.lv2.tar.gz avldrums.lv2/*
rm -rf avldrums.lv2
