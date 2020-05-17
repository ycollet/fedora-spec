Summary: Impulse responses for various cabinet
Name:    impulse-response
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2+ and GPLv3
Group:   Applications/Multimedia
URL:     https://musical-artifacts.com/artifacts/252

Source0: 650-Assorted-Cabinet-Impulses.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: unzip

%description
Impulse responses for various cabinet

%prep

%install
rm -rf %{buildroot}

rm -rf IR_files
mkdir -p IR_files
cd IR_files
unzip %{SOURCE0}

mkdir -p %{buildroot}/%{_datadir}/IR/

cp *.wav %{buildroot}/%{_datadir}/IR/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/IR/*

%changelog
* Sun May 17 2020 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- initial spec file
