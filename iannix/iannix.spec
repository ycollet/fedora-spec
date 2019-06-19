# http://www.iannix.org/

# Global variables for github repository
%global commit0 1294f84ba809ebf5262a1c7071a18ac5ff4109b0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    IanniX
Version: 0.9.20.%{shortcommit0}
Release: 2%{?dist}
Summary: A graphic / MIDI / OSC player
URL:     https://github.com/iannix/Iannix
Group:   Applications/Multimedia

License: GPLv2+

Source0: https://github.com/iannix/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: iannix.xml
Patch0:  iannix-0001-fix-missing-glew.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: glew-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
IanniX is a graphical open source sequencer, based on Iannis Xenakis works, for digital art. IanniX syncs via Open Sound Control (OSC) events and curves to your real-time environment.

%prep
%setup -qn %{name}-%{commit0}
%patch0 -p1

%build

qmake-qt5 IanniX.pro
%{__make} VERBOSE=1 %{?_smp_mflags}

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 iannix.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 iannix %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 iannix.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

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
%license COPYING.txt
%{_bindir}/iannix
%{_datadir}/applications/IanniX.desktop
%{_datadir}/mime/packages/IanniX.xml
%{_datadir}/icons/hicolor/*


%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.20-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.20-2
- update to the latest master

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9.16-1
- Initial spec file 0.9.16
