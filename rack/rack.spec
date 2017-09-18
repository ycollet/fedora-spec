# Global variables for github repository
%global commit0 5f49d9b27d63f4da9b100f9ce5176c25468606e8
%global gittag0 v0.7.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           Rack
Version:        0.3.1
Release:        1%{?dist}
Summary:        A modular synthetizer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/VCVRack/Rack.git

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

%description
A modular synthetizer

%prep

git clone https://github.com/VCVRack/Rack.git
cd Rack
sed -i -e "s/-march=core2//g" compile.mk
git submodule init
git submodule update
cd plugins
git clone https://github.com/VCVRack/AudibleInstruments.git
cd AudibleInstruments
git submodule init
git submodule update
cd ..
git clone https://github.com/VCVRack/Befaco.git
git clone https://github.com/VCVRack/ESeries.git
https://github.com/VCVRack/Fundamental.git

%build
cd Rack
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} sisco_VERSION=%{version} LDFLAGS=-lpthread %{?_smp_mflags}

%install 
cd Rack

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/man/man1/
mkdir -p %{buildroot}%{_datadir}/applications/

install -m 755 postfish %{buildroot}%{_bindir}/
install -m 644 %{S:1} %{buildroot}%{_datadir}/pixmaps/Rack.png

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
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1
- Initial build
