#!/bin/bash

# ./littlefly-source.sh <tag>
# ./littlefly-source.sh v1.0

git clone https://github.com/brummer10/LittleFly.lv2
cd LittleFly.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz LittleFly.lv2.tar.gz LittleFly.lv2/*
rm -rf LittleFly.lv2
