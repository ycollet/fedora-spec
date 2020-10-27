#!/bin/bash

# ./xpolymonk-source.sh <tag>
# ./xpolymonk-source.sh 0.6

git clone https://github.com/brummer10/XPolyMonk.lv2
cd XPolyMonk.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz XPolyMonk.lv2.tar.gz XPolyMonk.lv2/*
rm -rf XPolyMonk.lv2
