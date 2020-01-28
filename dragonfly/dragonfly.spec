# Global variables for github repository
%global commit0 b0832a377b9aaf3f3aabce57b9cbee03eac8c597
%global gittag0 2.0.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    dragonfly-reverb
Version: 2.0.0
Release: 1%{?dist}
Summary: DragonFly reverberation plugin

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/michaelwillis/dragonfly-reverb/

# git clone https://github.com/michaelwillis/dragonfly-reverb/
# cd dragonfly-reverb
# git checkout 2.0.0
# git submodule init
# git submodule update
# rm -rf .git dpf/.git
# cd ..
# tar cvfz dragonfly-reverb.tar.gz dragonfly-reverb/*

Source0: dragonfly-reverb.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
A free hall-style reverb based on freeverb3 algorithms

%prep
%setup -qn %{name}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyHallReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyRoomReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/DragonflyHallReverb %{buildroot}/%{_bindir}/
cp bin/DragonflyRoomReverb %{buildroot}/%{_bindir}/
cp -r bin/DragonflyHallReverb.lv2/* %{buildroot}/%{_libdir}/lv2/DragonflyHallReverb.lv2/
cp -r bin/DragonflyRoomReverb.lv2/* %{buildroot}/%{_libdir}/lv2/DragonflyRoomReverb.lv2/
cp bin/DragonflyHallReverb-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyRoomReverb-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
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
