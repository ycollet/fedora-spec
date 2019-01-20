# Global variables for github repository
%global commit0 c61b6690a892c503f3341db767a7d74b56970e29
%global gittag0 1.1.4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    dragonfly-reverb
Version: 1.1.4
Release: 1%{?dist}
Summary: DragonFly reverberation plugin

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/michaelwillis/dragonfly-reverb/

# git clone https://github.com/michaelwillis/dragonfly-reverb/
# cd dragonfly-reverb
# git checkout 1.1.4
# git submodule init
# git submodule update
# rm -rf .git dpf/.git
# cd ..
# tar cvfz dragonfly-reverb.tar.gz dragonfly-reverb/*

Source0: dragonfly-reverb.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

%description
A free hall-style reverb based on freeverb3 algorithms

%prep
%setup -qn %{name}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyReverb.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/DragonflyReverb %{buildroot}/%{_bindir}/
cp -r bin/DragonflyReverb.lv2/* %{buildroot}/%{_libdir}/lv2/DragonflyReverb.lv2/
cp bin/DragonflyReverb-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
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
