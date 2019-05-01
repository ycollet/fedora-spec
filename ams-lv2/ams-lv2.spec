%global debug_package %{nil}

# Global variables for github repository
%global commit0 0f60ee0a0e6df64877210dfee2d30f126dc3137f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    ams-lv2
Version: 1.2.1.%{shortcommit0}
Release: 1%{?dist}
Summary: AMS LV2 set of plugins (from Alsa Modular Synth)

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/blablack/ams-lv2
Source0: https://github.com/blablack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtkmm24-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: lvtk
BuildRequires: fftw-devel

%description
AMS LV2 set of plugins synth (from Alsa Modular Synth)

%prep
%setup -qn %{name}-%{commit0}

%build

sed -i -e "s/lvtk-plugin-1/lvtk-plugin-2/g" wscript
sed -i -e "s/lvtk-ui-1/lvtk-ui-2/g" wscript
sed -i -e "s/lvtk-gtkui-1/lvtk-gtkui-2/g" wscript

for Files in src/*.cpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done
for Files in src/*.hpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

find . -type f -exec sed -i -e "s/env python/env python2/g" {} \;

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.2.1
- Initial build
