# Global variables for github repository
%global commit0 d2f68cebc74445f8f758b422afdb440c9bcc1f7f
%global gittag0 3.1.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    dragonfly-reverb
Version: 3.1.1
Release: 2%{?dist}
Summary: DragonFly reverberation plugin

License: GPLv2+
URL:     https://github.com/michaelwillis/dragonfly-reverb/

# git clone https://github.com/michaelwillis/dragonfly-reverb
# cd dragonfly-reverb
# git checkout 3.1.1
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz dragonfly-reverb.tar.gz dragonfly-reverb/*

Source0: dragonfly-reverb.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
A free hall-style reverb based on freeverb3 algorithms

%prep
%autosetup -n %{name}

%build

%make_build

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyHallReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyRoomReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyEarlyReflections.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyPlateReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst
%__install -m 755 -d %{buildroot}/%{_datadir}/pixmaps

cp bin/DragonflyHallReverb       %{buildroot}/%{_bindir}/
cp bin/DragonflyRoomReverb       %{buildroot}/%{_bindir}/
cp bin/DragonflyEarlyReflections %{buildroot}/%{_bindir}/
cp bin/DragonflyPlateReverb      %{buildroot}/%{_bindir}/

cp -r bin/DragonflyHallReverb.lv2/*       %{buildroot}/%{_libdir}/lv2/DragonflyHallReverb.lv2/
cp -r bin/DragonflyRoomReverb.lv2/*       %{buildroot}/%{_libdir}/lv2/DragonflyRoomReverb.lv2/
cp -r bin/DragonflyEarlyReflections.lv2/* %{buildroot}/%{_libdir}/lv2/DragonflyEarlyReflections.lv2/
cp -r bin/DragonflyPlateReverb.lv2/*      %{buildroot}/%{_libdir}/lv2/DragonflyPlateReverb.lv2/

cp bin/DragonflyHallReverb-vst.so       %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyRoomReverb-vst.so       %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyEarlyReflections-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyPlateReverb-vst.so      %{buildroot}/%{_libdir}/vst/

cp dragonfly-early-screenshot.png %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-hall-screenshot.png  %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-plate-screenshot.png %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-room-screenshot.png  %{buildroot}/%{_datadir}/pixmaps/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_datadir}/pixmaps/*

%changelog
* Sun Jun 14 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.1-2
- update to 3.1.1-2 - fix missing presets

* Wed Jun 10 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.1-1
- update to 3.1.1-1

* Sun Mar 1 2020 Yann Collette <ycollette.nospam@free.fr> - 3.0.0-1
- update to 3.0.0

* Mon Jun 24 2019 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0

* Sun Jan 20 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-1
- update to 1.1.4

* Thu Jan 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-1
- update to 1.1.2

* Tue Nov 13 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0

* Fri Oct 26 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-1
- update to 0.9.5

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.3-1
- update for Fedora 29
- update to 0.9.3

* Fri Oct 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- Initial build
