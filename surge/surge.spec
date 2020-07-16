Name:    surge
Version: 1.6.6
Release: 5%{?dist}
Summary: A VST2 synthetizer
License: GPLv2+

# Use ./source.sh 1.6.6 to get the sources

URL:     https://github.com/surge-synthesizer/surge
Source0: surge.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: premake5
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: rsync
BuildRequires: python2
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel

%description
A VST2 synthetizer

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

%ifarch x86_64
  sed -i -e "s/lib\/vst/lib64\/vst/g" build-linux.sh
%endif

sed -i -e "s/python/python2/g" premake5.lua
sed -i -e "/-Wl,--strip-all/d" premake5.lua

tar xvfj %{SOURCE1}

%build

export VST2SDK_DIR=vst/vstsdk2.4/

%set_build_flags

./build-linux.sh clean-all
./build-linux.sh -p vst2 premake
./build-linux.sh -p vst3 premake
./build-linux.sh -p lv2 premake

# Inject optflags into CFLAGS
sed -i "s|^\s*ALL_CFLAGS\s*+=.*|ALL_CFLAGS += \$(ALL_CPPFLAGS) %{optflags} -I/usr/include/freetype2/ -fPIC|"     surge-lv2.make
sed -i "s|^\s*ALL_CXXFLAGS\s*+=.*|ALL_CXXFLAGS += \$(ALL_CPPFLAGS) %{optflags} -I/usr/include/freetype2/ -fPIC|" surge-lv2.make
sed -i "s|^\s*ALL_CFLAGS\s*+=.*|ALL_CFLAGS += \$(ALL_CPPFLAGS) %{optflags} -I/usr/include/freetype2/ -fPIC|"     surge-vst2.make
sed -i "s|^\s*ALL_CXXFLAGS\s*+=.*|ALL_CXXFLAGS += \$(ALL_CPPFLAGS) %{optflags} -I/usr/include/freetype2/ -fPIC|" surge-vst2.make
sed -i "s|^\s*ALL_CFLAGS\s*+=.*|ALL_CFLAGS += \$(ALL_CPPFLAGS) %{optflags} -I/usr/include/freetype2/ -fPIC|"     surge-vst3.make
sed -i "s|^\s*ALL_CXXFLAGS\s*+=.*|ALL_CXXFLAGS += \$(ALL_CPPFLAGS) %{optflags} -I/usr/include/freetype2/ -fPIC|" surge-vst3.make
# Disable stripping the executable
sed -i "s| -s | |" surge-lv2.make
sed -i "s| -s | |" surge-vst2.make
sed -i "s| -s | |" surge-vst3.make

./build-linux.sh -p vst2 build
./build-linux.sh -p vst3 build
./build-linux.sh -p lv2 build

%install 

export HOME=.
mkdir .vst
mkdir .vst3
mkdir .lv2
mkdir -p .local/share

./build-linux.sh -v -p vst2 -l install
./build-linux.sh -v -p vst3 -l install
./build-linux.sh -v -p lv2 -l install

%__install -m 755 -d %{buildroot}%{_libdir}/vst/
%__install -m 644 -p .vst/*.so %{buildroot}/%{_libdir}/vst/

%__install -m 755 -d %{buildroot}%{_libdir}/vst3/
%__install -m 644 -p .vst3/Surge.vst3/Contents/x86_64-linux/*.so %{buildroot}/%{_libdir}/vst3/

%__install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -r .lv2/* %{buildroot}/%{_libdir}/lv2/

%__install -m 755 -d %{buildroot}%{_datadir}/Surge/
rsync -rav .local/share/Surge/* %{buildroot}/%{_datadir}/Surge/

%files
%{_datadir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Jul 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-5
- update to 1.6.6-5 - fix package

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-4
- update to 1.6.6-4 - fix debug build

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-3
- update to 1.6.6-3 - fix requires for subpackage

* Mon Jun 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-2
- update to 1.6.6-2

* Sat Feb 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-1
- update to 1.6.6-1

* Tue Feb 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.5-1
- update to 1.6.5-1

* Sun Nov 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-1
- update to 1.6.3-1

* Thu Sep 26 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.2.1
- update to 1.6.2.1

* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b9
- update to beta9

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b3
- Initial spec file
