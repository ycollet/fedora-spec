# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 c8f53207b0feb110d35b2bf5b6fd89dc148f27e7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    jalv_select
Version: 1.3.0.%{shortcommit0}
Release: 2%{?dist}
Summary: A LV2 synthetizer launcher for Jack audio
URL:     https://github.com/brummer10/jalv_select
Group:   Applications/Multimedia

License: GPLv2+

Source0: https://github.com/brummer10/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gtkmm24-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel

%description
A little GUI to select lv2 plugs from a list

%prep
%setup -qn %{name}-%{commit0}

%build

make DESTDIR=%{buildroot} PREFIX=%{_usr} %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} PREFIX=%{_usr} %{?_smp_mflags} install

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/jalv.select.desktop

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%doc README.md
%{_bindir}/jalv.select
%{_datadir}/applications/jalv.select.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/locale/*
%{_mandir}/man1/jalv.select.*

%changelog
* Wed Jul 17 2019 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- update to 1.3.0

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-2
- update for Fedora 29

* Sat Sep 29 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-2

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 75a52292550178db2e3d82b5656ffd836382c9ef

* Thu Jan 18 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file 0.7.0
