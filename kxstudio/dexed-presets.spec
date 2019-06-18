Summary: Additional presets for Dexed
Name:    dexed-extra-presets
Version: 1.0.1
Release: 1%{?dist}
License: GPLv2+ and GPLv3 and Green OpenMusic
Group:   Applications/Multimedia
URL:     https://asb2m10.github.io/dexed/

Source0: http://ycollette.free.fr/Milkdrop/DX7_AllTheWeb.zip
Source1: http://ycollette.free.fr/Milkdrop/3221-Dexed_cart_1.0.zip
Source2: http://ycollette.free.fr/Milkdrop/SynLib_DX_TX_Marc_Bareille.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: p7zip

%description
A collection of additional preset for Dexed.

%prep

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT

# These directories are owned by hydrogen:
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/dexed/presets

7za x %{SOURCE0} -o$RPM_BUILD_ROOT%{_datadir}/dexed/presets/alltheweb
7za x %{SOURCE1} -o$RPM_BUILD_ROOT%{_datadir}/dexed/presets/cart
7za x %{SOURCE2} -o$RPM_BUILD_ROOT%{_datadir}/dexed/presets/syntlib

# Reorganisation
cd $RPM_BUILD_ROOT%{_datadir}/dexed/presets/alltheweb
mv DX7_AllTheWeb/* .
rmdir DX7_AllTheWeb

cd $RPM_BUILD_ROOT%{_datadir}/dexed/presets/syntlib
mv SynLib_DX_TX_Marc_Bareille/* .
rmdir SynLib_DX_TX_Marc_Bareille

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/dexed/presets/alltheweb/*
%{_datadir}/dexed/presets/cart/*
%{_datadir}/dexed/presets/syntlib/*

%changelog
* Wed Jan 23 2019 Yann Collette <ycollette dot nospam at free.fr> 1.0.1-1
- add SynLib_DX_TX_Marc_Bareille.zip

* Sun Sep 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- Initial release
