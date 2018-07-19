# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:          Jamulus
Version:       3.4.3
Release:       1%{?dist}
Summary:       Jamulus
URL:           http://llcon.sourceforge.net/
Group:         Applications/Multimedia

License:       GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

# original tarfile can be found here:
Source0:       http://downloads.sourceforge.net/project/llcon/Jamulus/3.4.3/Jamulus-3.4.3.tar.gz

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt4-devel
BuildRequires: desktop-file-utils

%description
The Jamulus software enables musicians to perform real-time jam sessions over the internet.
There is a Jamulus server which collects the audio data from each Jamulus client,
mixes the audio data and sends the mix back to each client.

%prep
%setup -q -c %{name}

%build

cd %{name}%{version}
%_qt4_qmake Jamulus.pro

make VERBOSE=1 %{?_smp_mflags}

%install

cd %{name}%{version}

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 644 %{name} %{buildroot}%{_bindir}/jamulus

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 src/res/jamulus.desktop %{buildroot}%{_datadir}/applications/

desktop-file-install --vendor '' \
        --add-category=Audio \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/jamulus.desktop

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
%{_datadir}/applications/*

%changelog
* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.4.2-1
* Sat May 30 2015 Yann Collette <ycollette.nospam@free.fr> - 3.4.1-1
- Initial release
