# Global variables for github repository
%global commit0 4e075332fa0867a65740c8a55eb7bce063ae3527
%global gittag0 v0.5.0
#%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           Rack
Version:        0.5.0
Release:        1%{?dist}
Summary:        A modular synthetizer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/VCVRack/Rack.git

Source0:        rack.png

BuildRequires: git
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
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel

%description
A modular synthetizer

%prep

[ ! -d Rack ] && git clone https://github.com/VCVRack/Rack.git
cd Rack
git pull
git checkout -- compile.mk
git checkout %{gittag0}

rm -rf include/rtmidi
mkdir -p include/rtmidi
ln -s /usr/include/RtMidi.h include/rtmidi/RtMidi.h 
CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-g//g" compile.mk
echo "CXXFLAGS += -I$CURRENT_PATH/include" >> compile.mk

git submodule init
git submodule update

cd dep
git submodule init
git submodule update
sed -i -e "s/--with-ssl=\"\$(LOCAL)\"/--with-ssl/g" Makefile

cd ../plugins
[ ! -d AudibleInstruments ] && git clone https://github.com/VCVRack/AudibleInstruments.git
cd AudibleInstruments
git pull
git submodule init
git submodule update
cd eurorack 
git submodule init
git submodule update
cd ..
cd ..
[ ! -d Befaco ] && git clone https://github.com/VCVRack/Befaco.git
cd Befaco
git pull
cd ..
[ ! -d ESeries ] && git clone https://github.com/VCVRack/ESeries.git
cd ESeries
git pull
cd ..
[ ! -d Fundamental ] && git clone https://github.com/VCVRack/Fundamental.git
cd Fundamental
git pull
cd ..

#[ ! -d ML_modules ] && git clone https://github.com/martin-lueders/ML-modules.git
#cd ML_modules
#git pull
#%make_build
#cd ..

#[ ! -d vcv_luckyxxl ] && git clone https://github.com/luckyxxl/vcv_luckyxxl.git
#cd vcv_luckyxxl
#git pull
#%make_build
#cd ..

#[ ! -d vcvrackplugins_av500 ] && git clone https://github.com/av500/vcvrackplugins_av500.git
#cd vcvrackplugins_av500
#git pull
#%make_build
#cd ..

#[ ! -d vcvrackplugins_dekstop ] && git clone https://github.com/av500/vcvrackplugins_dekstop.git
#cd vcvrackplugins_dekstop
#git pull
#%make_build
#cd ..

%build
cd Rack
cd dep
make
cd ..
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}
cd plugins
cd AudibleInstruments
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}
cd ..
cd Befaco
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}
cd ..
cd ESeries
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}
cd ..
cd Fundamental
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}


%install 
cd Rack

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/man/man1/
mkdir -p %{buildroot}%{_datadir}/applications/

install -m 755 Rack       %{buildroot}%{_bindir}/
install -m 755 Rack.sh    %{buildroot}%{_bindir}/
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/pixmaps/rack.png

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

%changelog
* Tue Dec 26 2017 Yann Collette <ycollette.nospam@free.fr> - 0.5.0
- update to version 0.5.0

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.4.0
- update to version 0.4.0

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1
- Initial build
