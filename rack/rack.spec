# Global variables for github repository
%global commit0 4e075332fa0867a65740c8a55eb7bce063ae3527
#%global gittag0 v0.3.1
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           Rack
Version:        0.3.1
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
BuildRequires: jansson-devel
BuildRequires: gtk2-devel

%description
A modular synthetizer

%prep

[ ! -d Rack ] && git clone https://github.com/VCVRack/Rack.git
cd Rack
git pull

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-g//g" compile.mk

git submodule init
git submodule update
cd plugins
[ ! -d AudibleInstruments ] && git clone https://github.com/VCVRack/AudibleInstruments.git
cd AudibleInstruments
git pull
git submodule init
git submodule update
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

%build
cd Rack
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
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1
- Initial build
