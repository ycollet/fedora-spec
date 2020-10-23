#!/bin/bash

# ./sisco-source.sh <tag>
# ./sisco-source.sh v0.9.0

git clone https://github.com/x42/sisco.lv2
cd sisco.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz sisco.lv2.tar.gz sisco.lv2/*
rm -rf sisco.lv2
