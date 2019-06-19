# Global variables for github repository
%global commit0 19e01dcaf1afda031143ae171d8eeadd0c49fee1
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    nanomsg
Version: 1.1.2
Release: 1%{?dist}
Summary: The nanomsg library is a simple high-performance implementation of several "scalability protocols"
URL:     https://github.com/nanomsg/nanomsg
Source0: https://github.com/nanomsg/nanomsg/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:   Applications/Multimedia
License: GPLv2+

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
The nanomsg library is a simple high-performance implementation of several "scalability protocols". These scalability protocols are light-weight messaging protocols which can be used to solve a number of very common messaging patterns, such as request/reply, publish/subscribe, surveyor/respondent, and so forth. These protocols can run over a variety of transports such as TCP, UNIX sockets, and even WebSocket.
For more information check the http://nanomsg.org.

%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}

%build

%cmake -DNN_ENABLE_DOC=OFF -DNN_TESTS=OFF .
make VERBOSE=1 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} install

%files
%{_bindir}/*
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.2
- update for Fedora 29

* Sat May 12 2017 Yann Collette <ycollette.nospam@free.fr> - 1.1.2
- update to 1.1.2

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
