%global debug_package %{nil}

Summary: A crossplatform music editor for creating Commodore 64 music. Uses reSID library by Dag Lem and supports alternatively HardSID & CatWeasel devices.
Name:    goatracker
Version: 2.75
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia

URL:     https://sourceforge.net/projects/goattracker2/
Source0: https://sourceforge.net/projects/goattracker2/files/GoatTracker 2 Stereo/%{version}/GoatTracker_%{version}_Stereo.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: SDL-devel

%description
A crossplatform music editor for creating Commodore 64 music. Uses reSID library by Dag Lem and supports alternatively HardSID & CatWeasel devices.

%prep
mkdir -p goatracker-%{version}
cd goatracker-%{version}
unzip %SOURCE0

%build

cd goatracker-%{version}/src
sed -i -e "/CFLAGS/c\CFLAGS=%{build_cflags} -Ibme -Iasm" makefile.common
sed -i -e "/CXXFLAGS/c\CXXFLAGS=%{build_cflags} -Ibme -Iasm" makefile.common
%{__make} DESTDIR=%{buildroot} %{?_smp_mflags}

%install

cd goatracker-%{version}

%{__rm} -rf %{buildroot}

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__cp -a linux/* %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/pixmaps
install -m 644 src/goattrk2.bmp %{buildroot}%{_datadir}/pixmaps/

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/goatracker.desktop << EOF
[Desktop Entry]
Name=goatracker
Comment=A tracker synthetizer.
Exec=/usr/bin/gt2stereo
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/goattrk2.bmp
Categories=AudioVideo;
EOF

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples
%__cp -r examples/* %{buildroot}%{_datadir}/%{name}/examples/

%__install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc
%__cp -a goat_tracker_commands.pdf %{buildroot}%{_datadir}/%{name}/doc/

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/goatracker.desktop

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
%doc goatracker-%{version}/authors goatracker-%{version}/copying goatracker-%{version}/readme_resid.txt goatracker-%{version}/readme_sdl.txt goatracker-%{version}/readme.txt

%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Thu Jan 3 2019 Yann Collette <ycollette dot nospam at free.fr> 2.75-1
- Initial release of spec file
