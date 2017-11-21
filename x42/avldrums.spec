# Global variables for github repository
%global commit0 43164765ba94d850a348f0f15ea4b9ee05ec2de7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

# git clone https://github.com/x42/avldrums.lv2.git
# mv avldrums.lv2 avldrums.lv2.43164765ba94d850a348f0f15ea4b9ee05ec2de7
# cd avldrums.lv2.43164765ba94d850a348f0f15ea4b9ee05ec2de7
# git submodule init
# git submodule update
# cd ..
# tar cvfz avldrums.lv2.43164765ba94d850a348f0f15ea4b9ee05ec2de7.tar.gz avldrums.lv2.43164765ba94d850a348f0f15ea4b9ee05ec2de7

Name:           lv2-avldrums-x42-plugin
Version:        0.2.2.%{shortcommit0}
Release:        1%{?dist}
Summary:        LV2 Analogue simulation of a tube preamp

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/brummer10/GxPlugins.lv2
Source0:        avldrums.lv2.43164765ba94d850a348f0f15ea4b9ee05ec2de7.tar.gz

BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
avldrums.lv2 is a simple Drum Sample Player Plugin, dedicated to the http://www.bandshed.net/avldrumkits/

%prep
%setup -qn avldrums.lv2.43164765ba94d850a348f0f15ea4b9ee05ec2de7

%build

%make_build PREFIX=%{buildroot}%{_usr} LV2DIR=%{buildroot}%{_libdir}/lv2

%install 

make submodules
make PREFIX=%{buildroot}%{_usr} LV2DIR=%{buildroot}%{_libdir}/lv2 install

%files
%{_libdir}/lv2/avldrums.lv2/*

%changelog
* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.2.2
- Initial build
