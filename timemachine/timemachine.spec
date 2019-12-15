# Global variables for github repository
%global commit0 5b663fb12afeb7e28d8c6e9aeafce73f4328c6ca
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Audio recorder
Name:    timemachine
Version: 0.3.4
Release: 2%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/swh/timemachine

Source0: https://github.com/swh/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: gtk2-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: liblo-devel
BuildRequires: lash-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: intltool

%description
I used to always keep a minidisc recorder in my studio running in a mode where
when you pressed record it wrote the last 10 seconds of audio to the disk and
then caught up to realtime and kept recording. The recorder died and haven't
been able to replace it, so this is a simple jack app to do the same job. It
has the advantage that it never clips and can be wired to any part of the jack
graph.

%prep
%setup -qn %{name}-%{commit0}

# Force wav as the default format
sed -i -e "s/w64/wav/g" src/main.h

%build
./autogen.sh
./configure --prefix=%{_prefix}
%{__make} DESTDIR=%{buildroot} %{_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/timemachine.desktop << EOF
[Desktop Entry]
Name=timemachine
Comment=Audio recorder.
Exec=/usr/bin/timemachine
Type=Application
Terminal=0
Icon=/usr/share/timemachine/pixmaps/timemachine-icon.png
Categories=AudioVideo;
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*

%changelog
* Sun Dec 15 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.4-3
- Set default format to wav instead of w64 / remove fedora flags which make tm hangs 

* Wed Aug 21 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.4-2
- Set default format to wav instead of w64

* Thu May 9 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.4-1
- Initial spec file
