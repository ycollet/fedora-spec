Name:    structuresynth
Version: 1.5.0
Release: 1%{?dist}
Summary: Structure Synth generates 3D structures by specifying a design grammar

License: GPLv2
URL:     https://sourceforge.net/projects/structuresynth/

# svn checkout https://svn.code.sf.net/p/structuresynth/code/trunk structuresynth
# cd structuresythn
# finf . -nams .svn -exec rm -rf {} \,
# cd ..
# tar cvfz structuresynth.tar.gz structuresynth
# rm -rf structuresynth

Source: structuresynth.tar.gz
Patch0: structuresynth-nullptr.patch
Patch1: structuresynth-qmake.patch

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: freeglut-devel
BuildRequires: desktop-file-utils

%description
Structure Synth generates 3D structures by specifying a design grammar.
Even simple systems may generate surprising and complex structures.
Structure Synth offers a graphical environment with multiple tabs, syntax highlighting, and OpenGL preview.

%prep
%autosetup -p0 -n structuresynth

%build

%qmake_qt5 StructureSynth.pro
%make_build

%install

mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_datadir}/structuresynth/examples
mkdir -p %{buildroot}/%{_datadir}/structuresynth/misc
mkdir -p %{buildroot}/%{_datadir}/applications/
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
cp -r Examples/* %{buildroot}/%{_datadir}/structuresynth/examples/
cp -r Misc/* %{buildroot}/%{_datadir}/structuresynth/misc/
cp StructureSynthBin %{buildroot}/%{_bindir}/structuresynth
cp structure-synth.desktop %{buildroot}/%{_datadir}/applications/
cp images/structuresynth.png %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install                         \
  --add-category="Graphics"                  \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/structure-synth.desktop

%files
%doc changelog.txt notes.txt bugs.txt
%license LICENSE.GPL3 LICENSE.LGPL LICENSE.README
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Sep 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- initial-version

