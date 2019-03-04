# Disable production of debug package.
%global debug_package %{nil}

Summary: Tool for describing builds
Name:    premake4
Version: 4.4beta5
Release: 1%{?dist}
License: GPLv3+
Group:   Developpment
URL:     http://sourceforge.net/projects/premake/
Source0: https://sourceforge.net/projects/premake/files/Premake/4.4/premake-4.4-beta5-src.zip

BuildRequires: gcc gcc-c++

%description
Describe your software project with a full-featured scripting language and let Premake write the build scripts for you. With one file your project can support both IDE-addicted Windows coders and Linux command-line junkies!

%prep
%setup -qn premake-4.4-beta5

%build
cd build/gmake.unix/
make %{?_smp_mflags}

%install
%__install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/release/premake4 %{buildroot}/%{_bindir}/premake4

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc BUILD.txt CHANGES.txt LICENSE.txt README.txt
%{_bindir}/*

%changelog
* Mon Mar 4 2019 Yann Collette <ycollette.nospam@free.fr> - 4.4-beta5-1
- update to 4.4-beta5

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 4.3-1
- initial release
