# Global variables for github repository
%global commit0 4461547c300896690eb9dd809f7d0aaf648da11c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    VL1-emulator
Version: 1.1.0.0
Release: 1%{?dist}
Summary: An emulator of Casio VL-Tone VL1

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/linuxmao-org/VL1-emulator

# git clone https://github.com/linuxmao-org/VL1-emulator
# cd VL1-emulator
# git checkout 1.1.0.0
# git submodule init
# git submodule update
# rm -rf .git dpf/.git
# cd ..
# tar cvfz VL1-emulator.tar.gz VL1-emulator/*

Source0: VL1-emulator.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: cairo-devel

%description
An emulator of Casio VL-Tone VL1, based on source code by PolyValens

%prep
%setup -qn %{name}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install

make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/vl1.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/vl1 %{buildroot}/%{_bindir}/
cp -r bin/vl1.lv2/* %{buildroot}/%{_libdir}/lv2/vl1.lv2/
cp bin/vl1-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Thu Jan 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0.0-1
- Initial build
