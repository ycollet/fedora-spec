# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:         polyphone
Version:      1.8
Release:      2%{?dist}
Summary:      A SF2 sound font editor
URL:          http://polyphone-sourndfour.com/fr/
Group:        Applications/Multimedia

License:      GPLv2+

Source0:      %{name}-%{version}-src.zip
Source1:      polyphone.desktop
Source2:      polyphone.xml

BuildRequires: qt4-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel 
BuildRequires: rtmidi-devel 
BuildRequires: stk-devel 
BuildRequires: qcustomplot-devel 
BuildRequires: libvorbis-devel 
BuildRequires: libogg-devel 

%description
Polyphone is a free software for editing soundfonts in format sf2. These files contain a multitude of audio samples put together and configured so as to form musical instruments that can be used by synthesizers such as fluidsynth and played using a MIDI keyboard.
The goal of Polyphone is to provide:

* a simple and efficient interface for creating and editing .sf2 files, available on Windows, Mac OS X and Linux, tools to facilitate and automate the editing of different parameters, making it possible to handle a large amount of data.

* Polyphone is licensed under GNU General Public License. Anyone may thus access the source code, and is welcome to help in the development of the program.

%prep
%setup0 -qn %{name}-%{version}-src

%build

cd trunk
qmake-qt4 "DEFINES+=USE_LOCAL_RTMIDI" polyphone.pro
make VERBOSE=1 %{?_smp_mflags}
cd ..

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 trunk/RELEASE/polyphone %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
%__install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 trunk/ressources/logo.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category X-Drumming \
        --add-category X-Sound \
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
%doc trunk/changelog trunk/README
%{_bindir}/polyphone
%{_datadir}/applications/polyphone.desktop
%{_datadir}/mime/packages/polyphone.xml
%{_datadir}/icons/hicolor/*


%changelog
* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- Initial spec file 1.6.0
