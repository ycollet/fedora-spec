# Global variables for github repository
%global commit0 a82fff059baafc03f7c0e8b9a99f383af7bfbd79
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:           DISTRHO-Ports
Version:        1.0.0.%{shortcommit0}
Release:        3%{?dist}
Summary:        A set of LV2 plugins

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/DISTRHO/DISTRHO-Ports
Source0:        https://github.com/DISTRHO/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        http://downloads.sourceforge.net/premake/premake-linux-3.7.tar.gz

BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
# For premake
%ifarch x86_64 amd64
BuildRequires: glibc(x86-32)
%endif

%description
A set of LV2 plugins

%prep
%setup -qn %{name}-%{commit0}

%build

tar xvfz %SOURCE1
export PATH=`pwd`:$PATH
./scripts/premake-update.sh linux
make PREFIX=/usr LIBDIR=/usr/lib64 DESTDIR=%{buildroot} lv2 %{?_smp_mflags}

%install 
make PREFIX=/usr LIBDIR=/usr/lib64 DESTDIR=%{buildroot} lv2 %{?_smp_mflags} install

rm -rf %{buildroot}/usr/src

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
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_libdir}/lv2/*

%changelog
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update to a82fff059baafc03f7c0e8b9a99f383af7bfbd79
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-2
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
