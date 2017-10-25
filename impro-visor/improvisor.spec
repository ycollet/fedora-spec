# Copyright (c) 2007-2008 oc2pus
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de
#
# in the source directory, remove the sc directory (supercollider for windows).
#
%define name            improvisor
%define maj             9
%define min             1
%define patch           0
%define version         %{maj}.%{min}%{patch}
%define release         1

Name:                   %{name}
Version:                %{version}
Release:                %{release}
Summary:                Impro-Visor is a music notation program for jazz musicians
License:                GPL
URL:                    http://www.cs.hmc.edu/~keller/jazz/improvisor/
#Source0:                http://sourceforge.net/projects/impro-visor/files/Impro-Visor%207.0%20Release/
Source0:                %{name}%{maj}%{min}%{patch}.zip
Source1:                %{name}.sh
Source2:                %{name}.png
BuildArch:              noarch
BuildRequires:          unzip
BuildRequires:          desktop-file-utils
BuildRequires:          java-devel

Requires:               jpackage-utils
%if 0%{?rhel}
Requires(post):         jpackage-utils
Requires(postun):       jpackage-utils
%endif
Requires:               ant
Requires:               java >= 1.5

BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Impro-Visor (short for Improvisation Advisor) is a music notation
program designed to help jazz musicians compose and hear solos
similar to ones that might be improvised. The objective is to
improve understanding of solo construction and tune chord changes.

* Lead sheets and solos can be constructed through either
point-and-click or using a plain text editor (one is provided,
but any editor can be used). Solos or solo fragments can be
played back immediately on the computer, with chord accompaniment.

* It is not necessary that the soloist memorize the solos that are
created in Impro-Visor. Rather the act of constructing solos is
supposed to help one get a better understanding of the tune and of
solo construction. But one can use some, if not all, of the ideas
from the solos constructed, as many outstanding players have done
for generations.

* Impro-Visor also provides a way for the user to create and save
licks for later use. Lick creation is helpful in understanding
how to construct interesting lines over chord changes.

* When used for transcription, Impro-Visor allows easy mining of
selected licks from a solo for future reference.

* Impro-Visor uses dynamic menus in the form shown to help one
choose notes, cells, idioms, licks, and quotes for use in
constructing a solo.

* Musical knowledge about chords, scales, licks, etc. are definable
by the user, in the form of a vocabulary text file. These items are
defined in a single key, and Impro-Visor will transpose them to
any key.

* Impro-Visor saves solos and other lead sheets as free-form text.
We call this leadsheet notation. Although a point-and-click
interface is provided, users can optionally enter chords and/or
melody in this notation with a standard text editor and have them
displayed as a lead sheet in Impro-Visor. The documentation tells
how to create and interpret the notation. The notation also
provides slash-chords and polychords.

* The release of Impro-Visor comes with a few leadsheets with
melodies, a number of sample solos, transcriptions, and The
Imaginary Book, a large set (over 1600) of chords-only lead
sheets for standard and jazz tunes.

%prep
%setup -q -c %{name}

%build

%install

# jars
%__install -dm 755 %{buildroot}%{_javadir}
%__install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar

pushd %{buildroot}%{_javadir}
for jar in *-%{version}*; do
    ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
done
popd

%__install -dm 755 %{buildroot}%{_datadir}/%{name}
for i in grammars styleExtract styles; do
    %__install -dm 755 %{buildroot}%{_datadir}/%{name}/$i
    %__install -m 644 $i/* %{buildroot}%{_datadir}/%{name}/$i
done
%__install -dm 755 %{buildroot}%{_datadir}/%{name}/vocab
%__cp -a vocab/* %{buildroot}%{_datadir}/%{name}/vocab

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/leadsheets
%__cp -a leadsheets/* %{buildroot}%{_datadir}/%{name}/leadsheets

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/connectomes
%__cp -a connectomes/* %{buildroot}%{_datadir}/%{name}/connectomes

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/midi
%__cp -a midi/* %{buildroot}%{_datadir}/%{name}/midi

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/voicings
%__cp -a voicings/* %{buildroot}%{_datadir}/%{name}/voicings

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/transforms
%__cp -a transforms/* %{buildroot}%{_datadir}/%{name}/transforms

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/fractals
%__cp -a fractals/* %{buildroot}%{_datadir}/%{name}/fractals

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/counts
%__cp -a counts/* %{buildroot}%{_datadir}/%{name}/counts

# startscript
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{SOURCE1} %{buildroot}%{_bindir}

# icon and menu-entry
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
%__install -dm 755 %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Impro-Visor
Comment=%{summary}
Exec=%{name}.sh
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
MimeType=application/x-%{name};
Categories=Audio;X-Sound
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.txt
%{_bindir}/%{name}.sh
%{_javadir}/*.jar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/grammars
%{_datadir}/%{name}/grammars/*
%dir %{_datadir}/%{name}/leadsheets
%{_datadir}/%{name}/leadsheets/*
%dir %{_datadir}/%{name}/styles
%{_datadir}/%{name}/styles/*
%dir %{_datadir}/%{name}/styleExtract
%{_datadir}/%{name}/styleExtract/*
%dir %{_datadir}/%{name}/vocab
%{_datadir}/%{name}/vocab/*
%dir %{_datadir}/%{name}/connectomes
%{_datadir}/%{name}/connectomes/*
%dir %{_datadir}/%{name}/midi
%{_datadir}/%{name}/midi/*
%dir %{_datadir}/%{name}/voicings
%{_datadir}/%{name}/voicings/*
%dir %{_datadir}/%{name}/transforms
%{_datadir}/%{name}/transforms/*
%dir %{_datadir}/%{name}/fractals
%{_datadir}/%{name}/fractals/*
%dir %{_datadir}/%{name}/counts
%{_datadir}/%{name}/counts/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Oct 25 2017 Yann Collette <ycollette dot nospam at free.fr> 9.10
- upgrade to 9.10

* Sat Jun 06 2015 Yann Collette <ycollette dot nospam at free.fr> 7.00
- upgrade to 7.00

* Thu Jun 14 2012 Neal <nealbrks0 at gmail.com> 5.11-2pclos2012
- rebuild

* Fri Apr 13 2012 Neal <nealbrks0 at gmail.com> 5.11-1pclos2012
- process

* Mon Mar 26 2012 Galen Seaman <gseaman@clear.net> 5.11-1pclos2012
- update 5.11

* Wed Sep 01 2010 Galen Seaman <gseaman2186@comcast.net> 4.12-1pclos2010
- update 4.12

* Sat Jun 12 2010 Galen Seaman <gseaman2186@comcast.net> 4.11-2pclos2010
- update 4.11

* Fri Aug 21 2009 Texstar <texstar@gmail.com> 4.06-2pclos2009
- fix rpm group

* Fri Aug 07 2009 Galen Seaman <gseaman2186@comcast.net> ???
- updated to 4.06 and adapted for PCLinuxOS

* Mon Jun 02 2008 Toni Graffy <toni@links2linux.de> - 3.39-0.pm.1
- update to 3.39

