# Global variables for github repository
%global commit0 1bc1fed211e140c7330d6035122234afe78e5257
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    plujain-ramp
Version: 1.1.3
Release: 1%{?dist}
Summary: Plujain-Ramp is a mono rhythmic tremolo LV2 Audio Plugin
License: GPLv2+

URL:     https://github.com/Houston4444/plujain-ramp.git
Source0: https://github.com/Houston4444/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
Plujain-Ramp is a mono rhythmic tremolo LV2 Audio Plugin.
Each period of the tremolo is made of one short fade in and one long fade out, so we can say it generates musical pulses.
It can also generate pitched periods (see Speed Effect).
There is currently no GUI, but it's not really needed.

%package -n lv2-%{name}
Summary: Real-time Noise Suppression LV2 Plugin
Group:   Applications/Multimedia

%description -n lv2-%{name}
A real-time noise suppression LV2 plugin for voice based on Xiph's RNNoise - https://github.com/xiph/rnnoise.
More info about the base library - https://people.xiph.org/~jm/demo/rnnoise/.

%prep
%setup -qn %{name}-%{commit0}

%build

make DESTDIR=%{buildroot} INSTALL_PATH=/usr/%{_lib}/lv2 VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} INSTALL_PATH=/usr/%{_lib}/lv2 install

%files -n lv2-%{name}
%doc readme.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Wed Jul 17 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-1
- update to 1.1.3

* Fri Apr 19 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial version of the spec file
