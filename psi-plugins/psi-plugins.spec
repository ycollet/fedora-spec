# Global variables for github repository
%global commit0 afc66be1441d0119b5c8ff6e612b0e83e87610d2
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%define __waf ./waf

Summary:        PSI LV2 Plugins
Name:           psi-plugins
Version:        0.0.1
Release:        1%{?dist}
License:        GPL
Group:          Applications/Multimedia
URL:            https://github.com/ycollet/psi-plugins
Source0:        https://github.com/ycollet/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: jack-audio-connection-kit-devel

%description
psi-plugins is a small collection of LV2 plugins ideal for (but not limited to)
electronic music.

%prep
%setup -qn %{name}-%{commit0}

%build
%{__waf} configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__waf} build

%install
%{__rm} -rf %{buildroot}
%{__waf} -j1 install --destdir=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
%{_libdir}/lv2/*

%changelog
* Thu Nov 2 2017 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-1
- initial release 
