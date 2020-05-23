# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 b674f7ec1f41d8f0fcfea86e3d3d3df3e9bdcf36
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    openFrameworks
Version: 0.11.0.%{shortcommit0}
Release: 1%{?dist}
Summary: openFrameworks library / code
URL:     https://github.com/openframeworks/openFrameworks
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
# git clone https://github.com/openframeworks/openFrameworks
# cd openFrameworks
# git checkout 0.11.0
# git submodule init
# git submodule update
# ./script/linux/download_libs.sh
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvf openFrameworks.tar.gz openFrameworks/*
# rm -rf openFrameworks

# Source0: https://github.com/openframeworks/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source0: openFrameworks.tar.gz
Source1: of-make-workspace
# Patch0: openal_fix.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ make
BuildRequires: freeimage-devel
BuildRequires: uriparser-devel
BuildRequires: pugixml-devel
BuildRequires: poco-devel

%description
openFrameworks is a C++ toolkit for creative coding. If you are new to OF, welcome!

%prep
# %setup -qn %{name}-%{commit0}
%setup -qn %{name}

# %patch0 -p0

%build

export OF_ROOT=`pwd`
export LC_ALL=C

ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]; then
    LIBSPATH=linux64
else
    LIBSPATH=linux
fi

cd libs/openFrameworksCompiled/project
%{__make} %{?_smp_mflags} Release

cd ../../..

cd apps/projectGenerator/commandLine
%{__make} %{?_smp_mflags} Release

cd ../../..
cd libs/openFrameworksCompiled/project
%{__make} %{?_smp_mflags} Release

%install

%__install -dm755 %{buildroot}/%{_bindir}/
%__install -Dm755 apps/projectGenerator/commandLine/bin/projectGenerator %{buildroot}/%{_bindir}/projectGenerator

%__install -dm755 %{buildroot}/opt/openFrameworks
cp -R . %{buildroot}/opt/openFrameworks

%__install -Dm775 %{SOURCE1} %{buildroot}/opt/openFrameworks/scripts/of-make-workspace

sed -i -e "s/env python/env python2/g" %{buildroot}/opt/openFrameworks/scripts/dev/parsePRs.py

rm -rf %{buildroot}/opt/openFrameworks/.appveyor.yml
rm -rf %{buildroot}/opt/openFrameworks/.gitattributes
rm -rf %{buildroot}/opt/openFrameworks/.gitignore
rm -rf %{buildroot}/opt/openFrameworks/.gitmodules
rm -rf %{buildroot}/opt/openFrameworks/.travis.yml

%files
%doc README.md LICENSE.md 
%{_bindir}/*
/opt/%{name}/*

%changelog
* Sat May 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.11.0-1
- initial specfile
