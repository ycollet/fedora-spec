#!/bin/bash

# Usage: ./source-chowcentaur.sh <tag>
#        ./source-chowcentaur.sh 1.3.0

git clone https://github.com/jatinchowdhury18/KlonCentaur
cd KlonCentaur
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz KlonCentaur.tar.gz KlonCentaur/*
rm -rf KlonCentaur
