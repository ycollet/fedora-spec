#!/bin/bash

# ./purr-data-source.sh <tag>
# ./purr-data-source.sh 2.17.0

git clone https://github.com/agraef/purr-data
cd purr-data
git checkout $1
git submodule init
git submodule update
cd ..
tar cvfz purr-data.tar.gz purr-data
rm -rf purr-data
