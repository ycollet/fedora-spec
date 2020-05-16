%global debug_package %{nil}

# Global variables for github repository
%global commit0 4e428f197a2b59fc89718052d07015bda89de3ad
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    abNinjam
Version: 0.0.2
Release: 1%{?dist}
Summary: Ninjam LV2 / VST plugin
URL:     https://github.com/antanasbruzas/abNinjam
Group:   Applications/Multimedia
License: GPLv3

Source0: abNinjam.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
BuildRequires: cmake make

%description
Ninjam LV2 / VST plugin.

%prep
%setup -qn %{name}

# Don't try to create /usr/lib64/{vst,lv2} directories
sed -i -e "/MAKE_DIRECTORY/d" cmake/VSTConfig.cmake

%build

mkdir build
cd build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DVSTPLUGIN_INSTALL_DIR=%{_libdir}/vst \
       -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2 \
       ..

make DESTDIR=%{buildroot}

%install

cd build

make DESTDIR=%{buildroot} install

%files
%doc LICENSE README.md
%{_libdir}/*

%changelog
* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- initial version of the spec file
