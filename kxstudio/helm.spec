%global debug_package %{nil}

# Global variables for github repository #6dbcd64ba122c2fe1342962c51744b7663925658
%global commit0 927d2ed27f71a735c3ff2a1226ce3129d1544e7e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           helm
Version:        1.0.0.%{shortcommit0}
Release:        1%{?dist}
Summary:        A LV2 / standalone synth

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/mtytel/helm
Source0:        https://github.com/mtytel/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
#Patch0:         helm-0001-fix-type-problem.patch

BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel

%description
A LV2 / standalone synth

%prep
%setup -qn %{name}-%{commit0}
#%patch0 -p1

sed -i "s/\/lib\//\/lib64\//g" Makefile

%build
make DESTDIR=%{buildroot} standalone lv2 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} standalone lv2 %{?_smp_mflags} install

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
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/lxvst/*
%{_datadir}/helm/*
%{_datadir}/doc/helm/*
%{_mandir}/man1/helm.1.gz
%{_datadir}/applications/helm.desktop
%{_datadir}/icons/hicolor/*

%changelog
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
