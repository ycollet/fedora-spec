# Global variables for github repository
%global commit0 9cccef501c7897465c7baa3ebb2315d653af5971
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    zynthian-data
Version: 1.0.0.%{shortcommit0}
Release: 2%{?dist}
Summary: A set of LV2 presets for DISTRHO

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/zynthian/zynthian-data.git

Source0: https://github.com/zynthian/zynthian-data/archive/%{commit0}.tar.gz#/zynthian-data-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

%description
A set of LV2 presets for DISTRHO

%package distrho
Summary:  Presets for DISTRHO plugins
Group:    Applications/Multimedia
Requires: DISTRHO-Ports

%description distrho
Presets for DISTRHO plugins

%package synthv1
Summary:  Presets for synthv1 plugin
Group:    Applications/Multimedia
Requires: synthv1

%description synthv1
Presets for synthv1 plugin

%package padthv1
Summary:  Presets for padthv1 plugin
Group:    Applications/Multimedia
Requires: padthv1

%description padthv1
Presets for padthv1 plugin

%prep
%setup -qn %{name}-%{commit0}

%build

%install 

mkdir -p %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/[oO]bxd* %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/VEX*     %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/[vV]ex*  %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/synthv1* %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/padthv1* %{buildroot}/usr/%{_lib}/lv2/

%files distrho
%{_libdir}/lv2/VEX*
%{_libdir}/lv2/[vV]ex*
%{_libdir}/lv2/[oO]bxd*

%files synthv1
%{_libdir}/lv2/synthv1*

%files padthv1
%{_libdir}/lv2/padthv1*

%changelog
* Mon Mar 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- Add padthv1 presets

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
