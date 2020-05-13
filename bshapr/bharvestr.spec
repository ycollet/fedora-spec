# Global variables for github repository
%global commit0 ffd310a794e899eb863ab3a1d9ce672c540503f7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: B.Harvestr is an experimental granular synthesizer LV2 plugin
Name:    lv2-BHarvestr
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sjaehn/BHarvestr

Source0: https://github.com/sjaehn/BHarvestr/archive/%{commit0}.tar.gz#/BHarvestr-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
B.Harvestr is an experimental granular synthesizer LV2 plugin.

Warning: B.Harvestr is in an early stage of development.
Not for production use! No guarantees! Some essential features are not (fully) implemented yet.
Major changes in the plugin definition need to be expected.
Therefore, future versions of this plugin may be completely incompatible to this version.

%prep
%setup -qn BHarvestr-%{commit0}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install
%{__rm} -rf %{buildroot}
make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC" install

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
%{_libdir}/lv2/*

%changelog
* Wed May 13 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release of the spec file
