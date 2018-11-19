#!/bin/bash
# $1: tag to check

for Files in `ls -1d */`
do
    cd $Files
    TAGS=`git tag -l | grep $1`
    if [ ! -z "$TAGS" ];
    then
	echo "$Files has tags $1"
    fi
    cd ..
done
