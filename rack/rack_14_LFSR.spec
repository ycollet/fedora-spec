# Global variables for github repository
%global commit0 00cfcf740cc079d6faa7f6230b3f46c0e4ff8767
%global gittag0 v0.6.21
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-LFSR
Version: 0.6.21
Release: 1%{?dist}
Summary: A plugin for Rack

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/alto777/LFSR

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

Source0: Rack.tar.gz
Source1: https://github.com/alto777/LFSR/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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
LFSR: Linear Feedback Shift Register sequencers

These are modules for VCV Rack - https://vcvrack.com/. I present them for your enjoyment and exploitation, musically or however. As with all synthesizer modules, experimentation will unlock whatever potential lurks.

All the source code is here. You are welcome to use it, but be warned I am neither a C++ programmer nor a musician. *It may not be the best place to start for making your own progress or answering questions*. But I do encourage you to dare ascend the learning curve laid out on VCV Rack's github site. I am quite surprised at how rapidly all this makes a certain level of incompetence in module-making possible. Hats off to Rack. It's all there if you look hard enough.

%prep
%setup -qn Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-g//g" compile.mk
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile

sed -i -e "s/assetGlobalDir = \".\";/assetGlobalDir = \"\/usr\/libexec\/Rack\";/g" src/asset.cpp

mkdir alto777_LFSR_plugin
tar xvfz %{SOURCE1} --directory=alto777_LFSR_plugin --strip-components=1 

%build

cd alto777_LFSR_plugin
make RACK_DIR=.. DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack/alto777_LFSR/
cp -r alto777_LFSR_plugin/dist/alto777_LFSR/* %{buildroot}%{_libexecdir}/Rack/alto777_LFSR/

%files
%{_libexecdir}/*

%changelog
* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.21
- initial specfile
