#!/bin/bash

# ./wolf-shapper-source.sh <tag>
# ./wolf-shapper-source.sh v0.1.8

git clone https://github.com/pdesaulniers/wolf-shaper
cd wolf-shaper
git checkout $1
git submodule init
git submodule update
rm -rf .git dpf/.git
cd ..
tar cvfz wolf-shaper.tar.gz wolf-shaper/*
rm -rf wolf-shapper
