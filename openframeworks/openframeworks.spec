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

Source0: openFrameworks.tar.gz
Source1: of-make-workspace

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ make
BuildRequires: freeimage-devel
BuildRequires: uriparser-devel
BuildRequires: pugixml-devel
BuildRequires: poco-devel
BuildRequires: openal-soft-devel
BuildRequires: cairo-devel
%if 0%{?fedora} >= 32
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
%else
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
%endif
BuildRequires: systemd-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libsndfile-devel
BuildRequires: libcurl-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: alsa-lib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: glew-devel
BuildRequires: freeglut-devel
BuildRequires: glfw-devel
BuildRequires: boost-devel
BuildRequires: opencv-devel
BuildRequires: rtaudio-devel
BuildRequires: mpg123-devel
BuildRequires: libXcursor-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXrandr-devel
#BuildRequires: python2-lxml
#BuildRequires: assimp-devel

%description
openFrameworks is a C++ toolkit for creative coding. If you are new to OF, welcome!

The Project Generator is in /opt/openFrameworks/apps/projectGenerator/projectGeneratorSimple.
To initialize the workspace needed for openFrameworks launch the command: '/opt/openFrameworks/scripts/of-make-workspace'
this command will initialize a workspace folder, with no path given the default folder is: ~/of-workspace.

Remeber to regenerate your local workspace using: '/opt/openFrameworks/scripts/of-make-workspace'
If you already have a local workspace, BACKUP YOUR PROJECTS BEFORE generating a new local workspace.

%prep
%setup -qn %{name}

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
