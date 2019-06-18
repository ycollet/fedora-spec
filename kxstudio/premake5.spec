# Disable production of debug package.
%global debug_package %{nil}

Summary: Tool for describing builds
Name:    premake5
Version: 5.0.0alpha13
Release: 1%{?dist}
License: GPLv3+
Group:   Developpment
URL:     https://github/premake/

Source0: https://github.com/premake/premake-core/releases/download/v5.0.0-alpha13/premake-5.0.0-alpha13-src.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++

%description
Describe your software project with a full-featured scripting language and let Premake write the build scripts for you. With one file your project can support both IDE-addicted Windows coders and Linux command-line junkies!

%prep
%setup -qn premake-5.0.0-alpha13

%build
cd build/gmake.unix/
make %{?_smp_mflags}

%install
%__install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/release/premake5 %{buildroot}/%{_bindir}/premake5

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc BUILD.txt CHANGES.txt LICENSE.txt README.md
%{_bindir}/*

%changelog
* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-alpha13-1
- initial release
