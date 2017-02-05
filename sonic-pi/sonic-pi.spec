# Do not check any files here for requires
%global __requires_exclude_from (^.*/vendor/.*$|^.*/native/.*$)

#HOSTING-SERVICE:  "github.com"
%global OWNER samaaron

Name:           sonic-pi
Version:        2.11.1
%global gittag0 v%{version}
Release:        2%{?dist}
Summary:        A musical programming environment 
License:        MIT
URL:            http://sonic-pi.net/
Source0:        https://github.com/%{OWNER}/%{name}/archive/%{gittag0}/%{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel, qscintilla-qt5-devel, qwt-qt5-devel, supercollider-devel, cmake, libffi-devel, ruby-devel
Requires:   pulseaudio-module-jack 
Requires:   supercollider-sc3-plugins


%description
Sonic Pi is an open source programming environment designed to explore and
teach programming concepts through the process of creating new sounds. 
Comes with an associated scheme of work which emphasizes the importance of
creativity in the learning process and gives users the control to turn their
sonic ideas into reality.

%prep
%setup -qn %{name}-%{version} 

%build
pushd app/server/bin
././compile-extensions.rb
popd
pushd app/gui/qt/
cp -f ruby_help.tmpl ruby_help.h
../../server/bin/qt-doc.rb -o ruby_help.h

sed -i "s/-lqt5scintilla2/-lqscintilla2-qt5/g" SonicPi.pro

lrelease-qt5 SonicPi.pro
qmake-qt5 -o Makefile SonicPi.pro
make


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications/
cp -Rip app/ %{buildroot}%{_datadir}/%{name}/
ln -s %{_datadir}/%{name}/app/gui/qt/rp-app-bin %{buildroot}%{_bindir}/%{name}



cat > %{buildroot}%{_datadir}/applications/fedora-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{_datadir}/%{name}/app/gui/qt/images/icon-smaller.png
Comment=Music live coding for everyone
Comment[es]=Programación de música en vivo al alcance de cualquiera 
Terminal=false
Type=Application
Categories=Application;AudioVideo;Audio;Development;IDE;Music;Education;
X-AppInstall-Package=%{name}
EOF
desktop-file-install  --vendor "fedora" --dir=%{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/applications/fedora-%{name}.desktop 


%files
%{_datadir}
%{_bindir}/sonic-pi
%doc CHANGELOG.md  COMMUNITY.md  CONTRIBUTORS.md  HOW-TO-CONTRIBUTE.md  INSTALL.md  LICENSE.md  README.md  SYNTH_DESIGN.md  TESTING.md  TRANSLATION.md

%changelog
* Mon Dec 28 2015 Ismael Olea <ismael@olea.org> 2.8.0-2
- Added missed supercollider-sc3-plugins dependency https://github.com/samaaron/sonic-pi/issues/897#issuecomment-167682120

* Mon Dec 28 2015 Ismael Olea <ismael@olea.org> 2.8.0-1
- updating to 2.8.0

* Fri Dec 13 2013 Amadeus Konopko a.konopko@hotmail.com 0-0.3
- Added armv6 architecture build, removed some requires.

* Fri Dec 6 2013 Amadeus Konopko a.konopko@hotmail.com 0-0.2
- Modified files list to only include app folder, README, and LICENSE.

* Fri Nov 22 2013 Amadeus Konopko a.konopko@hotmail.com 0-0.1
- Made an initial rpm to package the sonic-pi application.

