** Add new packages
 Dplug               -> https://github.com/AuburnSounds/Dplug
 SmartGuitarAmp      -> https://github.com/keyth72/SmartGuitarAmp
 osmid               -> https://github.com/llloret/osmid
 Squeezer            -> https://github.com/mzuther/Squeezer
 DAFx19-Gamelanizer  -> https://github.com/lukemcraig/DAFx19-Gamelanizer
 ladspa-t5-plugins   -> https://gitlab.com/t-5/ladspa-t5-plugins
 OwlSim              -> https://github.com/pingdynasty/OwlSim
 DeLooper            -> https://github.com/sonejostudios/DeLooper
 morphex             -> https://github.com/MarcSM/morphex
 freqtweak           -> https://github.com/essej/freqtweak
 dexed               -> https://github.com/asb2m10/dexed
 mephisto            -> https://open-music-kontrollers.ch/lv2/mephisto/
 zrythm - lsp-dsp    -> add a devel package for zrythm
 emissioncontrol2    -> https://github.com/EmissionControl2/EmissionControl2
 regrader            -> https://github.com/igorski/regrader
 mapmap              -> https://github.com/mapmapteam/mapmap
 openshow            -> https://github.com/mapmapteam/openshow
 supercollider-study -> https://github.com/rumblesan/super-collider-study

** Add source.sh file in spec file:
Source1: source.sh

** Add check section:
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

** Fix debug generation:

purr-data/purr-data.spec       -> has a pure binary dependency
improviz/improviz.spec         -> (Cabal ...)
processing/processing.spec     -> precompiled java package -> noarch ...
rack                           -> fail with some fedora flags
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
sonic-pi  -> cmake - check ruby version
