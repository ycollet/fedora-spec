# Global variables for github repository
%global commit0 f11e5f9eb057c9e92300a73c1c49e6fedcacfe2c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    redkite
Version: 0.8.1
Release: 1%{?dist}
Summary: A cross-platform GUI toolkit in C++.
URL:     https://gitlab.com/geontime/redkite
Group:   Applications/Multimedia
License: GPLv2+

Source0: https://gitlab.com/geontime/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: cmake

%description
Redkite is a small free software and cross-platform GUI toolkit. It is developed in C++11&14 and inspired from other well known GUI toolkits.

%prep
%setup -qn %{name}-v%{version}

sed -i -e "s/${CMAKE_INSTALL_PREFIX}\/lib/${CMAKE_INSTALL_PREFIX}\/%{_lib}/g" CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

%files
%doc LICENSE README.md
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*

%changelog
* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Sat Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0

* Sat Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3

* Wed Oct 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to 0.6.2

* Thu Aug 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1

* Mon May 27 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- switch to 0.5.2

* Tue May 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- switch to 0.5.1

* Mon May 20 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- initial version of the spec file
