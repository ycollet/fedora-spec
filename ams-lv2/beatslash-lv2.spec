# Global variables for github repository
%global commit0 45044ce015c7a79b93a88aba1f0c19e2c00206d8
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           beatslash-lv2
Version:        1.0.0.%{shortcommit0}
Release:        1%{?dist}
Summary:        beatslash-lv2 is a set of LV2 plugins to mangle, slash, repeat and do much more with your beats

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/blablack/beatslash-lv2
Source0:        https://github.com/blablack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: gtkmm24-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: lvtk

%description
beatslash-lv2 is a set of LV2 plugins to mangle, slash, repeat and do much more with your beats. They are meant to be used live, but it is up to your imagination what to do!

The set contains:
 * Beat Repeater
 * Beat Slicer

%prep
%setup -qn %{name}-%{commit0}

%build

sed -i -e "s/lvtk-plugin-1/lvtk-plugin-2/g" wscript
sed -i -e "s/lvtk-ui-1/lvtk-ui-2/g" wscript
sed -i -e "s/lvtk-gtkui-1/lvtk-gtkui-2/g" wscript

for Files in src/*.cpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done
for Files in src/*.hpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
