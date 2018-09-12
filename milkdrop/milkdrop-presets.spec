Summary: Additional presets for ProjectM
Name:    projectm-extra-presets
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2+ and GPLv3 and Green OpenMusic
Group:   Applications/Multimedia
URL:     http://projectm.sourceforge.net

Source0: https://sourceforge.net/projects/projectm/files/presets-samples/presets-2.0.0-Source.tar.gz
Source1: https://sourceforge.net/projects/projectm/files/presets-samples/presets-projectm-2.0.0-Source.tar.gz
Source2: https://sourceforge.net/projects/projectm/files/presets-samples/presets-milkdrop_200-2.0.0-Source.tar.gz
Source3: https://sourceforge.net/projects/projectm/files/presets-samples/NativePresets-2.0.0-Source.tar.gz
Source4: https://sourceforge.net/projects/projectm/files/presets-samples/presets-milkdrop_104-2.0.0-Source.tar.gz
Source5: http://ycollette.free.fr/Milkdrop/milkdrop-md-presets.zip
Source6: http://ycollette.free.fr/Milkdrop/milkdrop-megapack.zip
Source7: http://ycollette.free.fr/Milkdrop/milkdrop-vlc-presets.zip
Source8: http://spiegelmc.com.s3.amazonaws.com/pub/projectm_presets.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: p7zip tar

%description
A collection of additional preset for ProjectM.

%package md
Summary: Extra presets for ProjectM (md presets)
Group:   Applications/Multimedia

%description md
Extra presets for ProjectM (md presets)

%package megapack
Summary: Extra presets for ProjectM (megapack presets)
Group:   Applications/Multimedia

%description megapack
Extra presets for ProjectM (megapack presets)

%package bltc201
Summary: Extra presets for ProjectM (bltc201 presets)
Group:   Applications/Multimedia

%description bltc201
Extra presets for ProjectM (bltc201 presets)

%package tryptonaut
Summary: Extra presets for ProjectM (tryptonaut presets)
Group:   Applications/Multimedia

%description tryptonaut
Extra presets for ProjectM (tryptonaut presets)

%package yin
Summary: Extra presets for ProjectM (yin presets)
Group:   Applications/Multimedia

%description yin
Extra presets for ProjectM (yin presets)

%prep

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT

# These directories are owned by hydrogen:
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/projectm/presets

tar xvfz %{SOURCE0} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
tar xvfz %{SOURCE1} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
tar xvfz %{SOURCE2} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
tar xvfz %{SOURCE3} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
tar xvfz %{SOURCE4} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectm/presets/

pushd .

cd $RPM_BUILD_ROOT%{_datadir}/projectm/presets

mv presets-2.0.0-Source              presets-2.0.0
mv presets-projectm-2.0.0-Source     projectm-2.0.0
mv presets_milkdrop_200-2.0.0-Source milkdrop-2.0.0
mv NativePresets-2.0.0-Source        native-2.0.0
mv presets_milkdrop_104-2.0.0-Source milkdrop-1.0.4

popd

7za x %{SOURCE5} -o$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
7za x %{SOURCE6} -o$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
7za x %{SOURCE7} -o$RPM_BUILD_ROOT%{_datadir}/projectm/presets/
7za x %{SOURCE8} -o$RPM_BUILD_ROOT%{_datadir}/projectm/presets/

pushd .

cd $RPM_BUILD_ROOT%{_datadir}/projectm/presets

mv milkdrop-md-presets  md
mv milkdrop-megapack    megapack
mv milkdrop-vlc-presets vlc

mv presets/presets_bltc201    bltc201
mv presets/presets_tryptonaut tryptonaut
mv presets/presets_yin        yin

rm -rf presets

rm md/presets/*.jar
rm md/presets/*.bat

find . -name "..[a-zA-Z]*" -exec rm {} \;
find . -name ".[a-zA-Z]*"  -exec rm {} \;
find . -name "*.cmake" -exec rm {} \;

popd

%clean

rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/projectm/presets/presets-2.0.0/*
%{_datadir}/projectm/presets/projectm-2.0.0/*
%{_datadir}/projectm/presets/milkdrop-2.0.0/*
%{_datadir}/projectm/presets/milkdrop-1.0.4/*
%{_datadir}/projectm/presets/native-2.0.0/*
%{_datadir}/projectm/presets/vlc/*
%{_datadir}/projectm/presets/bltc201/*
%{_datadir}/projectm/presets/tryptonaut/*
%{_datadir}/projectm/presets/yin/*

%files md
%{_datadir}/projectm/presets/md/*

%files megapack
%{_datadir}/projectm/presets/megapack/*
%{_datadir}/projectm/presets/megapack/\.*
%{_datadir}/projectm/presets/megapack/\.\.*

%files bltc201
%{_datadir}/projectm/presets/bltc201/*

%files tryptonaut
%{_datadir}/projectm/presets/tryptonaut/*

%files yin
%{_datadir}/projectm/presets/yin/*

%changelog
* Sun Sep 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- Initial release
