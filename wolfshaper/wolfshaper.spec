# Global variables for github repository
%global commit0 c61b6690a892c503f3341db767a7d74b56970e29
%global gittag0 1.1.4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    wolf-shaper
Version: 0.1.7
Release: 1%{?dist}
Summary: Wolf-shaper is a waveshaper plugin with a graph editor.

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/pdesaulniers/wolf-shaper

# git clone https://github.com/pdesaulniers/wolf-shaper
# cd wolf-shaper
# git checkout v0.1.7
# git submodule init
# git submodule update
# rm -rf .git dpf/.git
# cd ..
# tar cvfz wolf-shaper.tar.gz wolf-shaper/*

Source0: wolf-shaper.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

%description
Wolf Shaper is a waveshaper plugin with a graph editor.

%package -n dssi-%{name}
Summary: DSSI version of the Wolf Shaper plugin.
Group:   Applications/Multimedia

%package -n lv2-%{name}
Summary: LV2 version of the Wolf Shaper plugin.
Group:   Applications/Multimedia

%package -n vst-%{name}
Summary: VST version of the Wolf Shaper plugin.
Group:   Applications/Multimedia

%description -n dssi-%{name}
DSSI version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n lv2-%{name}
LV2 version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n vst-%{name}
VST version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%prep
%setup -qn %{name}

%ifarch x86_64
sed -i -e "s/\$(PREFIX)\/lib/\$(PREFIX)\/lib64/g" Makefile
%endif

%build
make DESTDIR=%{buildroot} PREFIX=/usr %{?_smp_mflags} all

%install
make DESTDIR=%{buildroot} PREFIX=/usr install

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Tue Apr 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- Initial version of the spec file
