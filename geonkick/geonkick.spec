# Global variables for github repository
%global commit0 ec3e1a0448c20ad644296685231fa8b70dbd4cbf
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    geonkick
Version: 1.5
Release: 1%{?dist}
Summary: Drum Software Synthesizer
URL:     https://github.com/quamplex/geonkick
Group:   Applications/Multimedia

License: GPLv2+

Source0: https://github.com/quamplex/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: rapidjson-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils

%description
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kick drums, snares, hit-hats, shakers, claps, steaks.

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/${CMAKE_INSTALL_PREFIX}\/lib/${CMAKE_INSTALL_PREFIX}\/%{_lib}/g" plugin/lv2/CMakeLists.txt

%build

mkdir build
cd build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_CXX_FLAGS="-I/usr/include/redkite" \
       -DCMAKE_C_FLAGS="-I/usr/include/redkite" \
       ..

make DESTDIR=%{buildroot}

%install

cd build

make DESTDIR=%{buildroot} install

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%doc AUTHORS ChangeLog COPYING* README.txt
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Mon May 20 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5-1
- initial version of the spec file
