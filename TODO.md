Fedora 33 - To be fixed:

BespokeSynth	-> JUCE was missing + lto-wrapper -> to fix directly on fedora 33 ... wait until gcc update
performer	-> cmake + ui_setlist.h missing - pb cmake 3.18 ...
qscintilla	-> fail to build for qt4
miniaudicle	-> qscintilla was missing
sonic-pi	-> cmake - check ruby version

Add new packages:
 Dplug
 SmartGuitarAmp -> https://github.com/keyth72/SmartGuitarAmp
 improviz-performance -> https://github.com/rumblesan/improviz-performance
 osmid -> https://github.com/llloret/osmid
 Squeezer -> https://github.com/mzuther/Squeezer
 DAFx19-Gamelanizer/ -> https://github.com/lukemcraig/DAFx19-Gamelanizer
 ladspa-t5-plugins -> https://gitlab.com/t-5/ladspa-t5-plugins
 OwlSim -> https://github.com/pingdynasty/OwlSim
 slplugins -> https://github.com/figbug/slplugins
 DeLooper -> https://github.com/sonejostudios/DeLooper
 morphex -> https://github.com/MarcSM/morphex
 CF3 -> https://github.com/MtnViewJohn/context-free.git
 minicomputer -> http://minicomputer.sourceforge.net/
 freqtweak
 dexed
 mephisto -> https://open-music-kontrollers.ch/lv2/mephisto/
 xmonk -> https://github.com/brummer10/Xmonk.lv2
 zrythm - ZPlugins -> https://git.zrythm.org/cgit/zplugins/
 zrythm - reproc -> https://github.com/DaanDeMeyer/reproc
 zrythm - lsp-dsp -> add a devel package
 emissioncontrol2 -> https://github.com/EmissionControl2/EmissionControl2
 
 supercollider-study -> https://github.com/rumblesan/super-collider-study
 
** Add source.sh file in spec file:
Source1: source.sh

** Add check section:
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

** Fix debug generation:

purr-data/purr-data.spec	has a pure binary dependency
improviz/improviz.spec 		(Cabal ...)
processing/processing.spec	precompiled java package
rack				fail with some fedora flags
ams-lv2/lvtk.spec 		(???)
psi-plugins 			error with fedora 33 + lv2-devel
picoloop/picoloop.spec		complex ...
orca/orca.spec			really special build system
ryukau/ryukau.spec		gcc hangs during compilation of parameter.cpp
performer/performer.spec	ui_setlist.h missing - cmake 3.18 pb probably
socallab/SocaLabs-plugins.spec	build fails because of a default juce path / maybe use juce 5.4 ...

surge/stochas.spec		juce maybe ...

zrythm/zrythm.spec
ossia/ossia-score.spec
odin2/odin2.spec

** Check install 644 / 755 usage:
A misuse of these permissions may let the debug build fail

** Fix Cadence build on FC33:
Cadence:
../widgets/pixmapdial.cpp: In member function 'virtual void PixmapDial::paintEvent(QPaintEvent*)':
../widgets/pixmapdial.cpp:231:26: error: aggregate 'QPainterPath ballPath' has incomplete type and cannot be defined
  231 |             QPainterPath ballPath;
      |                          ^~~~~~~~
../widgets/pixmapdial.cpp:278:26: error: aggregate 'QPainterPath ballPath' has incomplete type and cannot be defined
  278 |             QPainterPath ballPath;
      |                          ^~~~~~~~

Odin2: doesn't load into Carla.
 -> copy the whole plugin directory structure
