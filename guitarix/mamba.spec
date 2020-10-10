Name:    mamba
Version: 1.6.0
Release: 1%{?dist}
Summary: Virtual Midi Keyboard for Jack Audio Connection Kit
License: GPLv2+

URL:     https://github.com/brummer10/Mamba

# ./mamba_source.sh v1.6

Source0: Mamba.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: libsmf-devel
BuildRequires: fluidsynth-devel
BuildRequires: alsa-lib-devel

%description
Virtual Midi Keyboard for Jack Audio Connection Kit

%prep
%autosetup -n Mamba

%build

%set_build_flags

%make_build CXXFLAGS="%build_cxxflags -I/usr/include/cairo -I/usr/include/sigc++-2.0/ -I/usr/%{_lib}/sigc++-2.0/include" 

%install 

%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Oct 10 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0-1

* Sat Sep 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- update to 1.5.0-1

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-1
- update to 1.4.0-1

* Sat Aug 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
