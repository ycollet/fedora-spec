# Global variables for github repository
%global commit0 7c616a8a7d7fedd2fa5bfd7ce1f5d867d80cab0a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         performer
Version:      1.0.2
Release:      1%{?dist}
Summary:      Live performance audio session manager using Carla
URL:          https://github.com/progwolff/performer
Source0:      https://github.com/progwolff/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia

License:      GPLv2+

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qt5-qtwebview-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: sed

%description
Live performance audio session manager using Carla

%prep
%setup -qn %{name}-%{commit0}

sed -i -e "s/AudioVideo/X-AudioVideo/g" performer.desktop

%build

%cmake -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       .

%make_build VERBOSE=1

%install

%make_install DESTDIR=%{buildroot}

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

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
%doc CONTRIBUTORS README.md LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update for Fedora 29
* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to latest version
* Tue Nov 28 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial version of spec file
