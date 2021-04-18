#!/bin/bash

# ./gxplugins-source.sh <tag>
# ./gxplugins-source.sh v0.9

git clone https://github.com/brummer10/GxPlugins.lv2.git
cd GxPlugins.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz GxPlugins.lv2.tar.gz GxPlugins.lv2
rm -rf GxPlugins.lv2
