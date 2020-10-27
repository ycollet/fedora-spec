#!/bin/bash

# ./xmonk-source.sh <tag>
# ./xmonk-source.sh 0.4

git clone https://github.com/brummer10/Xmonk.lv2
cd Xmonk.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Xmonk.lv2.tar.gz Xmonk.lv2/*
rm -rf Xmonk.lv2
