# Global variables for github repository
%global commit0 a8c25e63f5edb934daa6ba051a95daaae4c0abeb
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:         vopa-lv2
Version:      1.0.0
Release:      1%{?dist}
Summary:      A LV2 amplifier controlled via MIDI messages
URL:          https://github.com/ycollet/vopa
Source0:      https://github.com/ycollet/vopa/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel

%description
A LV2 amplifier controlled via MIDI messages

%prep
%setup -qn vopa-%{commit0}

%build

make INSTALLDIR=%{buildroot}/%{_libdir}/lv2/ %{?_smp_mflags}

%install 
make INSTALLDIR=%{buildroot}/%{_libdir}/lv2/ %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
