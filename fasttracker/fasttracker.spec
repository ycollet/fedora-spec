Name:          fasttracker2
Version:       0.1b137
Release:       1%{?dist}
Summary:       Module tracker software for creating music
Group:         Applications/Multimedia
License:       GPLv3+
URL:           https://16-bits.org/ft2.php
Source0:       https://16-bits.org/ft2clone-b137-code.zip
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake

%description
FastTracker 2 is a music tracker created by Fredrik "Mr. H" Huss and Magnus "Vogue" Högdahl, two members of the demogroup Triton
(who later founded Starbreeze Studios) which set about releasing their own tracker after breaking into the scene in 1992 and winning several demo competitions.
The source code of FastTracker 2 is written in Pascal using Borland Pascal 7 and TASM. The program works natively under MS-DOS.

%prep
%setup -qn ft2-clone-code

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
* Thu Feb 21 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b137-1
- initial spec file
