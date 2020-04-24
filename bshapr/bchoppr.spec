# Global variables for github repository
%global commit0 27d55205c271bdee1f57455ae52e3d0171684a46
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: An audio stream chopping LV2 plugin
Name:    lv2-BChoppr
Version: 1.4.0
Release: 2%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sjaehn/BChoppr

Source0: https://github.com/sjaehn/BChoppr/archive/%{commit0}.tar.gz#/BChoppr-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
BChoppr cuts the audio input stream into a repeated sequence of up to 16 chops.
Each chop can be leveled up or down (gating). BChoppr is the successor of BSlizr

%prep
%setup -qn BChoppr-%{commit0}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install
%{__rm} -rf %{buildroot}
make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC" install

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
%{_libdir}/lv2/*

%changelog
* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- initial release 
