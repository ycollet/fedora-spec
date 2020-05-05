# Global variables for github repository
%global commit0 73dda97e27bd6113bdd525bcdaa92278ae98bce0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    sequencer64
Version: 0.96.7
Release: 1%{?dist}
Summary: MIDI sequencer

License: GPL
URL:     https://github.com/ahlstromcj/sequencer64
Source0: https://github.com/ahlstromcj/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: lash-devel
BuildRequires: rtmidi-devel
BuildRequires: git
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig

%description
Sequencer64 is a reboot of seq24, extending it with many new features.
The heart of seq24 remains intact.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}

%build

sh autogen.sh

%configure
%make_build

%install

rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc ChangeLog INSTALL NEWS README README.jack VERSION TODO
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%files devel
%{_includedir}/*

%changelog
* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.7-1
- update to 0.96.7-1

* Mon Nov 19 2018 L.L.Robinson <baggypants@fedoraproject.org> - 0.96.1-1
- initial version
