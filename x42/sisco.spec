# Global variables for github repository
%global commit0 62d537d3c6055e1ad7abb3c3987f8dd864e387ff
%global gittag0 v0.6.7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           sisco.lv2
Version:        0.6.7
Release:        1%{?dist}
Summary:        A LV2 oscilloscope

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/x42/sisco.lv2

BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A LV2 oscilloscope

%prep

[ ! -d build-sisco.lv2 ] && git clone https://github.com/x42/sisco.lv2.git build-sisco.lv2

%build
cd build-sisco.lv2
git checkout v0.6.7
make submodules
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} sisco_VERSION=%{version} %{?_smp_mflags}

%install 
cd build-sisco.lv2
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} sisco_VERSION=%{version} %{?_smp_mflags} install

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.6.7
- Initial build
