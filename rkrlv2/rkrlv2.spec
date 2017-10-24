# Global variables for github repository
%global commit0 bf4eca3115858246764d2294f34c73fe4082d040
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           rkrlv2
Version:        0.0.1.%{shortcommit0}
Release:        1%{?dist}
Summary:        Rakarrack LV2 plugins
URL:            https://github.com/ssj71/rkrlv2
Group:          Applications/Multimedia

License:        GPLv2+

# original tarfile can be found here:
Source0:        https://github.com/ssj71/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Patch0:         rkrlv2-0001-custom-install-path.patch

BuildRequires: lv2-devel
BuildRequires: libsamplerate-devel
BuildRequires: fftw-devel
BuildRequires: cmake

%description
This project is the rakarrack effects ported to LV2 plugins.
The ports are done such that hopefully when rakarrack gets
an active maintainer these will get merged into the original

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1 

%build
%cmake -DLV2_INSTALL_DIR:PATH=%{_libdir}/lv2/rkr.lv2 .

make VERBOSE=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%{_libdir}/lv2/*
%{_datadir}/rkr.lv2/*

%changelog
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.0.1
- update master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1
- Initial build
