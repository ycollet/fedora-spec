#/bin/bash

# ./loudness-scanner-source.sh <tag>
# ./loudness-scanner-source.sh v0.5.1

git clone https://github.com/jiixyj/loudness-scanner
cd loudness-scanner
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz loudness-scanner.tar.gz loudness-scanner/*
rm -rf loudness-scanner
