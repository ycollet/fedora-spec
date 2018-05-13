# Global variables for github repository
%global commit0 072e2feb5c09d0fb51300e688b7e4f32b75e9c89
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
#%global debug_package %{nil}

Name:           caps-lv2
Version:        0.9.%{shortcommit0}
Release:        1%{?dist}
Summary:        Caps LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/moddevices/caps-lv2
Source0:        https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel

%description
Caps LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build

# to allow pow10f, we need to define _GNU_SOURCE
for Files in `find . -name Makefile`
do
    sed -ie "s/-ffast-math/-ffast-math -D_GNU_SOURCE/g" $Files
done

make LV2_DEST=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make LV2_DEST=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Update to latest master version

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
