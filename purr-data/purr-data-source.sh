#!/bin/bash

# ./source.sh <tag>
# ./source.sh 2.15.1

git clone https://github.com/agraef/purr-data
cd purr-data
git checkout $1
git submodule init
git submodule update
cd ..
tar cvfz purr-data.tar.gz purr-data
rm -rf purr-data
