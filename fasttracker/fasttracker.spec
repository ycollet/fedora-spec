Name:          fasttracker2
Version:       1.05
Release:       1%{?dist}
Summary:       Module tracker software for creating music
Group:         Applications/Multimedia
License:       GPLv3+
URL:           https://16-bits.org/ft2.php
Source0:       https://github.com/8bitbubsy/ft2-clone/archive/v%{version}.tar.gz#/ft2-clone-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake

%description
FastTracker 2 is a music tracker created by Fredrik "Mr. H" Huss and Magnus "Vogue" Högdahl, two members of the demogroup Triton
(who later founded Starbreeze Studios) which set about releasing their own tracker after breaking into the scene in 1992 and winning several demo competitions.
The source code of FastTracker 2 is written in Pascal using Borland Pascal 7 and TASM. The program works natively under MS-DOS.

%prep
%setup -qn ft2-clone-%{version}

%build

mkdir -p build
cd build
%cmake -DCMAKE_BUILD_TYPE=RELEASE ..

make %{?_smp_mflags}

%install

mkdir -p %{buildroot}%{_bindir}/
cp release/other/ft2-clone %{buildroot}%{_bindir}/ft2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSES.txt
%{_bindir}/ft2

%changelog
* Sun Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.05-1
- update to 1.05

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.01-1
- update to 1.01

* Sat Aug 17 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b166-1
- update to 0.1b166

* Mon Aug 5 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b164-1
- update to 0.1b164

* Thu Feb 21 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b137-1
- initial spec file
