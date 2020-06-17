%global debug_package %{nil}

# Global variables for github repository
%global commit0 fc50af9e2603c2184f24f3a3483203d69d4b2c2a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    abNinjam
Version: 0.0.8
Release: 1%{?dist}
Summary: Ninjam LV2 / VST plugin
URL:     https://github.com/antanasbruzas/abNinjam
Group:   Applications/Multimedia
License: GPLv3

# git clone https://github.com/antanasbruzas/abNinjam
# cd abNinjam
# git checkout v0.0.8
# git submodule init
# git submodule update --recursive
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar xvfz abNinjam.tar.gz abNinjam/*
# rm -rf abNinjam

Source0: abNinjam.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libvorbis-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: cmake make

%description
Ninjam LV2 / VST plugin.

%prep
%autosetup -n %{name}

# Don't try to create /usr/lib64/{vst,lv2} directories
sed -i -e "/MAKE_DIRECTORY/d" cmake/VSTConfig.cmake

%build

mkdir build
cd build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DVSTPLUGIN_INSTALL_DIR=%{_libdir}/vst \
       -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2 \
       ..

%make_build

%install

cd build

%make_install

%files
%doc README.md
%license LICENSE 
%{_libdir}/vst/*
%{_libdir}/lv2/*

%changelog
* Wed Jun 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- update to 0.0.8-1

* Sun Jun 7 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.7-1
- update to 0.0.7-1

* Sun May 31 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update to 0.0.5-1

* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- initial version of the spec file
