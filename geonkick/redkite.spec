# Global variables for github repository
%global commit0 ad49c9182d9d7c1ed25e0319c0e48935b22b0774
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    redkite
Version: 0.6.1
Release: 1%{?dist}
Summary: A cross-platform GUI toolkit in C++.
URL:     https://github.com/quamplex/redkite
Group:   Applications/Multimedia
License: GPLv2+

Source0: https://github.com/quamplex/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: cmake

%description
Redkite is a small free software and cross-platform GUI toolkit. It is developed in C++11&14 and inspired from other well known GUI toolkits.

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/${CMAKE_INSTALL_PREFIX}\/lib/${CMAKE_INSTALL_PREFIX}\/%{_lib}/g" CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_BUILD_TYPE=RELEASE \
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
* Thu Aug 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1
* Mon May 27 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- switch to 0.5.2
* Tue May 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- switch to 0.5.1
* Mon May 20 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- initial version of the spec file
