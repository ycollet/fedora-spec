# Global variables for github repository
%global commit0 c6b6e3ab02d7ec1e93edeeb8042a89a561924826
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    jamulus
Version: 3.5.5
Release: 4%{?dist}
Summary: Jamulus
URL:     https://github.com/corrados/jamulus/
Group:   Applications/Multimedia

Obsoletes: Jamulus <= 3.5.3-3

License: GPLv2

# original tarfile can be found here:
Source0: https://github.com/corrados/jamulus/archive/%{commit0}.tar.gz#/jamulus-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: opus-devel
BuildRequires: desktop-file-utils

%description
The Jamulus software enables musicians to perform real-time jam sessions over the internet.
There is a Jamulus server which collects the audio data from each Jamulus client,
mixes the audio data and sends the mix back to each client.

%prep
%setup -qn jamulus-%{commit0}

%build

# optflags   %{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection
#  -fcf-protection produce an error in an object generatoin ...

qmake-qt5 Jamulus.pro \
	  QMAKE_CFLAGS_DEBUG="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection" \
	  QMAKE_CFLAGS_RELEASE="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection" \
	  QMAKE_CXXFLAGS_DEBUG="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection" \
	  QMAKE_CXXFLAGS_RELEASE="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection" \
	  CONFIG+=opus_shared_lib 

%make_build VERBOSE=1

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 Jamulus %{buildroot}%{_bindir}/jamulus

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 distributions/jamulus.desktop %{buildroot}%{_datadir}/applications/

%__install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
%__install -m 644 distributions/jamulus.png %{buildroot}%{_datadir}/pixmaps/

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
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat May 30 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-4
- fix debug package

* Thu May 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-3
- compile with fedora opus package
- fix install

* Thu May 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-2
- fix an executable right problem

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-1
- update 3.5.5-1

* Mon May 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.4-1
- update 3.5.4-1

* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.3-1
- update 3.5.3-1

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.2-1
- update 3.5.2-1

* Mon Apr 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.1-1
- update 3.5.1-1

* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.0-1
- update 3.5.0-1

* Sun Apr 12 2020 Yann Collette <ycollette.nospam@free.fr> - 3.4.7-1
- update 3.4.7-1

* Tue Mar 31 2020 Yann Collette <ycollette.nospam@free.fr> - 3.4.4-1
- update 3.4.4-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1
- update for Fedora 29

* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.4.2-1

* Sat May 30 2015 Yann Collette <ycollette.nospam@free.fr> - 3.4.1-1
- Initial release
