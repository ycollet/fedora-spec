Name:    mamba
Version: 1.7.0
Release: 2%{?dist}
Summary: Virtual Midi Keyboard for Jack Audio Connection Kit
License: BSD

URL:     https://github.com/brummer10/Mamba

# To get the source code: ./mamba_source.sh v1.7

Source0: Mamba.tar.gz
Source1: mamba-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: libsmf-devel
BuildRequires: fluidsynth-devel
BuildRequires: alsa-lib-devel

%description
Mamba is not only a Virtual MIDI keyboard, it's also a MIDI looper.
It allow you to record, for example a bass loop on one channel and
then play along on a other channel with a piano or whatever.

You could save your loops to MIDI files if you wish, in any case,
Mamba save your last record and load it on the next start on default.

Mamba is also a MIDI visualizer, it shows not only what you play,
it shows as well incoming events. It also allow you to load MIDI files,
play them in loop and show the output on the keyboard. You could select
which channel you would monitor on the keyboard.
You could as well monitor all channels at once.

Mamba includes also support by fluidsynth,
you could load a soundfont and directly play along.

Mamba will keep it's settings, so once a soundfont is loaded,
on the next start you could just play along with the keyboard.
You could load a new soundfont at any time. You could as well
exit fluidsynth to use Mamba as plain Virtual MIDI keyboard
with the synth of your choice.

%prep
%autosetup -n Mamba

%build

%set_build_flags

%make_build CXXFLAGS="%build_cxxflags -I/usr/include/cairo -I/usr/include/sigc++-2.0/ -I/usr/%{_lib}/sigc++-2.0/include" 

%install 

%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Nov 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7.0-2
- update to 1.7.0-2

* Tue Oct 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-2
- fix description, license and missing file

* Sat Oct 10 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0-1

* Sat Sep 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- update to 1.5.0-1

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-1
- update to 1.4.0-1

* Sat Aug 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
