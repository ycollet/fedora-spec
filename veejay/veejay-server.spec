%global debug_package %{nil}

# Global variables for github repository
%global commit0 6a7202284a2a5af9144e76505f948c4df6127c44
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    veejay-server
Version: 1.5.57
Release: 2%{?dist}
Summary: A 'visual' instrument and realtime video sampler (for live video improvisation) - server part
URL:     https://github.com/c0ntrol/veejay
Group:   Applications/Multimedia

License: GPLv2+

Source0: https://github.com/c0ntrol/veejay/archive/%{commit0}.tar.gz#/veejay-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ sed
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gtk2-devel
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: libjpeg-devel
BuildRequires: ffmpeg-devel
BuildRequires: libX11-devel
BuildRequires: libxml2-devel
BuildRequires: SDL-devel
BuildRequires: qrencode-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: freetype-devel
BuildRequires: liblo-devel
BuildRequires: libv4l-devel
BuildRequires: libglade2-devel
BuildRequires: compat-ffmpeg28-devel
BuildRequires: gmic-devel
BuildRequires: chrpath

%description
Veejay is a Visual Instrument

A 'visual' instrument and realtime video sampler (for live video improvisation)
It allows you to "play" the video like you would play a piano.
While playing, you can record the resulting video directly to disk (video sampling), all effects are realtime and optimized for use on modern processors.
Veejay likes the sound of your video's as much as their images: sound is kept in sync ( pitched when needed - trickplay) and delivered to [JACK](http://www.jackaudio.org/) for possible further processing.
You can cluster to allow a number of machines to work together over the network (uncompressed streaming, veejay chaining) And much more...
The engine is historically based upon mjpegtools's lavplay and processes all video in YUV planar It performs at its best, currently with MJPEG AVI (through ffmpeg/libav) or one of veejay's internal formats. Veejay is built upon a servent architecture.

%prep
%setup -qn veejay-%{commit0}

find . -name "*.c" ! -name vj-vloopback.c ! -name v4l2utils.c -exec sed -i -e "s/PIX_FMT/AV_PIX_FMT/g" {} \;

%build

export LIBAVUTIL_CFLAGS=-I/usr/include/compat-ffmpeg28
export LIBAVCODEC_CFLAGS=-I/usr/include/compat-ffmpeg28
export LIBAVFORMAT_CFLAGS=-I/usr/include/compat-ffmpeg28
export LIBSWSCALE_CFLAGS=-I/usr/include/compat-ffmpeg28
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig

cd veejay-current
cd veejay-server
./autogen.sh
./configure --prefix=%{_prefix} --libdir=%{_libdir} 

sed -i -e "s/libpng16/freetype/g" config.h
find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%{__make} DESTDIR=%{buildroot} %{_smp_mflags} CFLAGS=-I/usr/include/compat-ffmpeg28 LDFLAGS=-L/usr/lib64/compat-ffmpeg28/
%{__make} DESTDIR=%{buildroot} install

cd ../..

%install

cd veejay-current
cd veejay-server
%{__make} DESTDIR=%{buildroot} install CFLAGS="-I/usr/include/compat-ffmpeg28 -I%{buildroot}%{_includedir}" LDFLAGS="-L/usr/lib64/compat-ffmpeg28/ -L%{buildroot}%{_libdir}"
cd ../..

#chrpath --delete $RPM_BUILD_ROOT/usr/bin/reloaded
#chrpath --delete $RPM_BUILD_ROOT/usr/bin/sayVIMS
#chrpath --delete $RPM_BUILD_ROOT/usr/bin/veejay

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
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*
%{_includedir}/*

%changelog
* Sun Nov 17 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-2
- fix illegal instruction pb

* Sat Nov 16 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-1
- Initial spec file
