# Global variables for github repository
%global commit0 5e807a87cfad84c648d873107bfc91eef3648a4a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    stretchplayer
Version: 0.0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Variable speed audio plater
URL:     https://github.com/smbolton/stretchplayer
Group:   Applications/Multimedia
License: GPLv2+


Source0: https://github.com/smbolton/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  stretchplayer-fix-cast.patch
Patch1:  stretchplayer-remove-inline.patch
Patch2:  stretchplayer-disable-mpg123.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt4-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: rubberband-devel

%description
StretchPlayer is an audio file player that allows you to change the
speed of the song without changing the pitch.  It will also allow you
to transpose the song to another key (while also changing the speed).
This is a very powerful tool for musicians who are learning to play a
pre-recorded song.  You can:

 * Time Stretch (50% to 150% of song speed)
 * Pitch shift (up or down 1 octave)
 * A/B repeat

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1 
%patch1 -p1 
%patch2 -p1 

%build

%cmake .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=X-Jack \
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
%doc AUTHORS ChangeLog README.txt INSTALL.txt BUGS.txt
%license COPYING*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/icons/*
%exclude %{_datadir}/%{name}/%{name}.desktop

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- update for Fedora 29

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial release
