#!/bin/bash

# ./ossia-source.sh <tag>
# ./ossia-source.sh v2.5.2

git clone https://github.com/OSSIA/score
cd score
git checkout $1
git submodule init
git submodule update
cd 3rdparty/libossia/
git submodule init
git submodule update
cd ../..
find . -name .git -exec rm -rf {} \;
cd ..
mv score score-$1
tar cvfz score-$1.tar.gz score-$1/*
rm -rf score-$1
