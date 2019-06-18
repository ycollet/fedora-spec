# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 fe078ea036991081c3a28bb388a3fecd0e8e3a5d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    surge
Version: 1.6.0.b9.%{shortcommit0}
Release: 1%{?dist}
Summary: A VST2 synthetizer

Group:   Applications/Multimedia
License: GPLv2+

# git clone https://github.com/surge-synthesizer/surge
# cd surge
# git checkout release/1.6.0-beta-9
# git submodule init
# git submodule update
# cd vst3dsk
# git submodule init
# git submodule update
# cd ..
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz surge.tar.gz surge/*

URL:     https://github.com/surge-synthesizer/surge
Source0: surge.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: premake5
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: rsync
BuildRequires: python2
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel

%description
A VST2 synthetizer

%prep
%setup -qn %{name}

%ifarch x86_64
  sed -i -e "s/lib\/vst/lib64\/vst/g" build-linux.sh
%endif

sed -i -e "s/python/python2/g" premake5.lua

%build

tar xvfj %{SOURCE1}

export VST2SDK_DIR=vst/vstsdk2.4/

./build-linux.sh clean-all
./build-linux.sh -p vst2 build

%install 

export HOME=.
mkdir .vst
mkdir .local/
mkdir .local/share

./build-linux.sh -p vst2 -l install

%__install -m 755 -d %{buildroot}%{_libdir}/vst/
%__install -m 644 .vst/*.so %{buildroot}/%{_libdir}/vst/

%__install -m 755 -d %{buildroot}%{_datadir}/Surge/
rsync -rav .local/share/Surge/* %{buildroot}/%{_datadir}/Surge/

%files
%{_libdir}/*
%{_datadir}/*

%changelog
* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b9
- update to beta9

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b3
- Initial spec file
