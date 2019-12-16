# Global variables for github repository
%global commit0 b20d67550864df05c8969ad689f4ec465e6efbcc
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    lv2-screcord-plugin
Version: 0.2
Release: 2%{?dist}
Summary: A simple Lv2 capture plugin

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/brummer10/screcord.lv2
Source0: screcord.lv2.tar.gz

# git clone https://github.com/brummer10/screcord.lv2
# cd screcord.lv2
# git checkout v0.2
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz screcord.lv2.tar.gz screcord.lv2/*

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: cairo-devel

%description
A simple Lv2 capture plugin

%prep
%setup -qn screcord.lv2

%build

cd Xputty
make
cd ..
make INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 install

%files
%{_libdir}/lv2/sc_record.lv2/*

%changelog
* Mon Dec 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.2-2
- update to 0.2-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to latest master

* Tue Nov 21 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
