# Have a look at:
# https://github.com/archlinux/svntogit-community/tree/packages/sonic-pi/trunk

# Do not check any files here for requires
%global __requires_exclude_from (^.*/vendor/.*$|^.*/native/.*$)

%global __mangle_shebangs_exclude_from /vendor/
%global __mangle_shebangs_exclude ruby

%global debug_package %{nil}

Name:    sonic-pi
Version: 3.2.2
Release: 6%{?dist}
Summary: A musical programming environment 
License: MIT
URL:     http://sonic-pi.net/

Source0: https://github.com/samaaron/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: osmid.tar.gz
Source2: sonic-pi-source.sh

# Use sonic-pi-source.sh to get source files

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
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: erlang-erts
BuildRequires: ruby
BuildRequires: rubygem-rake
BuildRequires: rubygem-bundler
BuildRequires: rubygem-racc
BuildRequires: zlib-devel

Requires(pre): pulseaudio-module-jack 
Requires(pre): jack-audio-connection-kit-example-clients
Requires(pre): supercollider-sc3-plugins
Requires(pre): supercollider
Requires(pre): ruby
Requires(pre): aubio
Requires(pre): osmid

%description
Sonic Pi is an open source programming environment designed to explore and
teach programming concepts through the process of creating new sounds. 
Comes with an associated scheme of work which emphasizes the importance of
creativity in the learning process and gives users the control to turn their
sonic ideas into reality.

%prep
%autosetup -n %{name}-%{version} 

cd app/gui/qt

sed -i -e "/add_subdirectory(external\/QScintilla-2.11.4)/d" CMakeLists.txt
sed -i -e "s/QScintilla/qscintilla2-qt5/g" CMakeLists.txt
sed -i -e "s/return QCoreApplication::applicationDirPath() + \"\/..\/..\/..\/..\";/return QString(\"\/usr\/share\/sonic-pi\");/g" mainwindow.cpp

cd ../../..

sed -i -e "s/env python/env python3/g" app/server/ruby/vendor/ffi-1.11.3/ext/ffi_c/libffi/generate-darwin-source-and-headers.py

# remove make clean
sed -i -e "/make clean/d" app/server/ruby/bin/compile-extensions.rb

%build

cd app/gui/qt

ruby ../../server/ruby/bin/compile-extensions.rb
ruby ../../server/ruby/bin/i18n-tool.rb -t
cp -f utils/ruby_help.tmpl utils/ruby_help.h
ruby ../../server/ruby/bin/qt-doc.rb -o utils/ruby_help.h
lrelease-qt5 SonicPi.pro

cd ..
mkdir build
cd build
%set_build_flags
cmake -DCMAKE_BUILD_TYPE=RELEASE ../qt
make

#Build Erlang files
cd ../../server/erlang
erlc osc.erl
erlc pi_server.erl

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/app/gui/qt/theme/
mkdir -p %{buildroot}%{_datadir}/%{name}/etc/
mkdir -p %{buildroot}%{_datadir}/applications/
cp -ra app/gui/qt/theme/* %{buildroot}%{_datadir}/%{name}/app/gui/qt/theme/
cp app/gui/build/sonic-pi %{buildroot}%{_bindir}/%{name}
cp -ra etc/*              %{buildroot}%{_datadir}/%{name}/etc/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp app/gui/qt/images/icon-smaller.png %{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/native/osmid/
ln -s /usr/bin/m2o %{buildroot}%{_datadir}/%{name}/app/server/native/osmid/
ln -s /usr/bin/o2m %{buildroot}%{_datadir}/%{name}/app/server/native/osmid/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/erlang/
cp -ra app/server/erlang/*.beam %{buildroot}%{_datadir}/%{name}/app/server/erlang/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/bin/
cp -ra  app/server/ruby/bin/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/bin/

# Manage ruby version for various Fedora version
%define rb_version "2.4.0"
%if 0%{?fedora} >= 28
%define rb_version "2.5.0"
%endif
%if 0%{?fedora} >= 30
%define rb_version "2.6.0"
%endif
%if 0%{?fedora} >= 32
%define rb_version "2.7.0"
%endif

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/

cp -ra app/server/ruby/rb-native/%{rb_version}/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/
cp -ra app/server/ruby/*.rb %{buildroot}%{_datadir}/%{name}/app/server/ruby/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/vendor/
cp -ra app/server/ruby/vendor/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/vendor/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/lib/
cp -ra app/server/ruby/lib/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/lib/

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/atomic_reference.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/atomic/ext/atomic_reference.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/atomic_reference.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/ffi_c.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/ffi-1.11.3/ext/ffi_c/ffi_c.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/ffi_c.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/ruby_prof.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/ruby-prof-0.15.8/ext/ruby_prof/ruby_prof.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/ruby_prof.so

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/rugged.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/rugged-0.28.4.1/ext/rugged/rugged.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/rugged.so

find %{buildroot}%{_datadir}/%{name}/etc/wavetables/ -name "AdventureKidWaveforms.txt" -exec chmod a-x {} \;

# cleanup
rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/vendor/parslet/example/email_parser.rb

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=/usr/share/pixmaps/icon-smaller.png
Comment=Music live coding for everyone
Comment[es]=Programación de música en vivo al alcance de cualquiera 
Terminal=false
Type=Application
Categories=Application;AudioVideo;Audio;Development;IDE;Music;Education;
X-AppInstall-Package=%{name}
EOF

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc CHANGELOG.md  COMMUNITY.md  CONTRIBUTORS.md  HOW-TO-CONTRIBUTE.md  INSTALL.md  README.md  SYNTH_DESIGN.md  TESTING.md  TRANSLATION.md
%license LICENSE.md
%{_bindir}/sonic-pi
%{_datadir}

%changelog
* Fri Apr 24  2020 Yann Collette <ycollette.nospam@free.fr> 3.2.2-6
- fix for Fedora a32

* Mon Apr 6 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.2-5
- update to 3.2.2-5

* Sun Mar 22 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.0-5
- fix spec file - update oscmid to v0.6.8

* Mon Mar 2 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.0-4
- update to 3.2.0-4

* Sun Mar 1 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.0-3
- update to 3.2.0

* Thu Nov 7 2019 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- fix for Fedora 31

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- update for Fedora 30

* Tue Mar 26 2019 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- update to master (and add rugged-0.28.0)

* Fri Dec 7 2018 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- fix for Fedora 29 - update to master (to get rugged-0.27.5)

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> 3.1.0-2
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

