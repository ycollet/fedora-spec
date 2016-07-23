# Global variables for github repository
%global commit0 a593de0836790a3437b861cf0eb7acd1b581e512
%global gittag0 lv2unstable
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           drmr
Version:        1.0.0.%{shortcommit0}
Release:        1%{?dist}
Summary:        A drum LV2 plugin

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/falkTX/drmr
Source0:        https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gtk2-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel
BuildRequires: expat-devel
BuildRequires: cmake

%description
A drum LV2 plugin

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DLV2_INSTALL_DIR:Path=%{_lib}/lv2 .

make VERBOSE=1 %{?_smp_mflags}

%install
make VERBOSE=1 DESTDIR=%{buildroot} %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
