# Global variables for github repository
%global commit0 a8c9a70a81cc076abea2ed6c60437edb7aadca59
%global gittag0 v1.3.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    opn2bankeditor
Version: 1.3.0
Release: 2%{?dist}
Summary: A small cross-platform editor of the OPN2 FM banks of different formats
URL:     https://github.com/Wohlstand/OPN2BankEditor

License: GPLv3

# git clone https://github.com/Wohlstand/OPN2BankEditor
# git checkout v1.3
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz OPN2BankEditor.tar.gz OPN2BankEditor/*
# rm -rf OPN2BankEditor

Source0: OPN2BankEditor.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qwt-devel

%description
A small cross-platform editor of the OPN2 FM banks of different formats

%prep

%setup -qn OPN2BankEditor

sed -i -e "/Categories/d" src/resources/opn2_bank_editor.desktop

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/opn2_bank_editor.desktop

%files
%doc README.md changelog.txt
%license LICENSE license.txt
%{_bindir}/opn2_bank_editor
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/opn2_bank_editor/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- fix for Fedora 33

* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- initial release of the spec file
