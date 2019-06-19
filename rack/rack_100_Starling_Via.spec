# Global variables for github repository
%global commit0 452bf55af2026f9ed91745bf714c9dfb825227e1
%global gittag0 v0.6.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-Starling_Via
Version: 0.6.0
Release: 2%{?dist}
Summary: A plugin for Rack

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/starlingcode/Via-for-Rack

# git clone https://github.com/VCVRack/Rack.git Rack
# cd Rack
# git checkout v0.6.2b
# git submodule init
# git submodule update
# find . -name ".git" -exec rm -rf {} \;
# cd dep
# wget https://bitbucket.org/jpommier/pffft/get/29e4f76ac53b.zip
# unzip 29e4f76ac53b.zip
# cp jpommier-pffft-29e4f76ac53b/*.h include/
# rm  29e4f76ac53b.zip
# cd ..
# tar cvfz Rack.tar.gz Rack/*

# git clone https://github.com/starlingcode/Via-for-Rack
# cd Via-for-Rack
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz Via-for-Rack.tar.gz Via-for-Rack
# rm -rf Via-for-Rack

Source0: Rack.tar.gz
Source1: Via-for-Rack.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
Starling_Via modules for VCV Rack

%prep
%setup -qn Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-g//g" compile.mk
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile

sed -i -e "s/assetGlobalDir = \".\";/assetGlobalDir = \"\/usr\/libexec\/Rack\";/g" src/asset.cpp

mkdir Starling_Via_plugin
tar xvfz %{SOURCE1} --directory=Starling_Via_plugin --strip-components=1 

%build

cd Starling_Via_plugin
make RACK_DIR=.. DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack/plugins/Starling_Via/
cp -r Starling_Via_plugin/dist/Starling_Via/* %{buildroot}%{_libexecdir}/Rack/plugins/Starling_Via/

%files
%{_libexecdir}/*

%changelog
* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.0
- initial specfile
