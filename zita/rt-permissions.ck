#!/bin/bash
#
# Set realtime and memory locking permissions when sessions change state
#
# (C)2011 Fernando Lopez-Lezcano
#

# gets called with a single argument:
#
#  session_added
#  session_removed
#  session_active_changed
#
EVENT="${1}"

# ignore uids lower than this one
LOWUID=500

# max rt priority allowed
MAXPRIO=@@MAX_PRIORITY@@
# max memory that can be locked
MAXMEM=@@MAX_MEMORY_LOCK@@

if [ $CK_SESSION_USER_UID -lt $LOWUID ] ; then
    exit 0
fi

# only for local sessions
if [ "$CK_SESSION_IS_LOCAL" = "true" ] ; then
    if [ "${EVENT}" = "session_added" ] ; then
        ulimit -r ${MAXPRIO}
        ulimit -l ${MAXMEM}
    elif [ "${EVENT}" = "session_removed" ] ; then
        ulimit -r 0
        ulimit -l 0
    elif [ "${EVENT}" = "session_active_changed" ] ; then
        # take care of a session that changes state
        if [ "${CK_SESSION_IS_ACTIVE}" = "true" ] ; then
    	    ulimit -r ${MAXPRIO}
	    ulimit -l ${MAXMEM}
	else
    	    ulimit -r 0
	    ulimit -l 0
        fi
    else
        # unrecognized argument, should be an error
        exit 0
    fi
fi
