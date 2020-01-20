# Global variables for github repository
%global commit0 a767a9eea4e543061993290168a321d10c08b03c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Summary: A sample slicer audio plugin
Name:    ninjas2
Version: 0.2.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/rghvdberg/ninjas2

# git clone https://github.com/rghvdberg/ninjas2
# cd ninjas2
# git checkout v0.2.0
# git submodule init
# git submodule update
# rm -rf .git dpf/.git
# cd ..
# tar cvfz ninjas2.tar.gz ninjas2/*

Source0: ninjas2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel

%description
A sample slicer audio plugin

%prep
%setup -qn %{name}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%{__rm} -rf %{buildroot}

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/ninjas2.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/ninjas2 %{buildroot}/%{_bindir}/
cp -r bin/ninjas2.lv2/* %{buildroot}/%{_libdir}/lv2/ninjas2.lv2/
cp bin/ninjas2-vst.so %{buildroot}/%{_libdir}/vst/

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Mon Jan 20 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial release 
