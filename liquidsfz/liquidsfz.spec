Name:    liquidsfz
Version: 0.2.1
Release: 1%{?dist}
License: BSD-2-Clause
Summary: Sampler plugin and library for SFZ and Hydrogen instruments
Url:     https://github.com/swesterfeld/liquidsfz

Source0: https://github.com/swesterfeld/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires: jack-audio-connection-kit

BuildRequires: gcc gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel
BuildRequires: readline-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: chrpath

%description
liquidsfz is a free and open source sampler that can load and play .sfz files.
It can also load and play Hydrogen drumkits. We support JACK and LV2.

%package devel
Summary:  Header files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
Header files for the %{name} library.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

sh autogen.sh

%configure

%make_build

%install

%make_install

chrpath --delete %{buildroot}/%{_libdir}/lv2/liquidsfz.lv2/liquidsfz_lv2.so

%files
%doc README.md NEWS OPCODES.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*

%files devel
%{_libdir}/libliquidsfz.la
%{_libdir}/libliquidsfz.a
%{_includedir}/liquidsfz.hh
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/liquidsfz.pc

%changelog
* Wed Oct 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- initial release of the spec file
