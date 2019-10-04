# Disable production of debug package. Problem with fedora 23
# %global debug_package %{nil}

# Global variables for github repository
%global commit0 5f378860bf9a0f6864f1b191377905008d85e587
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    osc2midi
Version: 1.0.0.%{shortcommit0}
Release: 1%{?dist}
Summary: OSC2MIDI is a highly configurable OSC to jack MIDI (and back).
URL:     https://github.com/ssj71/OSC2MIDI
Group:   Applications/Multimedia

License: GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

Source0: https://github.com/ssj71/OSC2MIDI/archive/%{commit0}.tar.gz#/OSC2MIDI-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
OSC2MIDI is a highly configurable OSC to jack MIDI (and back). It was designed especially for use on linux desktop
and the open source Android app called "Control (OSC+MIDI)" but was deliberately written to be flexible enough
to be used with any OSC controller or target.

%prep
%setup -qn OSC2MIDI-%{commit0}

sed -i -e "s/CMAKE_C_FLAGS \"/CMAKE_C_FLAGS \"-fPIC /g" src/CMakeLists.txt

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_C_FLAGS=-fPIC \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Oct 4 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial spec file
