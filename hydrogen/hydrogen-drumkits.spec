Summary: Additional DrumKits for Hydrogen
Name:    hydrogen-drumkits
Version: 0.9.6
Release: 4%{?dist}
License: GPLv2+ and GPLv3 and Green OpenMusic
Group:   Applications/Multimedia
URL:     http://www.hydrogen-music.org

Source0:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/ForzeeStereo.h2drumkit
Source1:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/circAfrique%20v4.h2drumkit
Source2:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/BJA_Pacific.h2drumkit
Source3:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/DeathMetal.h2drumkit
Source4:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Millo_MultiLayered3.h2drumkit
Source5:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Millo_MultiLayered2.h2drumkit
Source6:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Millo-Drums_v.1.h2drumkit
Source7:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/HardElectro1.h2drumkit
Source8:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/ElectricEmpireKit.h2drumkit
Source9:  https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Classic-626.h2drumkit
Source10: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Classic-808.h2drumkit
Source11: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/K-27_Trash_Kit.h2drumkit
Source12: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/EasternHop-1.h2drumkit
Source13: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/YamahaVintageKit.h2drumkit
Source14: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/ColomboAcousticDrumkit.h2drumkit
Source15: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/ErnysPercussion.h2drumkit
Source16: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Boss_DR-110.h2drumkit
Source17: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/TR808909.h2drumkit
Source18: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Techno-1.h2drumkit
Source19: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/TD-7kit.h2drumkit
Source20: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Synthie-1.h2drumkit
Source21: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/HipHop-2.h2drumkit
Source22: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/HipHop-1.h2drumkit
Source23: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/3355606kit.h2drumkit
Source24: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/VariBreaks.h2drumkit
Source25: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/The%20Black%20Pearl%201.0.h2drumkit 	
Source26: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/Lightning1024.h2drumkit 	
Source27: https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/SF3007-2011-Set-03.h2drumkit 	

# From http://www.bandshed.net/sounds/h2drumkit/
Source28: http://www.bandshed.net/sounds/h2drumkit/AVL-Drumkits-1.1/AVL-BlackPearl-4A-1.1.h2drumkit
Source29: http://www.bandshed.net/sounds/h2drumkit/AVL-Drumkits-1.1/AVL-BlackPearl-4B-1.1.h2drumkit
Source30: http://www.bandshed.net/sounds/h2drumkit/AVL-Drumkits-1.1/AVL-BlackPearl-5-1.1.h2drumkit
Source31: http://www.bandshed.net/sounds/h2drumkit/AVL-Drumkits-1.1/AVL-RedZep-4-1.1.h2drumkit
Source32: http://www.bandshed.net/sounds/h2drumkit/AVL-Drumkits-1.1/AVL-RedZep-5-1.1.h2drumkit
Source33: http://www.bandshed.net/sounds/h2drumkit/AVL-Drumkits-1.1/Gimme%20A%20Hand%201.1.h2drumkit

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

Requires: hydrogen >= 0.9.5

%description
A collection of additional drumkits for the 
Hydrogen advanced drum machine for GNU/Linux.

%package -n hydrogen-drumkit-3355606kit
Summary:        Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-3355606kit
Hydrogen drumkit

%package -n hydrogen-drumkit-BJA_Pacific
Summary:        BJA_Pacific Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-BJA_Pacific
BJA_Pacific hydrogen drumkit

%package -n hydrogen-drumkit-DeathMetal
Summary:        DeathMetal Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-DeathMetal
DeathMetal hydrogen drumkit

%package -n hydrogen-drumkit-Gimme_A_Hand_1.1
Summary:        Gimme_A_Hand_1.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Gimme_A_Hand_1.1
Gimme_A_Hand_1.1 hydrogen drumkit

%package -n hydrogen-drumkit-Lightning1024
Summary:        Lightning1024 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Lightning1024
Lightning1024 hydrogen drumkit

%package -n hydrogen-drumkit-TD-7kit
Summary:        TD-7kit Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-TD-7kit
TD-7kit hydrogen drumkit

%package -n hydrogen-drumkit-YamahaVintageKit
Summary:        YamahaVintageKit Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-YamahaVintageKit
YamahaVintageKit hydrogen drumkit

%package -n hydrogen-drumkit-AVL-BlackPearl-4A-1.1
Summary:        AVL-BlackPearl-4A-1.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-AVL-BlackPearl-4A-1.1
AVL-BlackPearl-4A-1.1 hydrogen drumkit

%package -n hydrogen-drumkit-Boss_DR-110
Summary:        Boss_DR-110 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Boss_DR-110
Boss_DR-110 hydrogen drumkit

