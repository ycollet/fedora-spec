# Global variables for github repository
%global commit0 4ff361ada2afdc3a58092aba4e99b1cf347bf1e0
%global gittag0 v0.7.2b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           pianobooster
Version:        0.7.2b
Release:        6%{?dist}
Summary:        A MIDI file player that teaches you how to play the piano
Group:          Applications/Sound
License:        GPL-3.0-or-later

Url:            https://github.com/captnfab/PianoBooster
Source0:        https://github.com/captnfab/PianoBooster/archive/%{commit0}.tar.gz#/PianoBooster-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  hicolor-icon-theme

Requires:       dejavu-sans-fonts
Requires:       unzip
Requires:       hicolor-icon-theme
Requires:       %{name} = %{version}-%{release}
Requires:       libnotify

Recommends:     qt5-qttranslations

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano.

PianoBooster is a fun way of playing along with a musical accompaniment and
at the same time learning the basics of reading musical notation.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI keyboard.

To run Piano Booster you need a MIDI Piano Keyboard and a MIDI interface
for the PC. If you don't have a MIDI keyboard you can still try out
PianoBooster, using the PC keyboard ('x' is middle C), but a MIDI piano
is really recommended.

#----------------------------------------------------------------------------

%prep
%setup -qn PianoBooster-%{commit0}

%build

%cmake -DUSE_SYSTEM_FONT=ON \
       -DNO_DOCS=ON \
       -DNO_LICENSE=ON \
       -DNO_CHANGELOG=ON \
       -DWITH_MAN=ON \
       .
%make_build

%install
%make_install -C build

%files
%doc README.md Changelog.txt doc/faq.md
%license license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/music
%dir %{_datadir}/games/%{name}/translations
%{_datadir}/games/%{name}/music/*.zip
%{_datadir}/games/%{name}/translations/%{name}*.qm
%{_datadir}/games/%{name}/translations/music*.qm
%{_datadir}/games/%{name}/translations/*.json
%{_mandir}/man6/%{name}.6*

%changelog
* Tue Mar 17 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.2b-1
- initial specfile

