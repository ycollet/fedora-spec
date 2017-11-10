# Global variables for github repository
%global commit0 afc66be1441d0119b5c8ff6e612b0e83e87610d2
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

%define __waf ./waf

Summary:        PSI LV2 Plugins
Name:           psi-plugins-doc
Version:        0.0.1
Release:        2%{?dist}
License:        GPL
Group:          Applications/Multimedia
URL:            https://github.com/ycollet/psi-plugins
Source0:        https://github.com/ycollet/psi-plugins/archive/%{commit0}.tar.gz#/psi-plugins-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: non-ntk-devel
BuildRequires: non-ntk-fluid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
psi-plugins is a small collection of LV2 plugins ideal for (but not limited to)
electronic music.

%package -n lv2-midi_gate-psi
Summary:        PSI Plugins / Midi Gate LV2 plugin
Group:          Applications/Multimedia
%description -n lv2-midi_gate-psi
This is a stereo gate MIDI based on the example LV2 midi gate plugin by Dave Robillard

%package -n lv2-midi_rnd-psi
Summary:        PSI Plugins / Midi Rnd LV2 plugin
Group:          Applications/Multimedia
%description -n lv2-midi_rnd-psi
midi_rnd is a simple MIDI random note generator for the inspirationally bereft.

It receives incoming note messages and returns a randomized note of the same 
velocity with the parameters defined by octave range and scale. The generated 
note is produced relative to the incoming key.

An attempt to map Note Off midi messages to previously recevied note on
messages is made but is only reliable for sequential input. As a result some 
NoteOn messages may be left hanging. 

%package -n lv2-sidechain_gate-psi
Summary:        PSI Plugins / Sidechain Gate LV2 plugin
Group:          Applications/Multimedia
%description -n lv2-sidechain_gate-psi
This is a stereo gate with optional sidechain input based on the Gate plugin by Steve Harris. 

%package -n lv2-super_welle
Summary:        PSI Plugins / Super Welle LV2 plugin
Group:          Applications/Multimedia
%description -n lv2-super_welle
super_welle is a 2x16 oscillator virtual analog synthesizer. Originally it 
started out as an experiment in simulating the super saw of the 
Roland JP8000/JP8080 but has since widened is scope. 

%prep
%setup -qn psi-plugins-%{commit0}

%build
%{__waf} configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__waf} build

%install
%{__rm} -rf %{buildroot}
%{__waf} -j1 install --destdir=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md
#midi_gate-psi.lv2/README.md midi_rnd-psi.lv2/README.md sidechain_gate-psi.lv2/README.md super_welle.lv2/README.md

%files -n lv2-midi_gate-psi
%{_libdir}/lv2/midi_gate-psi.lv2/*

%files -n lv2-midi_rnd-psi
%{_libdir}/lv2/midi_rnd-psi.lv2/*

%files -n lv2-sidechain_gate-psi
%{_libdir}/lv2/sidechain_gate-psi.lv2/*

%files -n lv2-super_welle
%{_libdir}/lv2/super_welle-psi.lv2/*

%changelog
* Thu Nov 2 2017 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-2
- multi-packages

* Thu Nov 2 2017 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-1
- initial release 
