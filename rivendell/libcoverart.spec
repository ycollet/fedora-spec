# Global variables for github repository
%global commit0 86c3d8ce8c706ea6184e792459b55a57839c34e8
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: A library for accessing the MusicBrainz Cover Art Archive
Name:    libcoverart
Version: 1.0.0
Release: 1%{?dist}
License: LGPL
Group:   Applications/Multimedia
URL:     https://github.com/metabrainz/libcoverart

Source0: https://github.com/metabrainz//%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: neon-devel
BuildRequires: jansson-devel
BuildRequires: libxml2-devel

%description
A library for accessing the MusicBrainz Cover Art Archive

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/\*\.inc//g" src/CMakeLists.txt

%build

mkdir build
cd build

%cmake -DCMAKE_BUILD_TYPE=RELEASE ..

%{__make} DESTDIR=%{buildroot} %{?_smp_mflags}

%install

cd build
%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc INSTALL.txt NEWS.txt README.md
%license COPYING.txt
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Sat May 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial release of the spec file
