# Global variables for github repository
%global commit0 e7d5b7bb2fe6f0c6bc6e6a148c9899fb859300ed
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:         lenmus
Version:      5.4.1.%{shortcommit0}
Release:      1%{?dist}
Summary:      An app to study music theory and train you ear
Group:        Applications/Multimedia
License:      GPLv2+

URL:          https://github.com/lenmus/lenmus
Source0:      https://github.com/lenmus/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:       lenmus_0001-fix-install.patch

BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: zlib-devel 
BuildRequires: libpng-devel
BuildRequires: freetype-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: cmake
BuildRequires: wxGTK3-devel
BuildRequires: sqlite-devel
BuildRequires: lomse-devel

%description
LenMus Phonascus, "the teacher of music", is a free program to help you in the study of music theory and ear training.

The LenMus Project is an open project, committed to the principles of
Open Source, free education, and open access to information. It has no comercial
purpose. It is an open workbench for working on all areas related to teaching
music, and music representation and management with computers. It aims at
developing publicly available knowledge, methods and algorithms related to all
these areas and at the same time provides free quality software for music
students, amateurs, and teachers.

Please visit the LenMus website (http://www.lenmus.org) for the latest news
about the project or for further details about releases.

%prep
%setup -qn %{name}-%{commit0}
%patch0 -p1

%build

# -Werror=format-security -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1
#export CFLAGS="-fPIC -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic"

#-Werror=format-security -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1
#export CXXFLAGS="-fPIC -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic"

%cmake -D_filename:FILEPATH=/usr/include/wx-3.0/wx/version.h \
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
       -DPortTime_LIBRARY:FILEPATH=/usr/%{_lib}/libportaudio.so \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/%{name}/%{version}/res \
        %{buildroot}%{_datadir}/%{name}/%{version}/res/desktop/%{name}.desktop

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
%doc AUTHORS CHANGELOG.md INSTALL README.md NEWS THANKS LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-1
- Initial version
