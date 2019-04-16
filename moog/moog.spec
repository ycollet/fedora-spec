# Global variables for github repository
%global commit0 a2d43931ae58561fff2c22d0885f54ebebab36d0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    raffosynth
Version: 0.1.0
Release: 1%{?dist}
Summary: This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.

Group:   Applications/Multimedia
License: GPLv3+
URL:     https://github.com/nicoroulet/moog
Source0: https://github.com/nicoroulet/moog/archive/%{commit0}.tar.gz#/moog-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: lv2-c++-tools-devel

%description
This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.

%package -n lv2-%{name}
Summary: This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.
Group:   Applications/Multimedia

%description -n lv2-%{name}
This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.

%prep
%setup -qn moog-%{commit0}

%build

make INSTALL_DIR=%{buildroot}/usr/%{_lib}/lv2/ %{?_smp_mflags}

%install

rm -rf %{buildroot}
make INSTALL_DIR=%{buildroot}/usr/%{_lib}/lv2/ install

%clean
rm -rf %{buildroot}

%files -n lv2-%{name}
%doc README.md LICENSE.md
%{_libdir}/lv2/*

%changelog
* Tue Apr 16 2019 Yann Collette <ycollette dot nospam at free dot fr> - 0.1.0-1
- Initial version of the spec file

