# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 ba9aee218dd4a9cfab914ad78bdb6d59e9a37400
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    fluxus
Version: 0.17rc5.%{shortcommit0}
Release: 1%{?dist}
Summary: A 3D game engine for livecoding worlds into existence
URL:     http://pawfal.org/fluxus/
Group:   Applications/Multimedia

License: GPLv2+

Source0: https://gitlab.com/nebogeo/%{name}/-/archive/%{commit0}/fluxus-%{commit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: python2-scons
BuildRequires: ode-devel >= 0.9
BuildRequires: racket-devel >= 5.1.1
BuildRequires: racket >= 5.1.1
BuildRequires: fftw-devel >= 3.2.2
BuildRequires: jack-audio-connection-kit-devel >= 1.9.7
BuildRequires: libsndfile-devel >= 1.0.25
BuildRequires: liblo-devel >= 0.26
BuildRequires: glew-devel >= 1.5.8
BuildRequires: freetype-devel >= 2.2.4
BuildRequires: python2-scons
BuildRequires: libjpeg-turbo-devel >= 1.1.1
BuildRequires: libpng-devel >= 1.2.46
BuildRequires: libtiff-devel >= 3.9.5
BuildRequires: zlib-devel >= 1.2.3
BuildRequires: freeglut-devel >= 2.6.0
BuildRequires: alsa-lib-devel >= 1.0.24
BuildRequires: openal-soft-devel >= 1.12.854
BuildRequires: gstreamer-devel >= 0.10.25
BuildRequires: gstreamer-plugins-base-devel >= 0.10.25
BuildRequires: gstreamer-plugins-good-devel >= 0.10.17
BuildRequires: gstreamer-plugins-bad-free-devel >= 0.10.22
BuildRequires: libunicap-devel >= 0.9.12
BuildRequires: ffmpeg-devel >= 0.7
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils

Requires: racket >= 5.1.1
Requires: fftw >= 3.2.2
Requires: jack-audio-connection-kit >= 1.9.7
Requires: libsndfile >= 1.0.25
Requires: liblo >= 0.26
Requires: glew >= 1.5.8
Requires: freetype >= 2.2.4
Requires: libjpeg-turbo >= 1.1.1
Requires: libpng >= 1.2.46
Requires: libtiff >= 3.9.5
Requires: zlib >= 1.2.3
Requires: freeglut >= 2.6.0
Requires: alsa-lib >= 1.0.24
Requires: openal-soft >= 1.12.854
Requires: gstreamer >= 0.10.25
Requires: gstreamer-plugins-base >= 0.10.25
Requires: gstreamer-plugins-good >= 0.10.17
Requires: gstreamer-plugins-bad-free >= 0.10.22
Requires: libunicap >= 0.9.12
Requires: ffmpeg >= 0.7

%description
A rapid prototyping, livecoding and playing/learning environment for 3D
graphics, sound and games. Extends Racket with graphical commands
and can be used within it’s own livecoding environment or from within
the DrRacket IDE. Web Page: http://www.pawfal.org/fluxus/

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/\/lib\/racket/\/%{_lib}\/racket/g" SConstruct
sed -i -e "s/FluxusCollectsLocation = Prefix + \"\/lib\"/FluxusCollectsLocation = Prefix + \"\/%{_lib}\"/g" SConstruct

%build

#cd docs
#./makehelpmap.scm

%install
scons-2 -Q install DESTDIR="%{buildroot}" Prefix=/usr RacketPrefix=/usr
install -m 644 -D modules/material/textures/fluxus-icon.png %{buildroot}/usr/share/pixmaps/fluxus-icon.png
install -m 644 -D debian/fluxus.desktop %{buildroot}/usr/share/applications/fluxus.desktop

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/fluxus.desktop

%post
chcon -t textrel_shlib_t '/usr/lib/fluxus-018/compiled/native/i386-linux/3m/fluxus-engine_ss.so'
semanage fcontext -a -t textrel_shlib_t '/usr/lib/fluxus-018/compiled/native/i386-linux/3m/fluxus-engine_ss.so'

touch --no-create %{_datadir}/mime/packages &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/fluxus
%{_bindir}/fluxa
%{_libdir}/fluxus-019/*
%{_datadir}/fluxus-019/*
%{_docdir}/fluxus-019/*
%{_datadir}/pixmaps/fluxus-icon.png
%{_datadir}/applications/fluxus.desktop

%changelog
* Tue Nov 19 2019 Yann Collette <ycollette.nospam@free.fr> - 0.17rc5-1
- Initial release of the spec file
