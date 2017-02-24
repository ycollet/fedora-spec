# Global variables for github repository
%global commit0 81189de710103f1479a45460a54fadba356f9ca4
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         synthpod
Version:      0.1.0
Release:      1%{?dist}
Summary:      Lightweight Nonlinear LV2 Plugin Container
URL:          https://github.com/OpenMusicKontrollers/synthpod
Source0:      https://github.com/OpenMusicKontrollers/synthpod/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: sratom-devel
BuildRequires: efl-devel
BuildRequires: elementary-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake

%description
Lightweight Nonlinear LV2 Plugin Container

%prep
%setup -qn %{name}-%{commit0}

%build

%ifarch x86_64 amd64 ia32e
sed -i "s/lib\/synthpod/lib64\/synthpod/g" CMakeLists.txt
sed -i "s/lib\/lv2/lib64\/lv2/g" CMakeLists.txt
sed -i "s/DESTINATION lib/DESTINATION lib64/g" app/CMakeLists.txt
sed -i "s/DESTINATION lib/DESTINATION lib64/g" ui/CMakeLists.txt
%endif

%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0
- Initial build
