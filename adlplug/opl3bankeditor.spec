# Global variables for github repository
%global commit0 a8c9a70a81cc076abea2ed6c60437edb7aadca59
%global gittag0 v1.5.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    opl3bankeditor
Version: 1.5.1
Release: 1%{?dist}
Summary: A small cross-platform editor of the OPL3 FM banks of different formats
URL:     https://github.com/Wohlstand/OPL3BankEditor
Group:   Applications/Multimedia

License: GPLv3

# git clone https://github.com/Wohlstand/OPL3BankEditor
# git checkout v1.5.1
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz OPL3BankEditor.tar.gz OPL3BankEditor/*
# rm -rf OPL3BankEditor

Source0: OPL3BankEditor.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qwt-devel

%description
A small cross-platform editor of the OPL3 FM banks of different formats

%prep

%setup -qn OPL3BankEditor

sed -i -e "/Categories/d" src/resources/opl3_bank_editor.desktop

%build

mkdir -p build
cd build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
       ..

%make_build VERBOSE=1

%install

cd build

%make_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/opl3_bank_editor.desktop

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
%doc LICENSE license.txt README.md changelog.txt
%{_bindir}/opl3_bank_editor
%{_datadir}/mime/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/opl3_bank_editor/*

%changelog
* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- update to 1.5.1

* Fri Mar 22 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- initial release of the spec file
