#!/bin/bash

# ./stone-phaser-source.sh <tag>
# ./stone-phaser-source.sh v0.1.2

git clone https://github.com/jpcima/stone-phaser
cd stone-phaser
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stone-phaser.tar.gz stone-phaser/*
rm -rf stone-phaser
