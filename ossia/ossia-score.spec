%global debug_package %{nil}

# Global variables for github repository
%global commit0 f7e34e37d376e18ec097fa42957c9ecb42d50b9f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    ossia-score
Version: 2.5.2
Release: 1%{?dist}
Summary: ossia score is a sequencer for audio-visual artists, designed to create interactive shows
URL:     https://github.com/OSSIA/score
Group:   Applications/Multimedia
License: CeCILL License v2

# git clone https://github.com/OSSIA/score
# cd score
# git checkout v2.5.2
# git submodule init
# git submodule update
# cd 3rdparty/libossia/
# git submodule init
# git submodule update
# cd ../..
# find . -name .git -exec rm -rf {} \;
# cd ..
# mv score score-v2.5.2
# tar cvfz score-v2.5.2.tar.gz score-v2.5.2/*

Source0: https://gitlab.com/OSSIA/score/-/archive/v%{version}/score-v%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qttools
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: ffmpeg-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: unzip

%description
ossia score is a sequencer for audio-visual artists, designed to create interactive shows

%prep
%setup -qn score-v%{version}

%build

mkdir build
cd build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DSCORE_CONFIGURATION=static-release \
       -DPORTAUDIO_ONLY_DYNAMIC=1 ..

make DESTDIR=%{buildroot} %{?_smp_mflags}

%install

cd build

make DESTDIR=%{buildroot} install

%__install -m 755 -d %{buildroot}/%{_datadir}/Ossia/
mv %{buildroot}/%{_usr}/Ossia %{buildroot}/%{_datadir}/Ossia/Qml

# remove lib, it contains only static libs
rm -rf %{buildroot}/%{_usr}/lib

rm -f %{buildroot}/%{_usr}/include/.gitignore

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%doc LICENSE.txt INSTALL.md README.md AUTHORS
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*

%changelog
* Wed Oct 23 2019 Yann Collette <ycollette.nospam@free.fr> - 2.5.2-1
- initial version of the spec file
