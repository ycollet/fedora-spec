# Global variables for github repository
%global commit0 01e5e0301d6c1f6b3d52e717fa2ba7098dd4b49c
%global gittag0 v1.1.6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    Rack-v1
Version: 1.1.6
Release: 10%{?dist}
Summary: A modular synthetizer
License: GPLv2+
URL:     https://github.com/VCVRack/Rack

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

Source0: Rack.tar.gz
Source1: Rack-manual.tar.gz

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
BuildRequires: python3-sphinx
BuildRequires: python3-recommonmark
BuildRequires: python3-sphinx_rtd_theme

Requires: rack-v1-Fundamental

%description
A modular synthetizer

%package doc
Summary:   Documentation files for Rack
BuildArch: noarch

%description doc
Documentation files for Rack

%prep
%autosetup -n Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=nocona//g" compile.mk
sed -i -e "s/-O3/-O2/g" compile.mk

echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-rack -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile
sed -i -e "s/dep\/lib\/libglfw3.a/-lglfw/g" Makefile
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

sed -i -e "s/systemDir = \".\";/systemDir = \"\/usr\/libexec\/Rack1\";/g" src/asset.cpp
sed -i -e "s/pluginsPath = userDir + \"\/plugins-v\"/pluginsPath = systemDir + \"\/plugins-v\"/g" src/asset.cpp

# This options seems to make Rack hangs after a restart ...
sed -i -e "s/options.flags |= RTAUDIO_JACK_DONT_CONNECT/\/\/options.flags |= RTAUDIO_JACK_DONT_CONNECT/g" src/audio.cpp

tar xvfz %{SOURCE1}

sed -i -e "s/sphinx-build/sphinx-build-3/g" manual/Makefile

%build

export CFLAGS=
export CXXFLAGS=
export LDFLAGS=

cd dep
cd glfw
cmake -DCMAKE_INSTALL_PREFIX=.. -DGLFW_COCOA_CHDIR_RESOURCES=OFF -DGLFW_COCOA_MENUBAR=ON -DGLFW_COCOA_RETINA_FRAMEBUFFER=ON -DCMAKE_BUILD_TYPE=DEBUG .
%make_build
%make_install
cd ..
cd ..

%make_build PREFIX=/usr LIBDIR=%{_lib}

cd manual
%make_build html

%install 

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/man/man1/
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/Rack/html/
mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins/

install -m 755 Rack         %{buildroot}%{_bindir}/
install -m 644 res/icon.png %{buildroot}%{_datadir}/pixmaps/rack.png
cp -r res                   %{buildroot}%{_libexecdir}/Rack1/

cp -r manual/_build/html/* %{buildroot}%{_datadir}/Rack/html/

cp cacert.pem Core.json template.vcv %{buildroot}%{_libexecdir}/Rack1/

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
%doc README.md CHANGELOG.md
%license LICENSE-GPLv3.txt LICENSE-dist.txt LICENSE.md
%{_bindir}/*
%{_datadir}/*
%{_libexecdir}/*

%files doc
%{_datadir}/*

%changelog
* Sun Nov 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.6-10
- disable compilation flags

* Thu Oct 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.6-9
- update to 1.1.6-9

* Wed Jan 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.6-8
- update to 1.1.6-8

* Mon Jan 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.6-6
- update to 1.1.6

* Fri Oct 11 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.5-6
- update to 1.1.5

* Wed Dec 5 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2c-6
- add static glew

* Wed Nov 28 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2c-5
- fix compilation flags

* Mon Nov 26 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2c-4
- add documentation package

* Mon Nov 26 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.2c-3
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
