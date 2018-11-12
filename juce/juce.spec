# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 baf78b1e5f6e02ade4f209d7f45a60e43f9b53cd
%global gittag0 5.4.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    JUCE
Version: 5.4.1.%{shortcommit0}
Release: 1%{?dist}
Summary: JUCE Framework
URL:     https://github.com/WeAreROLI/JUCE.git
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://github.com/WeAreROLI/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: ladspa-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: python2
BuildRequires: webkit2gtk3-devel
BuildRequires: sed
BuildRequires: libcurl-devel

%description
JUCE is an open-source cross-platform C++ application framework used for rapidly
developing high quality desktop and mobile applications, including VST, AU (and AUv3),
RTAS and AAX audio plug-ins. JUCE can be easily integrated with existing projects or can
be used as a project generation tool via the [Projucer](https://juce.com/discover/projucer),
which supports exporting projects for Xcode (macOS and iOS), Visual Studio, Android Studio,
Code::Blocks, CLion and Linux Makefiles as well as containing a source code editor and
live-coding engine which can be used for rapid prototyping.

%prep
%setup -qn %{name}-%{commit0}

%build

cd doxygen
sed -i -e "s/python/python2/g" Makefile

make CONFIG=Release
cd ../extras

cd AudioPluginHost/Builds/LinuxMakefile/
make CONFIG=Release
cd ../../..

cd BinaryBuilder/Builds/LinuxMakefile/
make CONFIG=Release
cd ../../..

cd Projucer/Builds/LinuxMakefile/
make CONFIG=Release
cd ../../..

cd UnitTestRunner/Builds/LinuxMakefile/
make CONFIG=Release
cd ../../..

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 extras/AudioPluginHost/Builds/LinuxMakefile/build/AudioPluginHost %{buildroot}%{_bindir}/
%__install -m 755 extras/BinaryBuilder/Builds/LinuxMakefile/build/BinaryBuilder     %{buildroot}%{_bindir}/
%__install -m 755 extras/Projucer/Builds/LinuxMakefile/build/Projucer               %{buildroot}%{_bindir}/
%__install -m 755 extras/UnitTestRunner/Builds/LinuxMakefile/build/UnitTestRunner   %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE/
%__install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE/examples/
cp -ra examples/*    %{buildroot}/%{_usrsrc}/JUCE/examples/
%__install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE/modules/
cp -ra modules/*     %{buildroot}/%{_usrsrc}/JUCE/modules/

%__install -m 755 -d %{buildroot}/%{_datadir}/JUCE/doc/
cp -ra doxygen/doc/* %{buildroot}/%{_datadir}/JUCE/doc/

%files
%doc README.md LICENSE.md 
%{_bindir}/*
%{_datadir}/*
%{_usrsrc}/*

%changelog
* Mon Nov 12 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-1
- initial specfile