%package -n hydrogen-drumkit-EasternHop-1
Summary:        EasternHop-1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-EasternHop-1
EasternHop-1 hydrogen drumkit

%package -n hydrogen-drumkit-Millo-Drums_v.1
Summary:        Millo-Drums_v.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Millo-Drums_v.1
Millo-Drums_v.1 hydrogen drumkit

%package -n hydrogen-drumkit-Techno-1
Summary:        Techno-1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Techno-1
Techno-1 hydrogen drumkit

%package -n hydrogen-drumkit-AVL-BlackPearl-4B-1.1
Summary:        AVL-BlackPearl-4B-1.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-AVL-BlackPearl-4B-1.1
AVL-BlackPearl-4B-1.1 hydrogen drumkit

%package -n hydrogen-drumkit-circAfrique_v4
Summary:        circAfrique_v4 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-circAfrique_v4
circAfrique_v4 hydrogen drumkit

%package -n hydrogen-drumkit-ElectricEmpireKit
Summary:        ElectricEmpireKit Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-ElectricEmpireKit
ElectricEmpireKit hydrogen drumkit

%package -n hydrogen-drumkit-HardElectro1
Summary:        HardElectro1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-HardElectro1
HardElectro1 hydrogen drumkit

%package -n hydrogen-drumkit-Millo_MultiLayered2
Summary:        Millo_MultiLayered2 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Millo_MultiLayered2
Millo_MultiLayered2 hydrogen drumkit

%package -n hydrogen-drumkit-The_Black_Pearl_1.0
Summary:        The_Black_Pearl_1.0 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-The_Black_Pearl_1.0
The_Black_Pearl_1.0 hydrogen drumkit

%package -n hydrogen-drumkit-AVL-BlackPearl-5-1.1
Summary:        AVL-BlackPearl-5-1.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-AVL-BlackPearl-5-1.1
AVL-BlackPearl-5-1.1 hydrogen drumkit

%package -n hydrogen-drumkit-Classic-626
Summary:        Classic-626 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Classic-626
Classic-626 hydrogen drumkit

%package -n hydrogen-drumkit-ErnysPercussion
Summary:        ErnysPercussion Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-ErnysPercussion
ErnysPercussion hydrogen drumkit

%package -n hydrogen-drumkit-HipHop-1
Summary:        HipHop-1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-HipHop-1
HipHop-1 hydrogen drumkit

%package -n hydrogen-drumkit-Millo_MultiLayered3
Summary:        Millo_MultiLayered3 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Millo_MultiLayered3
Millo_MultiLayered3 hydrogen drumkit

%package -n hydrogen-drumkit-TR808909
Summary:        TR808909 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-TR808909
TR808909 hydrogen drumkit

%package -n hydrogen-drumkit-AVL-RedZep-4-1.1
Summary:        AVL-RedZep-4-1.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-AVL-RedZep-4-1.1
AVL-RedZep-4-1.1 hydrogen drumkit

%package -n hydrogen-drumkit-Classic-808
Summary:        Classic-808 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Classic-808
Classic-808 hydrogen drumkit

%package -n hydrogen-drumkit-ForzeeStereo
Summary:        ForzeeStereo Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-ForzeeStereo
ForzeeStereo hydrogen drumkit

%package -n hydrogen-drumkit-HipHop-2
Summary:        HipHop-2 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-HipHop-2
HipHop-2 hydrogen drumkit

%package -n hydrogen-drumkit-SF3007-2011-Set-03
Summary:        SF3007-2011-Set-03 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-SF3007-2011-Set-03
SF3007-2011-Set-03 hydrogen drumkit

%package -n hydrogen-drumkit-AVL-RedZep-5-1.1
Summary:        AVL-RedZep-5-1.1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-AVL-RedZep-5-1.1
AVL-RedZep-5-1.1 hydrogen drumkit

%package -n hydrogen-drumkit-ColomboAcousticDrumkit
Summary:        ColomboAcousticDrumkit Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-ColomboAcousticDrumkit
ColomboAcousticDrumkit hydrogen drumkit

%package -n hydrogen-drumkit-K-27_Trash_Kit
Summary:        K-27_Trash_Kit Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-K-27_Trash_Kit
K-27_Trash_Kit hydrogen drumkit

%package -n hydrogen-drumkit-Synthie-1
Summary:        Synthie-1 Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-Synthie-1
Synthie-1 hydrogen drumkit

%package -n hydrogen-drumkit-VariBreaks
Summary:        VariBreaks Hydrogen drumkit
Group:          Applications/Multimedia

%description -n hydrogen-drumkit-VariBreaks
VariBreaks hydrogen drumkit

%prep

%install
rm -rf %{buildroot}

