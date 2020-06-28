#!/bin/bash

# Usage: ./source.sh <TAG>
# ./source.sh 3.1.2

git clone https://github.com/michaelwillis/dragonfly-reverb
cd dragonfly-reverb
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz dragonfly-reverb.tar.gz dragonfly-reverb/*
rm -rf dragonfly-reverb

