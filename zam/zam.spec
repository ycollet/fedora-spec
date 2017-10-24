# Global variables for github repository
%global commit0 3501810d403fdf5c35031dc3ac65ad56c13a8d2a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           zam-plugins
Version:        3.9
Release:        1%{?dist}
Summary:        Zam LV2 set of plugins

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/zamaudio/zam-plugins
# in the zam repository -> make dist
Source0:        zam-plugins-%{version}.tar.xz

BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

%description
Zam LV2 set of plugins

%package -n ladspa-zam
Summary:        Zam LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-zam
Zam LADSPA plugin

%package -n vst-zam
Summary:        Zam VST plugin
Group:          Applications/Multimedia

%description -n vst-zam
Zam VST plugin

%prep
%setup -qn %{name}-%{version}

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install 
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} install

%files
%{_bindir}/*
%{_libdir}/lv2/*

%files -n ladspa-zam
%{_libdir}/ladspa/* 

%files -n vst-zam
%{_libdir}/vst/* 

%changelog
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.9
- update version to 3.9

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build
