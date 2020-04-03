# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 1e71c07a492f01022f9064560c95c2bcd938847c
%global gittag0 5.4.7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    JUCE
Version: 5.4.7.%{shortcommit0}
Release: 3%{?dist}
Summary: JUCE Framework
URL:     https://github.com/WeAreROLI/JUCE
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://github.com/WeAreROLI/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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

# Remove old compilation flags and use compilation flags from Fedora
sed -i -e "s/-march=native//g" Makefile
sed -i -e "s/-O3/-O0/g" Makefile

mkdir build
make %{?_smp_mflags} CONFIG=Release # CXXFLAGS="%{build_cxxflags}" 
cd ../extras

cd AudioPluginHost/Builds/LinuxMakefile/

sed -i -e "s/-march=native//g" Makefile
sed -i -e "s/-O3/-O0/g" Makefile
sed -i -e "s/#define JUCER_ENABLE_GPL_MODE 0/#define JUCER_ENABLE_GPL_MODE 1/g" ../../JuceLibraryCode/AppConfig.h


make %{?_smp_mflags} CONFIG=Release #CXXFLAGS="%{build_cxxflags}"
cd ../../..

cd BinaryBuilder/Builds/LinuxMakefile/

sed -i -e "s/-march=native//g" Makefile
sed -i -e "s/-O3/-O0/g" Makefile
sed -i -e "s/#define JUCER_ENABLE_GPL_MODE 0/#define JUCER_ENABLE_GPL_MODE 1/g" ../../JuceLibraryCode/AppConfig.h

make %{?_smp_mflags} CONFIG=Release #CXXFLAGS="%{build_cxxflags}"
cd ../../..

cd Projucer/Builds/LinuxMakefile/

sed -i -e "s/-march=native//g" Makefile
sed -i -e "s/-O3/-O0/g" Makefile
sed -i -e "s/#define JUCER_ENABLE_GPL_MODE 0/#define JUCER_ENABLE_GPL_MODE 1/g" ../../JuceLibraryCode/AppConfig.h

make  %{?_smp_mflags} CONFIG=Release #CXXFLAGS="%{build_cxxflags}"
cd ../../..

cd UnitTestRunner/Builds/LinuxMakefile/

sed -i -e "s/-march=native//g" Makefile
sed -i -e "s/-O3/-O0/g" Makefile
sed -i -e "s/#define JUCER_ENABLE_GPL_MODE 0/#define JUCER_ENABLE_GPL_MODE 1/g" ../../JuceLibraryCode/AppConfig.h

make %{?_smp_mflags} CONFIG=Release #CXXFLAGS="%{build_cxxflags}"
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
* Mon Feb 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.7-3
- update to 5.4.7

* Tue Feb 4 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.6-3
- update to 5.4.6

* Fri Oct 18 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.5-3
- update to 5.4.5

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.4-3
- update to 5.4.4

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.3-3
- Fixes for gcc 9

* Fri Feb 22 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.3-3
- Switch to 5.4.3

* Fri Feb 8 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.2-3
- Switch to 5.4.2

* Thu Dec 27 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-3
- activate GPL mode

* Wed Nov 21 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-2
- fix compilation flags

* Mon Nov 12 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-1
- initial specfile
