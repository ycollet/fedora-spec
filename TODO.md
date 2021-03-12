** Add new packages
 Dplug               -> https://github.com/AuburnSounds/Dplug
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
LinuxShowPlayer      -> https://github.com/FrancescoCeruti/linux-show-player

** Add BuildRequires make in spec file which requires it:
BuildRequires: make

** Add source.sh file in spec file:
Source1: source.sh

** Add check section:
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

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
