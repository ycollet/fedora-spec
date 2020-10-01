Summary: A library for accessing the MusicBrainz Cover Art Archive
Name:    libcoverart
Version: 1.0.0
Release: 2%{?dist}
License: LGPL
URL:     https://github.com/metabrainz/libcoverart

Source0: https://github.com/metabrainz/libcoverart/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
%autosetup -n %{name}-release-%{version}

sed -i -e "s/\*\.inc//g" src/CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build 

%install

%cmake_install

%files
%defattr(-, root, root)
%doc INSTALL.txt NEWS.txt README.md
%license COPYING.txt
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- fix for fedora 33

* Sat May 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial release of the spec file
