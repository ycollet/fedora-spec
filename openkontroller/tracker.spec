Name:    tracker.lv2
Version: 0.1.0
Release: 1%{?dist}
Summary: A simple tracker for LV2 events
URL:     https://git.open-music-kontrollers.ch/lv2/tracker.lv2
License: GPLv2+

# current commit: d32e89d2bfe4708e889f3b118ae98354a833d94d
# git clone --recursive https://git.open-music-kontrollers.ch/lv2/tracker.lv2
# cd tracker.lv2
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz tracker.lv2.tar.gz tracker.lv2/*
# rm -rf tracker.lv2

Source0: tracker.lv2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: meson
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: fontconfig-devel
BuildRequires: sord

%description
A simple tracker for LV2 events

%prep
%autosetup -n %{name}

%build

%set_build_flags

VERBOSE=1 %meson --prefix=/usr -Dlv2libdir=%{_lib}/lv2
VERBOSE=1 %meson_build 

%install
VERBOSE=1 %meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial build