# These directories are owned by hydrogen:
mkdir -p %{buildroot}/%{_datadir}/hydrogen/data/drumkits/

# Now copy everything into the %{buildroot}

cp %{SOURCE0} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE1} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE2} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE3} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE4} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE5} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE6} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE7} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE8} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE9} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE10} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE11} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE12} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE13} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE14} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE15} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE16} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE17} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE18} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE19} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE20} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE21} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE22} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE23} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE24} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE25} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE26} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE27} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE28} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE29} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE30} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE31} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE32} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/
cp %{SOURCE33} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/

%clean
rm -rf %{buildroot}

%files -n hydrogen-drumkit-3355606kit
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/3355606kit.h2drumkit

%files -n hydrogen-drumkit-BJA_Pacific
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/BJA_Pacific.h2drumkit

%files -n hydrogen-drumkit-DeathMetal
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/DeathMetal.h2drumkit

%files -n hydrogen-drumkit-Gimme_A_Hand_1.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Gimme%20A%20Hand%201.1.h2drumkit

%files -n hydrogen-drumkit-Lightning1024
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Lightning1024.h2drumkit

%files -n hydrogen-drumkit-TD-7kit
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/TD-7kit.h2drumkit

%files -n hydrogen-drumkit-YamahaVintageKit
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/YamahaVintageKit.h2drumkit

%files -n hydrogen-drumkit-AVL-BlackPearl-4A-1.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/AVL-BlackPearl-4A-1.1.h2drumkit

%files -n hydrogen-drumkit-Boss_DR-110
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Boss_DR-110.h2drumkit

%files -n hydrogen-drumkit-EasternHop-1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/EasternHop-1.h2drumkit

%files -n hydrogen-drumkit-Millo-Drums_v.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Millo-Drums_v.1.h2drumkit

%files -n hydrogen-drumkit-Techno-1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Techno-1.h2drumkit

%files -n hydrogen-drumkit-AVL-BlackPearl-4B-1.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/AVL-BlackPearl-4B-1.1.h2drumkit

%files -n hydrogen-drumkit-circAfrique_v4
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/circAfrique%20v4.h2drumkit

%files -n hydrogen-drumkit-ElectricEmpireKit
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/ElectricEmpireKit.h2drumkit

%files -n hydrogen-drumkit-HardElectro1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/HardElectro1.h2drumkit

%files -n hydrogen-drumkit-Millo_MultiLayered2
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Millo_MultiLayered2.h2drumkit

%files -n hydrogen-drumkit-The_Black_Pearl_1.0
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/The%20Black%20Pearl%201.0.h2drumkit

%files -n hydrogen-drumkit-AVL-BlackPearl-5-1.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/AVL-BlackPearl-5-1.1.h2drumkit

%files -n hydrogen-drumkit-Classic-626
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Classic-626.h2drumkit

%files -n hydrogen-drumkit-ErnysPercussion
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/ErnysPercussion.h2drumkit

%files -n hydrogen-drumkit-HipHop-1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/HipHop-1.h2drumkit

%files -n hydrogen-drumkit-Millo_MultiLayered3
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Millo_MultiLayered3.h2drumkit

%files -n hydrogen-drumkit-TR808909
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/TR808909.h2drumkit

%files -n hydrogen-drumkit-AVL-RedZep-4-1.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/AVL-RedZep-4-1.1.h2drumkit

%files -n hydrogen-drumkit-Classic-808
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Classic-808.h2drumkit

%files -n hydrogen-drumkit-ForzeeStereo
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/ForzeeStereo.h2drumkit

%files -n hydrogen-drumkit-HipHop-2
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/HipHop-2.h2drumkit

%files -n hydrogen-drumkit-SF3007-2011-Set-03
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/SF3007-2011-Set-03.h2drumkit

%files -n hydrogen-drumkit-AVL-RedZep-5-1.1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/AVL-RedZep-5-1.1.h2drumkit

%files -n hydrogen-drumkit-ColomboAcousticDrumkit
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/ColomboAcousticDrumkit.h2drumkit

%files -n hydrogen-drumkit-K-27_Trash_Kit
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/K-27_Trash_Kit.h2drumkit

%files -n hydrogen-drumkit-Synthie-1
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/Synthie-1.h2drumkit

%files -n hydrogen-drumkit-VariBreaks
%defattr(-,root,root,-)
%{_datadir}/hydrogen/data/drumkits/VariBreaks.h2drumkit

%changelog
* Thu Apr 16 2020 Yann Collette <ycollette dot nospam at free.fr> 0.9.6-4
- updated list of drumkits

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.9.6-1
- updated list of drumkits
