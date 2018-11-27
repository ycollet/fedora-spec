# Global variables for github repository
%global commit0 7d8c04c993fa6d2d37e41bfaef015970e1932e5c
%global gittag0 v0.6.2c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    Rack
Version: 0.6.2c
Release: 3%{?dist}
Summary: A modular synthetizer

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/VCVRack/Rack.git

# git clone https://github.com/VCVRack/Rack.git Rack
# cd Rack
# #git checkout v0.6.2b
# git submodule init
# git submodule update
# find . -name ".git" -exec rm -rf {} \;
# cd dep
# wget https://bitbucket.org/jpommier/pffft/get/29e4f76ac53b.zip
# unzip 29e4f76ac53b.zip
# mkdir include
# cp jpommier-pffft-29e4f76ac53b/*.h include/
# rm  29e4f76ac53b.zip
# cd ../..
# tar cvfz Rack.tar.gz Rack/*

Source0: Rack.tar.gz
Source1: rack.png
Patch0: rack-0001-add-global-plugins.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake sed
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libzip-devel
BuildRequires: glew-devel
BuildRequires: glfw-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: jansson-devel
BuildRequires: gtk2-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel

%description
A modular synthetizer

%prep
%setup -qn %{name}

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-g//g" compile.mk
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile

sed -i -e "s/assetGlobalDir = \".\";/assetGlobalDir = \"\/usr\/libexec\/Rack\";/g" src/asset.cpp

%patch0 -p1 

%build
cd dep
cd glfw
cmake -DCMAKE_INSTALL_PREFIX=.. -DGLFW_COCOA_CHDIR_RESOURCES=OFF -DGLFW_COCOA_MENUBAR=ON -DGLFW_COCOA_RETINA_FRAMEBUFFER=ON .
make
make install

cd ../..
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}

%install 

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/man/man1/
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_libexecdir}/Rack/plugins/

install -m 755 Rack       %{buildroot}%{_bindir}/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/rack.png
cp -r res %{buildroot}%{_libexecdir}/Rack/

cat > %{buildroot}%{_datadir}/applications/Rack.desktop << EOF
[Desktop Entry]
Name=Rack
Comment=A modular synthetizer.
Exec=/usr/bin/Rack
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/rack.png
Categories=AudioVideo;
EOF

%files
%{_bindir}/*
%{_datadir}/*
%{_libexecdir}/*

%changelog
* Mon Nov 26 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2c
- update to 0.6.2c

* Mon Nov 26 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2b
- fix global plugins loading

* Thu Nov 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2b
- update to 0.6.2b

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.5.0
- update for Fedora 29

* Tue Dec 26 2017 Yann Collette <ycollette.nospam@free.fr> - 0.5.0
- update to version 0.5.0

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.4.0
- update to version 0.4.0

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1
- Initial build
