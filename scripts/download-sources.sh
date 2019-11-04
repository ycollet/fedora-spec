#/bin/bash

RELEASEVER=30

for Files in `dnf --releasever $RELEASEVER list --available | grep ycollet | grep -v debuginfo | grep -v debugsource | grep "\.x86_64" | sed -e "s/\(^.*\)\.x86_64.*/\1/"`
do
    echo "Downloading $Files SRPMS file"
    dnf --releasever $RELEASEVER download --source $Files
done
