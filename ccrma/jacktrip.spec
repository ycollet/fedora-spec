# Global variables for github repository
%global commit0 49c3dff7f286df007129eb7db029423559b35ef3
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Multimachine jam sessions over the internet
Name:    jacktrip
Version: 1.1.0
Release: 2%{?dist}
License: STK
Group:   Applications/Multimedia
URL:     https://ccrma.stanford.edu/software/jacktrip/
Source0: https://github.com//jacktrip/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

BuildRequires: gcc gcc-c++
BuildRequires: qt4-devel
BuildRequires: jack-audio-connection-kit-devel alsa-lib-devel

%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming. You
can use it between any combination of Linux and Mac OS X (i.e., one
end using Linux can connect to the other using Mac OS X).

It is currently being developed and actively tested at CCRMA by the
SoundWIRE group.

%prep
%setup -qn %{name}-%{commit0}

%build
cd jacktrip/src
./build
%{__make}

%install
%{__rm} -rf %{buildroot}
cd jacktrip/src
%{__mkdir} -p %{buildroot}%{_bindir}
%{__make} INSTALL_ROOT=%{buildroot} release-install

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc jacktrip/CHANGESLOG.txt jacktrip/TODO.txt jacktrip/INSTALL.txt
%{_bindir}/jacktrip

%changelog
* Fri May 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-2
- update 1.1.0

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Thu Sep 13 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.5-2
- add patch to fix build on Fedora 17 (gcc4.7)

* Wed Feb 18 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.5-2
- add patch to activate ports on the server without a client connection

* Wed Feb 18 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.5-1
- updated to 1.0.5, added patch for gcc44 build on fc11

* Wed Feb 18 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.4-1
- updated to 1.0.4

* Wed Jan  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.3-1
- updated to 1.0.3, enable build on x86_64

* Tue Oct  7 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.2-0.1alpha
- updated to latest alpha release (1.0.2-alpha)
- build only on i386 for now

* Wed Jul  9 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- fix building on CentOS

* Wed Jul  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- use qt3-devel when building on fc9
- add patch for building with gcc4.3

* Tue Oct 09 2007 Juan-Pablo Caceres <jcaceres@ccrma.Stanford.EDU> - 0.27-1
- new version 0.27

* Fri Oct 05 2007 Juan-Pablo Caceres <jcaceres@ccrma.Stanford.EDU> - 0.26-1
- new version 0.26, without qwt dependency

* Mon Feb 19 2007 Juan-Pablo Caceres <jcaceres@ccrma.Stanford.EDU> - 0.25-1
- modified names and version

* Thu Jul 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 25-1
- initial build.
