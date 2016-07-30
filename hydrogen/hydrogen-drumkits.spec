Summary: Additional DrumKits for Hydrogen
Name: hydrogen-drumkits
Version: 0.9.6
Release: 2%{?dist}
License: GPLv2+ and GPLv3 and Green OpenMusic
Group: Applications/Multimedia
URL: http://www.hydrogen-music.org

Source0:  http://downloads.sourceforge.net/hydrogen/ForzeeStereo.h2drumkit
Source1:  http://downloads.sourceforge.net/hydrogen/circAfrique.h2drumkit
Source2:  http://downloads.sourceforge.net/hydrogen/BJA_Pacific.h2drumkit
Source3:  http://downloads.sourceforge.net/hydrogen/deathmetal-drumkit.h2drumkit
Source4:  http://downloads.sourceforge.net/hydrogen/Millo_MultiLayered3.h2drumkit
Source5:  http://downloads.sourceforge.net/hydrogen/Millo_MultiLayered2.h2drumkit
Source6:  http://downloads.sourceforge.net/hydrogen/Millo-Drums_v.1.h2drumkit
Source7:  http://downloads.sourceforge.net/hydrogen/HardElectro1.h2drumkit
Source8:  http://downloads.sourceforge.net/hydrogen/ElectricEmpireKit.h2drumkit
Source9:  http://downloads.sourceforge.net/hydrogen/Classic-626.h2drumkit
Source10: http://downloads.sourceforge.net/hydrogen/Classic-808.h2drumkit
Source11: http://downloads.sourceforge.net/hydrogen/K-27_Trash_Kit.h2drumkit
Source12: http://downloads.sourceforge.net/hydrogen/EasternHop-1.h2drumkit
Source13: http://downloads.sourceforge.net/hydrogen/YamahaVintageKit.h2drumkit
Source14: http://downloads.sourceforge.net/hydrogen/ColomboAcousticDrumkit.h2drumkit
Source15: http://downloads.sourceforge.net/hydrogen/ErnysPercussion.h2drumkit
Source16: http://downloads.sourceforge.net/hydrogen/Boss_DR-110.h2drumkit
Source17: http://downloads.sourceforge.net/hydrogen/TR808909.h2drumkit
Source18: http://downloads.sourceforge.net/hydrogen/Techno-1.h2drumkit
Source19: http://downloads.sourceforge.net/hydrogen/TD-7kit.h2drumkit
Source20: http://downloads.sourceforge.net/hydrogen/Synthie-1.h2drumkit
Source21: http://downloads.sourceforge.net/hydrogen/HipHop-2.h2drumkit
Source22: http://downloads.sourceforge.net/hydrogen/HipHop-1.h2drumkit
Source23: http://downloads.sourceforge.net/hydrogen/3355606kit.h2drumkit
Source24: http://downloads.sourceforge.net/hydrogen/VariBreaks.h2drumkit

# From http://www.bandshed.net/sounds/h2drumkit/
Source25: http://www.bandshed.net/sounds/h2drumkit/AVL-BlackPearl-4A-1.0.h2drumkit
Source26: http://www.bandshed.net/sounds/h2drumkit/AVL-BlackPearl-4B-1.0.h2drumkit
Source27: http://www.bandshed.net/sounds/h2drumkit/AVL-BlackPearl-5-1.0.h2drumkit
Source28: http://www.bandshed.net/sounds/h2drumkit/AVL-RedZep-4-1.0.h2drumkit
Source29: http://www.bandshed.net/sounds/h2drumkit/AVL-RedZep-5-1.0.h2drumkit
Source30: http://www.bandshed.net/sounds/h2drumkit/Gimme%20A%20Hand%201.0.h2drumkit

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: hydrogen >= 0.9.5

%description
A collection of additional drumkits for the 
Hydrogen advanced drum machine for GNU/Linux.

%prep
%setup -q -c -n %{name} -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT

# These directories are owned by hydrogen:
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits

# Now copy everything into the $RPM_BUILD_ROOT
# "Forzee Stereo Drumkit"
# "circAfrique v4"
for drumkitdir in 3355606kit ColomboAcousticDrumkit ElectricEmpireKit  \
		  HardElectro1 K-27_Trash_Kit Millo_MultiLayered3 Techno-1 YamahaVintageKit \
		  BJA_Pacific Classic-626 DeathMetal ErnysPercussion HipHop-1 Millo-Drums_v.1 \
		  Synthie-1 TR808909 Classic-808 EasternHop-1  \
		  HipHop-2 Millo_MultiLayered2 TD-7kit VariBreaks ; do
  cp -a $drumkitdir  $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
done

cp -a Forzee\ Stereo\ Drumkit $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
cp -a circAfrique\ v4 $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
cp -a Boss\ DR-110 $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/*

%changelog
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.9.6-1
- updated list of drumkits
