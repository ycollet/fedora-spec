# Global variables for github repository
%global commit0 7b7e08b047eca476e71d1d037f4b72c976fe5475
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         midi_matrix.lv2
Version:      0.18.0
Release:      1%{?dist}
Summary:      A LV2 Plugin Bundle
URL:          https://github.com/OpenMusicKontrollers/midi_matrix.lv2
Source0:      https://github.com/OpenMusicKontrollers/midi_matrix.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: cmake

%description
A LV2 Plugin Bundle

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DPLUGIN_DEST:Path=%{_lib}/lv2/midi_matrix.lv2 .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.18.0
- Initial build
