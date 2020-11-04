#!/bin/bash

# ./sfizz_source.sh <tag>
# ./sfizz_source.sh 0.4.0

git clone https://github.com/sfztools/sfizz sfizz-$1
cd sfizz-$1
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz sfizz-$1.tar.gz sfizz-$1/*
rm -rf sfizz-$1
