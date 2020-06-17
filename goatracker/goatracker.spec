%global debug_package %{nil}

Summary: A crossplatform music editor for creating Commodore 64 music. Uses reSID library by Dag Lem and supports alternatively HardSID & CatWeasel devices.
Name:    goatracker
Version: 2.76
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
A crossplatform music editor for creating Commodore 64 music.
Uses reSID library by Dag Lem and supports alternatively
HardSID & CatWeasel devices.

%prep
%autosetup -n gt2stereo

sed -i -e "/CFLAGS/c\CFLAGS=%{build_cflags} -Ibme -Iasm" trunk/src/makefile.common
sed -i -e "/CXXFLAGS/c\CXXFLAGS=%{build_cflags} -Ibme -Iasm" trunk/src/makefile.common

%build

cd trunk/src
make clean
%make_build

%install

cd trunk

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__cp -a linux/* %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/pixmaps
install -m 644 -p src/goattrk2.bmp %{buildroot}%{_datadir}/pixmaps/

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
        --add-category=Audio \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/goatracker.desktop

%files
%doc trunk/authors trunk/readme_resid.txt trunk/readme_sdl.txt trunk/readme.txt
%license trunk/copying
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Wed Jun 17 2020 Yann Collette <ycollette dot nospam at free.fr> 2.76-1
- update to 2.76

* Thu Jan 3 2019 Yann Collette <ycollette dot nospam at free.fr> 2.75-1
- Initial release of spec file
