# Global variables for github repository
%global commit0 6bcd263ef366044f193373bc0ad5188c916e4f6c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    ryukau
Version: 0.0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Some audio plugins (LV2 and VST) from ruykau

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/ryukau/LV2Plugins/

# git clone --recursive https://github.com/ryukau/LV2Plugins/
# cd LV2Plugins
# find . -name .git -exec rm -rf {} \;
# cd ..
# mv LV2Plugins ryukau
# tar cvfz ryukay.tar.gz ryukau/*

Source0: ryukau.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
Some audio plugins (LV2 and VST) from ruykau

%prep
%setup -qn %{name}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/EnvelopedSine.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/EsPhaser.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/FDNCymbal.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/IterativeSinCluster.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/SevenDelay.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/SyncSawSynth.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/TrapezoidSynth.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/WaveCymbal.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/EnvelopedSine %{buildroot}/%{_bindir}/
cp bin/EsPhaser %{buildroot}/%{_bindir}/
cp bin/FDNCymbal %{buildroot}/%{_bindir}/
cp bin/IterativeSinCluster %{buildroot}/%{_bindir}/
cp bin/SevenDelay %{buildroot}/%{_bindir}/
cp bin/SyncSawSynth %{buildroot}/%{_bindir}/
cp bin/TrapezoidSynth %{buildroot}/%{_bindir}/
cp bin/WaveCymbal %{buildroot}/%{_bindir}/

cp -r bin/EnvelopedSine.lv2/* %{buildroot}/%{_libdir}/lv2/EnvelopedSine.lv2/
cp -r bin/EsPhaser.lv2/* %{buildroot}/%{_libdir}/lv2/EsPhaser.lv2/
cp -r bin/FDNCymbal.lv2/* %{buildroot}/%{_libdir}/lv2/FDNCymbal.lv2/
cp -r bin/IterativeSinCluster.lv2/* %{buildroot}/%{_libdir}/lv2/IterativeSinCluster.lv2/
cp -r bin/SevenDelay.lv2/* %{buildroot}/%{_libdir}/lv2/SevenDelay.lv2/
cp -r bin/SyncSawSynth.lv2/* %{buildroot}/%{_libdir}/lv2/SyncSawSynth.lv2/
cp -r bin/TrapezoidSynth.lv2/* %{buildroot}/%{_libdir}/lv2/TrapezoidSynth.lv2/
cp -r bin/WaveCymbal.lv2/* %{buildroot}/%{_libdir}/lv2/WaveCymbal.lv2/

cp bin/EnvelopedSine-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/EsPhaser-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/FDNCymbal-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/IterativeSinCluster-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/SevenDelay-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/SyncSawSynth-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/TrapezoidSynth-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/WaveCymbal-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Wed Feb 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6bcd263e-1
- Initial spec file for 6bcd263e
