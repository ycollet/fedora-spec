# Global variables for github repository
%global commit0 1130bc475e7d0cad554fc0b44a4cd1e98acfaa5d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

%global _cmake_skip_rpath %{nil}

Summary: LSP LV2 Plugins
Name:    lsp-plugins
Version: 1.1.21
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/sadko4u/lsp-plugins

# git clone https://github.com/sadko4u/lsp-plugins
# cd lsp-plugins
# git checkout lsp-plugins-1.1.21
# git submodule init
# git submodule update
# find . -name .git --exec rm -rf {} \;
# cd ..
# tar cvfz lsp-plugins.tar.gz lsp-plugins/*

Source0: lsp-plugins.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
BuildRequires: chrpath

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

%prep
%setup -qn lsp-plugins

%build

%{__make} DESTDIR=%{buildroot} PREFIX=/usr BUILD_PROFILE=%{_arch} CC_FLAGS=-DLSP_NO_EXPERIMENTAL BIN_PATH=%{_bindir} LIB_PATH=%{_libdir} DOC_PATH=%{_docdir}

%install

%{__rm} -rf %{buildroot}

%{__make} DESTDIR=%{buildroot} PREFIX=/usr BUILD_PROFILE=%{_arch} CC_FLAGS=-DLSP_NO_EXPERIMENTAL BIN_PATH=/usr/bin LIB_PATH=/usr/lib64 DOC_PATH=/usr/share/doc install

chrpath --delete $RPM_BUILD_ROOT/usr/bin/*
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/ladspa/*.so
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/lsp-plugins/*.so
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/lv2/lsp-plugins.lv2/*.so
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/vst/lsp-plugins-lxvst-%{version}/*.so

%clean

%{__rm} -rf %{buildroot}

%files
%doc CHANGELOG.txt LICENSE.txt README.txt
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%{_sysconfdir}/xdg/menus/applications-merged/lsp-plugins.menu

%changelog
* Sun May 17 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.21-1
- update to 1.1.21-1

* Sun Apr 19 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.19-1
- update to 1.1.19-1

* Sun Apr 5 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.17-1
- update to 1.1.17-1

* Sun Mar 29 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.15-1
- update to 1.1.15-1

* Tue Dec 24 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.13-1
- update to 1.1.13-1

* Sun Dec 22 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.11-1
- update to 1.1.11-1

* Tue Jul 23 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.10-1
- update to 1.1.10-1

* Mon Mar 18 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.7-1
- update to 1.1.7-1

* Fri Dec 21 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.5-1
- update to 1.1.5-1

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.4-1
- update for Fedora 29

* Sun Sep 30 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.4-1
- Initial release of the spec file
