# Global variables for github repository
%global commit0 07f3ba739e3eef8cbade8fbd1c5bda2d215aa475
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:         lomse
Version:      0.19.0.%{shortcommit0}
Release:      1%{?dist}
Summary:      A free open source library for rendering music scores
Group:        Applications/Multimedia
License:      GPLv2+

URL:          https://github.com/lenmus/lomse
Source0:      https://github.com/lenmus/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:       lomse_0001-fix-install.patch

BuildRequires: boost-devel
BuildRequires: zlib-devel 
BuildRequires: libpng-devel
BuildRequires: freetype-devel
BuildRequires: cmake

%description
Lomse objective is provide software developers with a library to add capabilities to any program for rendering, editing and playing back music scores. It is written in C++ and it is free open source and platform independent. Lomse stands for "LenMus Open Music Score Edition Library".

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -qn %{name}-%{commit0}
%patch0 -p1

%build

%cmake -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DWANT_SHARED:BOOL=ON \
       -DLIBDIR=%{_lib} \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

%files
%doc AUTHORS.md CHANGELOG.md README.md NEWS THANKS LICENSE CONTRIBUTING.md
%{_libdir}/*
%{_datadir}/%{name}/fonts/*

%files devel
%{_includedir}/*

%changelog
* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.19.0-1
- Initial version
