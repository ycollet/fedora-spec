#!/bin/bash

# ./mamba_source.sh <tag>
# ./mamba_source.sh v1.6

git clone https://github.com/brummer10/Mamba
cd Mamba
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Mamba.tar.gz Mamba/*
rm -rf Mamba
