%global debug_package %{nil}

# Global variables for github repository
%global commit0 355f0243480dde6c691e783489793eb445a88967
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           amuc
Version:        1.7.%{shortcommit0}
Release:        2%{?dist}
Summary:        Amuc - the Amsterdam Music Composer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/pjz/amuc.git
Source0:        https://github.com/pjz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         amuc-0001-fix-build-with-gcc-7.patch
Patch1:         amuc-0002-add-missing-library.patch

BuildRequires: alsa-lib-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: cairo-devel
BuildRequires: jack-audio-connection-kit-devel

%description
Amuc - the Amsterdam Music Composer

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1 
%patch1 -p1 

%build

make 

%install 

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 src/amuc %{buildroot}/%{_bindir}/
%__install -m 644 src-abcm2ps/abcm2ps %{buildroot}/%{_bindir}/
%__install -m 644 src-wav2score/wav2score %{buildroot}/%{_bindir}/
%__install -m 644 src-tr-sco/tr-sco %{buildroot}/%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/amuc/samples/
%__install -m 644 samples/* %{buildroot}/%{_datadir}/amuc/samples/
%__install -m 755 -d %{buildroot}/%{_datadir}/amuc/samples/
%__install -m 644 samples/* %{buildroot}/%{_datadir}/amuc/samples/
%__install -m 644 tunes/* %{buildroot}/%{_datadir}/amuc/
%__install -m 755 -d %{buildroot}/%{_mandir}/man1/
%__install -m 644 doc/amuc.1 %{buildroot}/%{_mandir}/man1/
%__install -m 755 -d %{buildroot}/%{_docdir}/amuc/
%__install -m 644 doc/* %{buildroot}/%{_docdir}/amuc/
rm %{buildroot}/%{_docdir}/amuc/amuc.1

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
%{_datadir}/amuc/*
%{_docdir}/amuc/*
%{_mandir}/man1/*

%changelog
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.7
- initial release
