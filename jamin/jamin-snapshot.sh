#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
cvs=$(date +%Y%m%d)cvs
name=jamin
version=0.97.16

cd "$tmp"
cvs -z3 -d:pserver:anonymous@$name.cvs.sourceforge.net:/cvsroot/$name export -D $(date +%Y%m%d) $name
mv $name $name-$version
tar jcf "$pwd"/$name-$version-$cvs.tar.bz2 $name-$version

echo "Written: $name-$version-$cvs.tar.bz2"
cd - >/dev/null
