#!/bin/bash

# ./GrandOrgue-source.sh <rev>
# ./GrandOrgue-source.sh 2330

svn export -r $1 http://svn.code.sf.net/p/ourorgan/svn/trunk ourorgan-$1
tar cvfz ourorgan-$1.tar.gz ourorgan-$1
rm -rf ourorgan-$1
