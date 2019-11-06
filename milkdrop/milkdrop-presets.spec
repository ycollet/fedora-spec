Summary: Additional presets for ProjectM
Name:    projectM-extra-presets
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2+ and GPLv3 and Green OpenMusic
Group:   Applications/Multimedia
URL:     http://projectm.sourceforge.net

Source0: https://sourceforge.net/projects/projectm/files/presets-samples/presets-2.0.0-Source.tar.gz
Source1: https://sourceforge.net/projects/projectm/files/presets-samples/presets-projectm-2.0.0-Source.tar.gz
Source2: https://sourceforge.net/projects/projectm/files/presets-samples/presets-milkdrop_200-2.0.0-Source.tar.gz
Source3: https://sourceforge.net/projects/projectm/files/presets-samples/presets-milkdrop_104-2.0.0-Source.tar.gz
Source4: http://ycollette.free.fr/Milkdrop/milkdrop-md-presets.zip
Source5: http://ycollette.free.fr/Milkdrop/milkdrop-megapack.zip
Source6: http://ycollette.free.fr/Milkdrop/milkdrop-vlc-presets.zip
Source7: http://spiegelmc.com.s3.amazonaws.com/pub/projectm_presets.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: p7zip tar

%description
A collection of additional preset for projectM.

%package md
Summary: Extra presets for projectM (md presets)
Group:   Applications/Multimedia

%description md
Extra presets for projectM (md presets)

%package megapack
Summary: Extra presets for projectM (megapack presets)
Group:   Applications/Multimedia

%description megapack
Extra presets for projectM (megapack presets)

%package bltc201
Summary: Extra presets for projectM (bltc201 presets)
Group:   Applications/Multimedia

%description bltc201
Extra presets for projectM (bltc201 presets)

%package tryptonaut
Summary: Extra presets for projectM (tryptonaut presets)
Group:   Applications/Multimedia

%description tryptonaut
Extra presets for projectM (tryptonaut presets)

%package yin
Summary: Extra presets for projectM (yin presets)
Group:   Applications/Multimedia

%description yin
Extra presets for projectM (yin presets)

%prep

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT

# These directories are owned by hydrogen:
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/projectM/presets

tar xvfz %{SOURCE0} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM/presets/
tar xvfz %{SOURCE1} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM/presets/
tar xvfz %{SOURCE2} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM/presets/
tar xvfz %{SOURCE3} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM/presets/

pushd .

cd $RPM_BUILD_ROOT%{_datadir}/projectM/presets

mv presets-2.0.0-Source              presets-2.0.0
mv presets-projectm-2.0.0-Source     projectm-2.0.0
mv presets_milkdrop_200-2.0.0-Source milkdrop-2.0.0
mv presets_milkdrop_104-2.0.0-Source milkdrop-1.0.4

popd

7za x %{SOURCE4} -o$RPM_BUILD_ROOT%{_datadir}/projectM/presets/
7za x %{SOURCE5} -o$RPM_BUILD_ROOT%{_datadir}/projectM/presets/
7za x %{SOURCE6} -o$RPM_BUILD_ROOT%{_datadir}/projectM/presets/
7za x %{SOURCE7} -o$RPM_BUILD_ROOT%{_datadir}/projectM/presets/

pushd .

cd $RPM_BUILD_ROOT%{_datadir}/projectM/presets

mv milkdrop-md-presets  md
mv milkdrop-megapack    megapack
mv milkdrop-vlc-presets vlc

mv presets/presets_bltc201    bltc201
mv presets/presets_tryptonaut tryptonaut
mv presets/presets_yin        yin

find . -name "..[a-zA-Z]*"   -exec rm {} \;
find . -name ".[a-zA-Z]*"    -exec rm {} \;
find . -name "...[a-zA-Z]*"  -exec rm {} \;
find . -name ".. [a-zA-Z]*"  -exec rm {} \;
find . -name "...@[a-zA-Z]*" -exec rm {} \;
find . -name "*.cmake"       -exec rm {} \;

# Cleanup
rm -rf presets

rm md/presets/*.jar
rm md/presets/*.bat

rm -rf milkdrop-2.0.0/CMakeFiles
rm -rf milkdrop-1.0.4/CMakeFiles
rm -rf projectm-2.0.0/CMakeFiles
rm -rf presets-2.0.0/CMakeFiles

find . -name "amandio c*" -exec rm {} \;
find . -name "*.bak" -exec rm {} \;
find . -name "*.prjm" -exec rm {} \;

# Rename
find . -name "*.MILK" -exec mv {} `basename {} .MILK`.milk \;
find . -name "*.MILk" -exec mv {} `basename {} .MILk`.milk \;
find . -name "*.MIL"  -exec mv {} `basename {} .MIL`.milk \;
find . -name "*.mil"  -exec mv {} `basename {} .mil`.milk \;

# Manage permissions

chmod a+rwx,g+rx,o+rx md megapack vlc bltc201 tryptonaut yin

find . -name "*.milk"  -exec chmod a-x {} \;

popd

%clean

rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/projectM/presets/presets-2.0.0/*
%{_datadir}/projectM/presets/projectm-2.0.0/*
%{_datadir}/projectM/presets/milkdrop-2.0.0/*
%{_datadir}/projectM/presets/milkdrop-1.0.4/*
%{_datadir}/projectM/presets/vlc/*

%files md
%{_datadir}/projectM/presets/md/*

%files megapack
%{_datadir}/projectM/presets/megapack/*

%files bltc201
%{_datadir}/projectM/presets/bltc201/*

%files tryptonaut
%{_datadir}/projectM/presets/tryptonaut/*

%files yin
%{_datadir}/projectM/presets/yin/*

%changelog
* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- fix for Fedora 31

* Sun Sep 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- Initial release
