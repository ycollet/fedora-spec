# Global variables for github repository
%global commit0 efdef2601435cf4f36da4b8f7b0412fa404facb8
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           caps-lv2
Version:        0.9.%{shortcommit0}
Release:        1%{?dist}
Summary:        Caps LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/moddevices/caps-lv2
Source0:        https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         caps-0001-fix-cast.patch

BuildRequires: lv2-devel

%description
Caps LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}
%patch0 -p1

%build
make LV2_DEST=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make LV2_DEST=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
