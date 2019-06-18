Summary: Guitar Amplifier emulator
Name:    rakarrack
Version: 0.6.2
Release: 2%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     git://git.code.sf.net/p/rakarrack/git
Source0: rakarrack.tar.gz
#Patch0:  rakarrack-0001-fix-distortion-and-ftlk.patch
Patch0: rakarrack-0002-fix-format-use.patch

# git clone git://git.code.sf.net/p/rakarrack/git rakarrack
# cd rakarrack
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz rakarrack.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: alsa-utils
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: libXpm-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
This app was born after an informal conversation about effects for guitar using GNU/linux.
The major part of this apps are discontinued or simply not have new versions after few
years. Josep Andreu say on the IRC chat 'I can made an app based on the effects set
hiden on code of ZynAddSubFX (by Paul Nasca Octavian)'. Some time after here is the
result of our work...

This app has 42 effects: EQ Lineal, Compressor, Distortion, Overdrive, Echo, Chorus,
Phaser, Flanger, Reverb , Parametric EQ, Wah Wah, Alienwha, Harmonizer etc.
The effects are procesed in cascade... The order of effects are configurable by the user.
The state of rack can be saved as 'presets'. Sets of presets can be stored as 'banks'.
The rack also has an integrated tuner and can receive MIDI control orders and can send MIDI
notes to MIDI devices like synthesizers.

%prep
%setup -qn %{name}

%patch0 -p1 

%build
./autogen.sh
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install

# desktop file categories
BASE="X-PlanetCCRMA X-Fedora Application AudioVideo"
XTRA="X-Synthesis X-MIDI X-Jack"
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/doc/*
%{_datadir}/man/*
%{_datadir}/pixmaps/*
%{_datadir}/rakarrack/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.5.1-1
- update for Fedora 29

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.5.1-1
- initial release 
