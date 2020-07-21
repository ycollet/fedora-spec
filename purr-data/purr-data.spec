# Maintainer: <aggraef at gmail.com>

# This is Jonathan Wilkes' nw.js variant of Pd-L2Ork nick-named "Purr-Data".
# Basically, it is Pd-L2Ork with the Tk GUI replaced with a JavaScript GUI
# implemented using nw.js (http://nwjs.io/). **NOTE:** The flite (speech
# synthesis) external isn't included right now, as I couldn't find a suitable
# flite package in openSUSE. Other than that, it's basically the same package
# as the one available in the Arch User Repositories (also maintained by yours
# truly). In particular, it renames the executable and library directories so
# that it can be installed alongside pd-l2ork.

# We use a custom install prefix here so that the package can be installed
# alongside classic pd-l2ork.
%define prefix /opt/purr-data

# Extra build options: E.g., you can use 'light' instead of 'all' for a light
# build (only essential externals).
%define buildopt all

# nw.js version and architecture
%define nwjs_version 0.24.4
%ifarch x86_64
%define nwjs_arch x64
%else
%define nwjs_arch ia32
%endif

# XXXFIXME: Debianism. We use that version number for convenience here since
# we actually use the Debian snapshot (.orig tarball) to build the package. Is
# there a versioning scheme for git packages in RPM land that we should use?
Name:    purr-data
Version: 2.12.0
Release: 1%{?dist}
Summary: Interactive multimedia programming environment (nw.js variant)
URL:     https://agraef.github.io/purr-data/
License: GPL

# git clone https://github.com/agraef/purr-data
# cd purr-data
# git ckeckout 2.12.0
# git submodule init
# git submodule update
## find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz purr-data.tar.gz purr-data

Source0: purr-data.tar.gz
Source1: https://dl.nwjs.io/v%{nwjs_version}/nwjs-sdk-v%{nwjs_version}-linux-%{nwjs_arch}.tar.gz
Source2: Makefile

BuildRequires: gcc-c++
BuildRequires: autoconf automake libtool bison flex rsync
BuildRequires: libtirpc-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: python3-devel
BuildRequires: ladspa-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: bluez-libs-devel
BuildRequires: cairo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: glew-devel
BuildRequires: gsl-devel
BuildRequires: ImageMagick-c++-devel
BuildRequires: libdc1394-devel
BuildRequires: fftw-devel
BuildRequires: fluidsynth-devel
BuildRequires: ftgl-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: lua-devel
BuildRequires: lame-devel
BuildRequires: libquicktime-devel
BuildRequires: libraw1394-devel
BuildRequires: speex-devel
BuildRequires: stk-devel
BuildRequires: libtiff-devel
BuildRequires: libv4l-devel
BuildRequires: libdv-devel
BuildRequires: libiec61883-devel
BuildRequires: libXv-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libvorbis-devel
BuildRequires: zlib-devel
BuildRequires: GConf2-devel
BuildRequires: nss-devel
BuildRequires: libXtst-devel
BuildRequires: flite-devel

Requires: xdg-utils
Requires: pulseaudio-utils
Requires: ladspa-tap-plugins
Requires: ladspa-swh-plugins
Requires: ladspa-mcp-plugins
Requires: ladspa-cmt-plugins
Requires: ladspa-blop-plugins
Requires: ladspa-VCO-plugins
Requires: ladspa-fil-plugins
Requires: mda-lv2
Requires: dssi

#Requires: ladspa-foo-plugins
#Requires: ladspa-invada-studio-plugins
#Requires: ladspa-blepvco
#Requires: ladspa-omins
#Requires: ladspa-WAH

#Suggests: python, fluid-soundfont-gm

