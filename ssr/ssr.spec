# Global variables for github repository
%global commit0 4cce5de6507ac91c9befc3cffa6afef73425f2a7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Simple Screen Recorder
Name: ssr
Version: 0.3.6.%{shortcommit0}
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL:            https://github.com/MaartenBaert/ssr
Source0:        https://github.com/MaartenBaert/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt4-devel
BuildRequires: ffmpeg-devel
BuildRequires: pulseaudio-libs-devel

%description
SimpleScreenRecorder is a Linux program created to record programs and games. 

%prep
%setup -qn %{name}-%{commit0}

%build

%configure
%{__make} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category X-Video \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/simplescreenrecorder.desktop


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

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS.md CHANGELOG.md COPYING README.md
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*


%changelog
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.3.6-1
- Initial release of spec fil to 0.3.6
