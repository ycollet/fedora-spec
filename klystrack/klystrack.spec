%global debug_package %{nil}

# Global variables for github repository
%global commit0 4ab998ee33673b87ba2c63e696c65016d73b5deb
%global gittag0 v1.7.4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Klystrack is a chiptune tracker for making chiptune-like music on a modern computer.
Name:    klystrack
Version: 1.7.4
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kometbomb.github.io/klystrack/
Source0: klystrack.tar.gz

BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: SDL2-devel
BuildRequires: SDL2_gfx-devel
BuildRequires: SDL2_image-devel

%description
Klystrack is a chiptune tracker for making chiptune-like music on a modern computer.

%prep
%setup -qn %{name}

%build

sed -i -e "s/-Werror//g" Makefile
%{__make} DESTDIR=%{buildroot} PREFIX=/usr RES_PATH=/usr/lib64/%{name}/ CFG=release

%install

%{__rm} -rf %{buildroot}

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__cp bin.release/%{name} %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
%__install -m 644 icon/256x256.png %{buildroot}/%{_datadir}/icons/%{name}/
%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 linux/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/res
%__cp -r res/* %{buildroot}%{_datadir}/%{name}/res/
%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc
%__cp -r doc/* %{buildroot}%{_datadir}/%{name}/doc/
%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples/instruments/n00bstar-instruments/
%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples/songs/
%__cp -r examples/instruments/* %{buildroot}%{_datadir}/%{name}/examples/instruments/
%__cp -r examples/songs/*       %{buildroot}%{_datadir}/%{name}/examples/songs/
%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/themes
%__cp -r themes/* %{buildroot}%{_datadir}/%{name}/themes/
%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/key
%__cp -r key/* %{buildroot}%{_datadir}/%{name}/key/

%clean

%{__rm} -rf %{buildroot}

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/%{name} >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/%{name} >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/%{name} >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%changelog
* Fri Sep 21 2018 Yann Collette <ycollette dot nospam at free.fr> 1.7.4-1
- Initial release of spec file
