# Disable production of debug package. Problem with fedora 23
# %global debug_package %{nil}

Name:    lebiniou
Version: 3.40
Release: 2%{?dist}
Summary: Lebiniou is an audio spectrum visualizer
URL:     https://biniou.net/
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://gitlab.com/lebiniou/lebiniou/-/archive/version-%{version}/lebiniou-version-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ make sed
BuildRequires: autoconf automake libtool
BuildRequires: pulseaudio-libs-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libcaca-devel
BuildRequires: fftw-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: freetype-devel
BuildRequires: pandoc
BuildRequires: libsndfile-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: ImageMagick-devel
BuildRequires: ffmpeg-devel
BuildRequires: perl-podlators
BuildRequires: gtk-update-icon-cache

Requires(pre): lebiniou-data

%description

As an artist, composer, VJ or just fan, lebiniou allows you to create live visuals based on your audio performances or existing tracks.
As a listener, lebiniou allows you to watch an everlasting and totally unseen creation reacting to the music.

%prep
%setup -qn %{name}-version-%{version}

sed -i -e "s/LEBINIOU_LIBDIR=\"\$prefix\/lib\"/LEBINIOU_LIBDIR=\"\$prefix\/%{_lib}\"/g" configure.ac

%build

autoreconf --install

# report: --enable-jackaudio doesn't work ...
%configure --prefix=%{_prefix} --enable-alsa --enable-pulseaudio --enable-sndfile --enable-caca --libdir=%{_libdir} CFLAGS="%{build_cxxflags}"

make %{?_smp_mflags} 

%install

make %{?_smp_mflags} DESTDIR=%{buildroot} install

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans 
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README.md AUTHORS ChangeLog THANKS
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Mon Feb 17 2020 Yann Collette <ycollette.nospam@free.fr> - 3.40-2
- update to 3.40

* Fri Dec 6 2019 Yann Collette <ycollette.nospam@free.fr> - 3.32-2
- fix path

* Fri Dec 6 2019 Yann Collette <ycollette.nospam@free.fr> - 3.32-1
- update to 3.32

* Fri May 17 2019 Yann Collette <ycollette.nospam@free.fr> - 3.31-1
- initial spec file
