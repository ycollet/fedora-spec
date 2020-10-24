%global debug_package %{nil}

# Global variables for github repository
%global commit0 bd94faa32539ba4228ad8ccfa00dcc35ab17c4fb
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    odin2
Version: 2.2.4
Release: 1%{?dist}
Summary: A VST3 synthetizer
License: GPLv2+
URL:     https://github.com/TheWaveWarden/odin2

Source0: https://github.com/TheWaveWarden/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  odin2-0001-soundbanks-in-share.patch

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: cmake
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: rsync
BuildRequires: python2
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE == 6.0.1

%description
A VST3 synthetizer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%set_build_flags

Projucer --resave Odin.jucer

export HOME=`pwd`
mkdir -p .vst3
mkdir -p .lv2
mkdir -p .local/share/Surge


cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true

%install 

%__install -m 755 -d %{buildroot}%{_libdir}/vst3/
%__install -m 755 -d %{buildroot}%{_bindir}/
%__install -m 755 -d %{buildroot}%{_datadir}/odin2/Soundbanks/

cp -r Soundbanks/* %{buildroot}%{_datadir}/odin2/Soundbanks/
rm %{buildroot}%{_datadir}/odin2/Soundbanks/User\ Patches/.gitignore 

%__install -m 644 -p Builds/LinuxMakefile/build/Odin2 %{buildroot}/%{_bindir}/
%__install -m 644 -p Builds/LinuxMakefile/build/Odin2.vst3/Contents/x86_64-linux/Odin2.so %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md change_log.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.4-1
- Initial spec file
