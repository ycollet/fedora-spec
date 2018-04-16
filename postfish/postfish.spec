%global debug_package %{nil}
%define revision 19609

Name:         postfish
Version:      %{revision}.svn
Release:      2%{?dist}
Summary:      The Postfish is a digital audio post-processing, restoration, filtering and mixdown tool.
Group:        Applications/Multimedia
License:      GPLv2+

URL:          https://svn.xiph.org/trunk/postfish
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 19609 https://svn.xiph.org/trunk/postfish postfish-19609
#  tar cvfz postfish-19609.tar.gz postfish-19609

Source0:      postfish-%{revision}.tar.gz
Source1:      postfish.png

BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: libao-devel
BuildRequires: gzip
BuildRequires: perl

%description
The Postfish is a digital audio post-processing, restoration, filtering and mixdown tool.
It works as a linear audio filter, much like a rack of analog effects.
The first stage of the filter pipeline provides a bank of configurable per-channel processing filters for up to 32 input channels.
The second stage provides mixdown of the processed input audio into a group of up to eight output channels.
The third stage applies processing filters to the output group post-mixdown.

The Postfish is a stream filter; feed it audio from a list of files or input stream, and it renders audio to standard out, as well as
optionally providing a configurable audio playback monitor via a sound device.
If the input audio is being taken from files, Postfish also provides simple forward/back/cue seeking and A-B looping control.
The next major update of Postfish will also include automation to allow mixdown settings to be 'recorded' and applied automatically during rendering.

%prep
%setup -qn postfish-%{revision}

%build

sed -i -e "s/PREFIX=\/usr\/local/PREFIX=\/usr/g" Makefile
make VERBOSE=1 %{?_smp_mflags}

%install

mkdir -p %{buildroot}%{_sysconfdir}/postfish/
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/man/man1/
mkdir -p %{buildroot}%{_datadir}/applications/

install -m 755 postfish %{buildroot}%{_bindir}/
install -m 644 %{S:1} %{buildroot}%{_datadir}/pixmaps/postfish.png
install -m 644 postfish.1 %{buildroot}%{_datadir}/man/man1/postfish.1
gzip %{buildroot}%{_datadir}/man/man1/postfish.1
install -m 644 postfish-wisdomrc %{buildroot}%{_sysconfdir}/postfish-wisdomrc

cat > %{buildroot}%{_datadir}/applications/postfish.desktop << EOF
[Desktop Entry]
Name=PostFish
Comment=Digital audio post-processing tool.
Exec=/usr/bin/postfish
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/postfish.png
Categories=AudioVideo;
EOF

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/*
%{_sysconfdir}/*

%changelog
* Wed Sep 13 2017 Yann Collette <ycollette.nospam@free.fr> - Initial version
- Initial version
