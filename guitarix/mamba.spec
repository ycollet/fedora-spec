Name:    mamba
Version: 1.4.0
Release: 1%{?dist}
Summary: Virtual Midi Keyboard for Jack Audio Connection Kit

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/brummer10/Mamba

# git clone https://github.com/brummer10/Mamba
# cd Mamba
# git checkout v1.4
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz Mamba.tar.gz Mamba/*
# rm -rf Mamba

Source0: Mamba.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: libsmf-devel

%description
Virtual Midi Keyboard for Jack Audio Connection Kit

%prep
%autosetup -n Mamba

%build

%set_build_flags

%make_build CXXFLAGS="%build_cxxflags -I/usr/include/cairo -I/usr/include/sigc++-2.0/" 

%install 

%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-1
- update to 1.4.0-1

* Sat Aug 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
