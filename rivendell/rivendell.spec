%global __python %{__python3}

# Global variables for github repository
%global commit0 cd80ab30049e711aa5b648c3fdb5621271cb2813
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: A radio automation system
Name:    rivendell
Version: 3.1.0
Release: 1%{?dist}
License: LGPL
Group:   Applications/Multimedia
URL:     https://github.com/ElvishArtisan/rivendell

Source0: https://github.com/ElvishArtisan//%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires: cdparanoia-devel
BuildRequires: id3lib-devel
BuildRequires: taglib-devel
BuildRequires: pam-devel
BuildRequires: soundtouch-devel
BuildRequires: gtk-update-icon-cache
BuildRequires: qt5-qtbase-devel
BuildRequires: qt-devel
BuildRequires: docbook-style-xsl
BuildRequires: autoconf automake libtool
BuildRequires: python3
BuildRequires: sed
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: expat-devel
BuildRequires: lame-devel
BuildRequires: libvorbis-devel
BuildRequires: libmad-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel

%description
Rivendell contains a full set of functionality needed to operate a radio
automation system

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/instdir = @LOCAL_PREFIX@\/lib/instdir = @LOCAL_PREFIX@\/%{_lib}/g" lib/Makefile.am

%build

./autogen.sh

# -Werror=format-security

CFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection'
export CFLAGS
CXXFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection'
export CXXFLAGS
FFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -I/usr/lib64/gfortran/modules'
export FFLAGS
FCFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -I/usr/lib64/gfortran/modules'
export FCFLAGS
LDFLAGS='-Wl,-z,relro  -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld'
export LDFLAGS

%configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-docbook
%{__make} DESTDIR=%{buildroot} %{?_smp_mflags}

%install

%{__make} DESTDIR=%{buildroot} install

%__install -m 755 -d %{buildroot}/usr/lib/systemd/system/
mv %{buildroot}/lib/systemd/system/rivendell.service %{buildroot}/usr/lib/systemd/system/rivendell.service

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%files
%defattr(-, root, root)
%doc AUTHORS INSTALL NEWS README ChangeLog UPGRADING
%license COPYING
%{_datadir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_bindir}/*
%{_sbindir}/*
%{_sysconfdir}/*
%{_includedir}/*
%{_unitdir}/*

%changelog
* Sat Sep 21 2019 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- initial release of the spec file
