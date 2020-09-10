# Global variables for github repository
%global commit0 eb41dd7cdf1112530c1a8059cfa3a99a402944ef
%global gittag0 v1.4.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-Fundamental
Version: 1.4.0
Release: 4%{?dist}
Summary: A plugin for Rack
License: GPLv2+
URL:     https://github.com/VCVRack/Fundamental

%define with_glew  %{?_with_glew:  1} %{?!_with_glew:  0}

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
Source1: https://github.com/VCVRack/Fundamental/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source2: Fundamental_plugin.json

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
BuildRequires: jq

%description
The Fundamental plugin pack gives you a basic foundation to create simple synthesizers, route and analyze signals, complement other more complicated modules, and build some not-so-simple patches using brute force (lots of modules).
They are also a great reference for creating your own plugins in C++.

%prep
%autosetup -n Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-march=nocona//g" compile.mk
sed -i -e "s/-ffast-math//g" compile.mk
sed -i -e "s/-fno-finite-math-only//g" compile.mk
sed -i -e "s/-O3/-O2/g" compile.mk

echo "CXXFLAGS += %{build_cxxflags} -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile
%if %{with_glew}
sed -i -e "s/-lGLEW/dep\/lib\/libGLEW.a/g" Makefile
%endif

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile

sed -i -e "s/dep\/lib\/libglfw3.a/dep\/%{_lib}\/libglfw3.a/g" Makefile

sed -i -e "s/dep\/lib\/libjansson.a/-ljansson/g" Makefile
sed -i -e "s/dep\/lib\/libcurl.a/-lcurl/g" Makefile
sed -i -e "s/dep\/lib\/libssl.a/-lssl/g" Makefile
sed -i -e "s/dep\/lib\/libcrypto.a/-lcrypto/g" Makefile
sed -i -e "s/dep\/lib\/libzip.a/-lzip/g" Makefile
sed -i -e "s/dep\/lib\/libz.a/-lz/g" Makefile
sed -i -e "s/dep\/lib\/libspeexdsp.a/-lspeexdsp/g" Makefile
sed -i -e "s/dep\/lib\/libsamplerate.a/-lsamplerate/g" Makefile
sed -i -e "s/dep\/lib\/librtmidi.a/-lrtmidi/g" Makefile
sed -i -e "s/dep\/lib\/librtaudio.a/-lrtaudio/g" Makefile

mkdir fundamental_plugin
tar xvfz %{SOURCE1} --directory=fundamental_plugin --strip-components=1 

cp %{SOURCE2} fundamental_plugin/plugin.json

# Remove libsamplerate download and install
sed -i -e "7,20d" fundamental_plugin/Makefile

%build

cd fundamental_plugin

make RACK_DIR=.. DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Fundamental/
cp -r fundamental_plugin/dist/Fundamental/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Fundamental/

%files
%{_libexecdir}/*

%changelog
* Tue Sep 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-4
- update to 1.4.0-4.

* Thu Feb 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-4
- update to 1.3.1-4. Update to last master to add Pulse plugin

* Mon Jan 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1
- update to 1.3.1

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.1
- initial specfile
