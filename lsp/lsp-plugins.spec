# Global variables for github repository
%global commit0 1d41a52f6b2236f38670c2d3a28ab97c419a4754
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

%global _cmake_skip_rpath %{nil}

Summary: LSP LV2 Plugins
Name:    lsp-plugins
Version: 1.1.5
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sadko4u/lsp-plugins
Source0: https://github.com/sadko4u/lsp-plugins/archive/%{commit0}.tar.gz#/lsp-plugins-%{shortcommit0}.tar.gz
Source1: Makefile.lsp

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: cairo-devel
BuildRequires: ladspa-devel
BuildRequires: expat-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: mesa-libGL-devel
BuildRequires: php-cli

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

%prep
%setup -qn lsp-plugins-%{commit0}

%build

cp %{SOURCE1} Makefile

%{__make} DESTDIR=%{buildroot} PREFIX=/usr BUILD_PROFILE=%{_arch} CC_FLAGS=-DLSP_NO_EXPERIMENTAL BIN_PATH=%{_bindir} LIB_PATH=%{_libdir} DOC_PATH=%{_docdir}

%install

%{__rm} -rf %{buildroot}

%{__make} DESTDIR=%{buildroot} PREFIX=/usr BUILD_PROFILE=%{_arch} CC_FLAGS=-DLSP_NO_EXPERIMENTAL BIN_PATH=/usr/bin LIB_PATH=/usr/lib64 DOC_PATH=/usr/share/doc install

%clean

%{__rm} -rf %{buildroot}

%files
%doc CHANGELOG.txt LICENSE.txt README.txt
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Fri Dec 21 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.5-1
- update to 1.1.5

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.4-1
- update for Fedora 29

* Sun Sep 30 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.4-1
- Initial release of the spec file
