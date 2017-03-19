# Global variables for github repository
%global commit0 99202579699d9ca0a5e10cd8de9f9f039f736306
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           midimsg-lv2
Version:        1.0.0.%{shortcommit0}
Release:        1%{?dist}
Summary:        A collection of basic LV2 plugins to translate midi messages to usable values

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/blablack/midimsg-lv2
Source0:        https://github.com/blablack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel

%description
A collection of basic LV2 plugins to translate midi messages to usable values

%prep
%setup -qn %{name}-%{commit0}

%build

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