%description
This is Jonathan Wilkes' nw.js variant of Pd-L2Ork, nick-named
"Purr-Data". Basically, it is Pd-L2Ork with the Tk GUI replaced
with a JavaScript GUI implemented using nw.js (http://nwjs.io/).

Pd-L2Ork is Linux Laptop Orchestra's (L2Ork) real-time visual
programming environment for interactive multimedia. It is based
on Miller Puckette's Pure Data (Pd).

%prep
%autosetup -n purr-data

# copy the nw.js sources to where purr-data wants them
rm -rf pd/nw/nw
mkdir -p pd/nw/nw
tar xvfz %{SOURCE1} -C pd/nw/nw --strip-components 1
cp %{SOURCE2} .

%build

%set_build_flags

# %make_build prefix=%{prefix}  %{buildopt}
make prefix=%{prefix}  %{buildopt}

%install

make prefix=%{prefix}

# Create a link to the executable.
mkdir -p "%{buildroot}/usr/bin"
ln -sf %{prefix}/bin/pd-l2ork "%{buildroot}/usr/bin/purr-data"
# Create links to the include and lib directories.
mkdir -p "%{buildroot}/usr/include"
ln -sf %{prefix}/include/pd-l2ork "%{buildroot}/usr/include/purr-data"
mkdir -p "%{buildroot}/usr/%{_lib}"
ln -sf %{prefix}/lib/pd-l2ork "%{buildroot}/usr/%{_lib}/purr-data"
# Edit bash completion file.
sed -e 's/pd-l2ork/purr-data/g' < "%{buildroot}/etc/bash_completion.d/pd-l2ork" > "%{buildroot}/etc/bash_completion.d/purr-data"
rm -f "%{buildroot}/etc/bash_completion.d/pd-l2ork"
# For now we just remove the Emacs mode as it will conflict with the
# pd-l2ork package.
rm -rf "%{buildroot}/usr/share/emacs"
# Edit the library paths in the default user.settings file so that it
# matches our install prefix.
cd "%{buildroot}%{prefix}/lib/pd-l2ork"
sed -e "s!/usr/lib/pd-l2ork!%{prefix}/lib/pd-l2ork!g" -i default.settings
# Replace the pd-l2ork desktop/mime files and icons with purr-data ones, so
# that pd-l2ork can be installed alongside purr-data. Also fix up some
# glitches in the desktop files to make brp-suse.d/brp-30-desktop happy, which
# is *very* picky about categories. We also remove the K12 desktop files which
# aren't needed since K12 mode is not supported by purr-data (yet).
cd "%{buildroot}/usr/share/applications"
sed -e 's/pd-l2ork/purr-data/g' -e 's/Pd-L2Ork/Purr-Data/g' -e 's/[.]xpm//g' -e 's/AudioVideo;Audio;/AudioVideo;Audio;Midi;/g' < pd-l2ork.desktop > purr-data.desktop
sed -e 's/pd-l2ork/purr-data/g' -e 's/Pd-L2Ork/Purr-Data/g' -e 's/[.]xpm//g' -e 's/AudioVideo;Audio;/AudioVideo;Audio;Midi;/g' < pd-l2ork-debug.desktop > purr-data-debug.desktop
rm -f pd-l2ork*.desktop
cd "%{buildroot}/usr/share/mime/packages"
sed -e 's/pd-l2ork/purr-data/g' < pd-l2ork.xml > purr-data.xml
rm -f pd-l2ork.xml
cd "%{buildroot}/usr/share/icons/hicolor/128x128/apps/"
rm -f pd-l2ork-k12*.png
mv pd-l2ork.png purr-data.png
mv pd-l2ork-red.png purr-data-red.png
cd "%{buildroot}/usr/share/icons/hicolor/128x128/mimetypes/"
mv text-x-pd-l2ork.png text-x-purr-data.png
# Remove libtool archives and extra object files.
cd "%{buildroot}%{prefix}"
rm -f lib/pd-l2ork/extra/*/*.la lib/pd-l2ork/extra/*/*.pd_linux_o
# Sanitize permissions.
cd "%{buildroot}"
chmod -R go-w *
chmod -R a+r *
chmod a-x .%{prefix}/lib/pd-l2ork/default.settings
find .%{prefix}/lib/pd-l2ork/bin/nw -executable -not -type d -exec chmod a+x {} +
#find . -executable -name '*.pd_linux' -exec chmod a-x {} +
find . -executable -name '*.pd' -exec chmod a-x {} +
find . -executable -name '*.txt' -exec chmod a-x {} +
find . -executable -name '*.aif*' -exec chmod a-x {} +
find . -type d -exec chmod a+x {} +

%files
%doc README.md
%license LICENSE.md
/opt/purr-data/*
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_data_dir}/

%changelog
* Tue Jul 21 2020 Yann Collette <ycollette.nospam@free.fr> - 2.12.0-1
- changes for Fedora

* Sat Aug 24 2019 Albert Graef <aggraef@gmail.com>
- Initial release
