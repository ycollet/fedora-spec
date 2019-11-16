#!/usr/bin/env bash
#
# Remove documentation files from source archives
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

VSXU_VERSION=`rpm -q --queryformat "%{version}\n" --specfile vsxu.spec | head -n1`
wget -c https://github.com/vovoid/vsxu/archive/v${VSXU_VERSION}.tar.gz \
     -O vsxu-${VSXU_VERSION}.tar.gz
gunzip -v < vsxu-${VSXU_VERSION}.tar.gz > vsxu-${VSXU_VERSION}.tar && \
tar -v --wildcards --delete -f vsxu-${VSXU_VERSION}.tar \
	"vsxu-${VSXU_VERSION}/lib/engine_graphics/thirdparty/glew-*" \
	&& \
mv -v vsxu-${VSXU_VERSION}.tar vsxu-${VSXU_VERSION}-noglew.tar && \
xz -9 -v vsxu-${VSXU_VERSION}-noglew.tar
rm vsxu-${VSXU_VERSION}.tar.gz
