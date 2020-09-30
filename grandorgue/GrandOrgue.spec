%global debug_package %{nil}

%define revision 2330

Name:    GrandOrgue
Version: 0.3.1.%{revision}
Release: 3%{?dist}
Summary: GrandOrgue is a sample based pipe organ simulator.
License: GPLv2+

URL:     http://sourceforge.net/projects/ourorgan
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 2330 http://svn.code.sf.net/p/ourorgan/svn/trunk ourorgan-2330
#  tar cvfz ourorgan-2330.tar.gz ourorgan-2330
Source0:      ourorgan-%{revision}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: wxGTK3-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: systemd-devel
BuildRequires: wavpack-devel
BuildRequires: fftw-devel

%description
GrandOrgue is a sample based pipe organ simulator.

%prep
%autosetup -n ourorgan-%{revision}

%build

%cmake -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
       -DLIBINSTDIR=lib64

%cmake_build

%install

%cmake_install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc README AUTHORS
%license license.txt
%{_bindir}/%{name}
%{_bindir}/GrandOrgueTool
%{_datadir}/*
%{_libdir}/*

%changelog
* Wed Sep 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- fix for fedora 33

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to release 2330

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to release 2294

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to release 2242

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- Initial version
