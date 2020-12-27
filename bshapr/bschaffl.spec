Summary: Pattern-controlled MIDI amp & time stretch LV2 plugin to produce shuffle / swing effects
Name:    lv2-BSchaffl
Version: 1.2.2
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BSchaffl

Source0: https://github.com/sjaehn/BSchaffl/archive/%{version}.tar.gz#/BSchaffl-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Pattern-controlled MIDI amp & time stretch LV2 plugin to produce shuffle / swing effects

%prep
%autosetup -n BSchaffl-%{version}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Dec 27 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-1
- update to 1.2.2-1

* Sun Aug 23 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- update to 1.2.0-1

* Fri Jul 24 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- update to 0.2.0-1

* Mon May 25 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release 
