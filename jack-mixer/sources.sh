#!/bin/bash

# ./sources.sh release-13

git clone https://repo.or.cz/jack_mixer.git
cd jack_mixer
git checkout $1
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz jack_mixer.tar.gz jack_mixer/
rm -rf jack_mixer
