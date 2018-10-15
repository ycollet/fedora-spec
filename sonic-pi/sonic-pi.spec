# Do not check any files here for requires
%global __requires_exclude_from (^.*/vendor/.*$|^.*/native/.*$)

# Global variables for github repository
%global commit0 3b1bb2cc71862beaa6ce18a75fc7c90fe8bc65ac
%global gittag0 v3.1.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    sonic-pi
Version: 3.1.0
%global gittag0 v%{version}
Release: 2%{?dist}
Summary: A musical programming environment 
License: MIT
URL:     http://sonic-pi.net/
Source0: https://github.com/samaaron/%{name}/archive/%{gittag0}/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qscintilla-qt5-devel
BuildRequires: qwt-qt5-devel
BuildRequires: qt5-linguist
BuildRequires: supercollider-devel
BuildRequires: cmake
BuildRequires: libffi-devel
BuildRequires: ruby-devel
BuildRequires: aubio-devel
BuildRequires: boost-devel

Requires(pre): pulseaudio-module-jack 
Requires(pre): supercollider-sc3-plugins
Requires(pre): supercollider
Requires(pre): ruby

%description
Sonic Pi is an open source programming environment designed to explore and
teach programming concepts through the process of creating new sounds. 
Comes with an associated scheme of work which emphasizes the importance of
creativity in the learning process and gives users the control to turn their
sonic ideas into reality.

%prep
%setup -qn %{name}-%{version} 

%build

cd app/gui/qt

sed -i "s/-lqt5scintilla2/-lqscintilla2-qt5/g" SonicPi.pro

ruby ../../server/ruby/bin/compile-extensions.rb
ruby ../../server/ruby/bin/i18n-tool.rb -t
cp -f ruby_help.tmpl ruby_help.h
ruby ../../server/ruby/bin/qt-doc.rb -o ruby_help.h
lrelease-qt5 SonicPi.pro
qmake-qt5 SonicPi.pro
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications/
cp -Rip app/ %{buildroot}%{_datadir}/%{name}/
ln -s %{_datadir}/%{name}/app/gui/qt/rp-app-bin %{buildroot}%{_bindir}/%{name}

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/atomic_reference.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/atomic/ext/atomic_reference.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/atomic_reference.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/ffi_c.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/ffi-1.9.17/ext/ffi_c/ffi_c.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/ffi_c.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/did_you_mean/method_receiver.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/did_you_mean-0.10.0/ext/did_you_mean/method_receiver.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/did_you_mean/method_receiver.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/ruby_prof.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/ruby-prof-0.15.8/ext/ruby_prof/ruby_prof.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/ruby_prof.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/fast_osc.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/fast_osc-0.0.12/ext/fast_osc/fast_osc.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/fast_osc.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/rugged.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/rugged-0.26.0/ext/rugged/rugged.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/2.4.0/rugged.so


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

desktop-file-install  --vendor "fedora" \
                      --dir=%{buildroot}%{_datadir}/applications/ \
                      %{buildroot}%{_datadir}/applications/fedora-%{name}.desktop 


%files
%{_datadir}
%{_bindir}/sonic-pi
%doc CHANGELOG.md  COMMUNITY.md  CONTRIBUTORS.md  HOW-TO-CONTRIBUTE.md  INSTALL.md  LICENSE.md  README.md  SYNTH_DESIGN.md  TESTING.md  TRANSLATION.md

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> 3.1.0
- update for Fedora 29

* Tue Apr 17 2018 Yann Collette <ycollette.nospam@free.fr> update build process
- update build process
- update to 3.1.0
- remove duplicated so

* Thu Oct 26 2017 Yann Collette <ycollette.nospam@free.fr> update to 3.0.1
- update to 3.0.1

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

