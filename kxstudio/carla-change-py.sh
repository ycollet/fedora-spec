#!/bin/bash

FILES=`find . -name "*.py" -exec grep -l "env python$" {} \;`

for Files in $FILES
do
    echo "Change python$ to python2$"
    sed -i -e "s/env python$/env python2/g" $Files
done
