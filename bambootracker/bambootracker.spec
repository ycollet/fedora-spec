# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 d5f21089a656220bf793bb35e2e4ade6b9c5b087
%global gittag0 v0.2.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: BambooTracker is a music tracker for the Yamaha YM2608 (OPNA) sound chip which was used in NEC PC-8801/9801 series computers.
Name:    BambooTracker
Version: 0.2.1
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/rerrahkr/BambooTracker
Source0: https://github.com/rerrahkr/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-linguist
BuildRequires: qtchooser

%description
BambooTracker is a music tracker for the Yamaha YM2608 (OPNA) sound chip which was used in NEC PC-8801/9801 series computers.

%prep
%setup -qn %{name}-%{commit0}

%build

cd BambooTracker
qmake-qt5 "PREFIX=/usr" BambooTracker.pro
%{__make} DESTDIR=%{buildroot} PREFIX=/usr

%install

%{__rm} -rf %{buildroot}

cd BambooTracker
%{__make} INSTALL_ROOT=%{buildroot} PREFIX=/usr install

cd ..

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 BambooTracker.desktop %{buildroot}%{_datadir}/applications/
%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/demos/
%__install -m 644 demos/* %{buildroot}%{_datadir}/%{name}/demos/
%__install -m 755 -d %{buildroot}/%{_datadir}/man/man1
%__install -m 644 BambooTracker.1 %{buildroot}%{_datadir}/man/man1/%{name}.1
%__install -m 755 -d %{buildroot}/%{_datadir}/man/fr/man1
%__install -m 644 BambooTracker.fr.1 %{buildroot}%{_datadir}/man/fr/man1/%{name}.1

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 img/icon.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean

%{__rm} -rf %{buildroot}

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
%defattr(-,root,root,-)
%doc CHANGELOG.md IMPORTANT.md LICENSE README.md README_ja.md
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Jun 17 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.1-1
- Update to version 0.2.1

* Thu May 30 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- Initial release of spec file
