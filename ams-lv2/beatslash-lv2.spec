# Global variables for github repository
%global commit0 5886aeb3779a37a5e4ab0b6c715216c22aae4e63
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    beatslash-lv2
Version: 1.0.6.%{shortcommit0}
Release: 3%{?dist}
Summary: beatslash-lv2 is a set of LV2 plugins to mangle, slash, repeat and do much more with your beats
License: GPLv2+
URL:     https://github.com/blablack/beatslash-lv2

Source0: https://github.com/blablack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: gtkmm24-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: lvtk
BuildRequires: sed
BuildRequires: python2

%description
beatslash-lv2 is a set of LV2 plugins to mangle, slash, repeat and do much more with your beats. They are meant to be used live, but it is up to your imagination what to do!

The set contains:
 * Beat Repeater
 * Beat Slicer

%prep
%autosetup -n %{name}-%{commit0}

%build

sed -i -e "s/lvtk-plugin-1/lvtk-plugin-2/g" wscript
sed -i -e "s/lvtk-ui-1/lvtk-ui-2/g" wscript
sed -i -e "s/lvtk-gtkui-1/lvtk-gtkui-2/g" wscript

for Files in src/*.cpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done
for Files in src/*.hpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

# For Fedora 29
%if 0%{?fedora} >= 29
  for Files in `grep -lr "/usr/bin/env.*python"`; do sed -ie "s/env python/python2/g" $Files; done
%endif

%set_build_flags

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%doc README.md THANKS
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-3
- update to 1.0.6-3 - fix debug build

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-2
- update to 1.0.6-2

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-1
- update to 1.0.6-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.5-1
- update for Fedora 29

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.5-1

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
