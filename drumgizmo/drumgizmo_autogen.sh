#!/bin/sh -e

# Check if hugin has been obtained:
if [ ! -f hugin/hugin.c ]
then
		echo "You are missing the hugin submodule."
		echo "Run"
		echo " git submodule init"
		echo " git submodule update"
		echo "to obtain it."
		exit 1
fi

# Check for support of AC_PROG_OBJCXX macro. If missing emulate it.
mkdir -p actest
cat << EOF > actest/configure.ac
AC_INIT([actest], [1.0.0])
AC_PROG_OBJCXX
EOF
[ -f acinclude.m4 ] && rm acinclude.m4
autoreconf -W error actest 2>/dev/null || echo "AC_DEFUN([AC_PROG_OBJCXX],[echo ' - ObjC++ hack - not support by this platform, but not needed either.'])" > acinclude.m4
rm -Rf actest

# Now run autoreconf
${AUTORECONF:-autoreconf} -fiv --warnings=no-unsupported
