%global debug_package %{nil}

# Global variables for github repository
%global commit0 31047741ba71948d7099406cdc5cb2a6a9d655cc
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    deteriorate-lv2
Version: 1.0.6.%{shortcommit0}
Release: 1%{?dist}
Summary: deteriorate-lv2 is a set of plugins to destroy and deteriorate the sound quality of a live input

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/blablack/deteriorate-lv2
Source0: https://github.com/blablack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: gtkmm24-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: lvtk
BuildRequires: sed

%description
deteriorate-lv2 is a set of plugins to destroy and deteriorate the sound quality of a live input. The set contains:
 * DownSampler
 * Granulator

%prep
%setup -qn %{name}-%{commit0}

%build

sed -i -e "s/lvtk-plugin-1/lvtk-plugin-2/g" wscript
sed -i -e "s/lvtk-ui-1/lvtk-ui-2/g" wscript
sed -i -e "s/lvtk-gtkui-1/lvtk-gtkui-2/g" wscript

# For Fedora 29
%if 0%{?fedora} >= 29
  for Files in `grep -lr "/usr/bin/env.*python"`; do sed -ie "s/env python/python2/g" $Files; done
%endif

for Files in src/*.cpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done
for Files in src/*.hpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.6
- update for Fedora 29

* Mon Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.6

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
