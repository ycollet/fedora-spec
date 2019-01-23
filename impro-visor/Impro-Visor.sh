#!/bin/bash
#
# startscript for Impro-Visor
#
# written by oc2pus
#
# Changelog:
# 25.01.2007 initial version
# 23.02.2008 added styles

# activate for debugging
#set -x

# base settings
myShareDir=/usr/share/improvisor
myHomeDir=~/impro-visor-version-7.00-files

# creates a local working directory in user-home
function createLocalDir ()
{
 	if [ ! -d $myHomeDir ]; then
		echo "creating local working directory $myHomeDir ..."
		mkdir -p $myHomeDir

		mkdir -p $myHomeDir/leadsheets
		cp -a $myShareDir/leadsheets $myHomeDir

                mkdir -p $myHomeDir/grammars
                cp -a $myShareDir/grammars $myHomeDir

		mkdir -p $myHomeDir/styles
		cp -a $myShareDir/styles $myHomeDir

		mkdir -p $myHomeDir/vocab
		cp $myShareDir/vocab/* $myHomeDir/vocab
	fi
 	if [ ! -d $myHomeDir/imaginary ]; then
		mkdir -p $myHomeDir/imaginary
		cp $myShareDir/imaginary/* $myHomeDir/imaginary
	fi
 	if [ ! -d $myHomeDir/styleExtract ]; then
		mkdir -p $myHomeDir/styleExtract
		cp $myShareDir/styleExtract/* $myHomeDir/styleExtract
	fi
}

echo ""
echo "starting Impro-Visor ..."

# creates a local working directory in user-home
createLocalDir

cd $myHomeDir

# source the jpackage helpers
VERBOSE=1
. /usr/share/java-utils/java-functions

# set JAVA_* environment variables
set_javacmd
check_java_env
set_jvm_dirs

CLASSPATH=`build-classpath improvisor`
MAIN_CLASS="imp.ImproVisor"

run
