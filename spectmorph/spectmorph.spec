Name:    spectmorph
Version: 0.4.1
Release: 1%{?dist}
Summary: SpectMorph is a free software project which allows to analyze samples of musical instruments, and to combine them (morphing)
URL:     http://www.spectmorph.org
Group:   Applications/Multimedia
Source0: http://www.spectmorph.org/files/releases/spectmorph-%{version}.tar.bz2
License: GPLv2+

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils
BuildRequires: lv2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libao-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: sed

%description
SpectMorph is a free software project which allows to analyze samples of musical instruments, and to combine them (morphing). It can be used to construct hybrid sounds, for instance a sound between a trumpet and a flute; or smooth transitions, for instance a sound that starts as a trumpet and then gradually changes to a flute. In its current version, SpectMorph ships with many ready-to-use instruments which can be combined using morphing. 

%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%setup -q -n %{name}-%{version}

sed -i -e "s/Icon=smjack.png/Icon=smjack/g" data/smjack.desktop
sed -i -e "s/Midi//g" data/smjack.desktop

%configure --prefix=%{_prefix} --with-lv2 --with-jack --with-qt --libdir=%{_libdir}

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%build

%{__make} DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} VERBOSE=1 %{?_smp_mflags}

%install

%{__make} DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} install

# install smjack.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/smjack.desktop

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
%doc AUTHORS COPYING README.md
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/*
%{_datadir}/man/*
%{_datadir}/pixmaps/*
%{_datadir}/spectmorph/*

%files devel
%{_includedir}/%{name}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update for Fedora 29
- update to 0.4.1

* Tue Apr 10 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- Initial release
