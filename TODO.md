** Add new packages
 osmid               -> https://github.com/llloret/osmid
 Squeezer            -> https://github.com/mzuther/Squeezer
 DAFx19-Gamelanizer  -> https://github.com/lukemcraig/DAFx19-Gamelanizer
 ladspa-t5-plugins   -> https://gitlab.com/t-5/ladspa-t5-plugins
 OwlSim              -> https://github.com/pingdynasty/OwlSim
 DeLooper            -> https://github.com/sonejostudios/DeLooper
 morphex             -> https://github.com/MarcSM/morphex
 freqtweak           -> https://github.com/essej/freqtweak
 mephisto            -> https://open-music-kontrollers.ch/lv2/mephisto/
 zrythm - lsp-dsp    -> add a devel package for zrythm
 emissioncontrol2    -> https://github.com/EmissionControl2/EmissionControl2
 regrader            -> https://github.com/igorski/regrader
 mapmap              -> https://github.com/mapmapteam/mapmap
 openshow            -> https://github.com/mapmapteam/openshow
 supercollider-study -> https://github.com/rumblesan/super-collider-study
 marsyas             -> http://marsyas.info/
 vapoursynth         -> http://www.vapoursynth.com/
                     -> https://github.com/dubhater/vapoursynth-fluxsmooth
					 -> https://github.com/HolyWu/L-SMASH-Works
					 -> https://github.com/dubhater/vapoursynth-mvtools
					 -> https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Deblock
frequanalizer        -> https://github.com/ffAudio/Frequalizer
paulstretch          -> https://bitbucket.org/xenakios/paulstretchplugin/src/master/
NoiseTorch           -> https://github.com/lawl/NoiseTorch
CadMus               -> https://github.com/josh-richardson/cadmus
tangamp              -> https://github.com/sadko4u/tamgamp.lv2
tascar               -> https://github.com/HoerTech-gGmbH/tascar/
midieditor           -> https://github.com/markusschwenk/midieditor/

** Cleanup
Remove mv-6pm or 6pm. Both are normally the same package

** Todo for 34
- update snd to 21.1
- add gamin from src.fedoraproject.org (if required)
- check std::numeric_limits pb (gcc 11 / C++17 ?)
- Socalab -> /usr/bin/ld: /usr/lib64/libglib-2.0.so.0: error adding symbols: DSO missing from command line
- error: 'numeric_limits' is not a member of 'std'
- rivendell: rdcart.cpp:365:39: error: ordered comparison of pointer with integer zero ('const void*' and 'int')
- kmidimon: needs drumstick-devel
- glava: <artificial>:(.text+0x1005): undefined reference to `glfwGetX11Window'
- ecasound: python3 missing

** Add BuildRequires make in spec file which requires it:
BuildRequires: make

** Add source.sh file in spec file:
Source1: source.sh

** Add check section:
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*%{name}.*.xml

** Check before packaging:
remove -march=native from Makefiles if it's present

** lvtk
fix pkgconfig file installation

** Fix debug generation:

purr-data/purr-data.spec       -> has a pure binary dependency
improviz/improviz.spec         -> (Cabal ...)
processing/processing.spec     -> precompiled java package -> noarch ...
ams-lv2/lvtk.spec              -> static library
psi-plugins                    -> error with fedora 33 + lv2-devel
picoloop/picoloop.spec         -> complex ...
orca/orca.spec                 -> really special build system
performer/performer.spec       -> ui_setlist.h missing - cmake 3.18 pb probably
socallab/SocaLabs-plugins.spec -> build fails because of a default juce path / maybe use juce 5.4 ...
surge/stochas.spec             -> jucaid compilation pb - maybe due tu %set_build_flags ...
zrythm/ztoolkit                -> it's a static library ...
ossia/ossia-score.spec         -> don't build anymore. Wait for next release

** Fedora 33 - To be fixed:
performer -> cmake + ui_setlist.h missing - pb cmake 3.18 ...
