#!/bin/bash

# ./abninjam-source.sh <tag>
# ./abninjam-source.sh v0.0.8

git clone https://github.com/antanasbruzas/abNinjam
cd abNinjam
git checkout $1
git submodule init
git submodule update --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz abNinjam.tar.gz abNinjam/*
rm -rf abNinjam
