# Global variables for github repository
%global commit0 0ecd7bef72942ae65858743b223bdc6916d240dd
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    fugio
Version: 3.1.0
Release: 1%{?dist}
Summary: Fugio is an open visual programming system for building digital art and creative projects quickly, with no programming experience required
URL:     https://www.bigfug.com/software/fugio/
Group:   Applications/Multimedia
License: LGPL-3.0

# git clone https://github.com/bigfug/Fugio
# cd Fugio
# git checkout v3.1.0
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz Fugio.tar.gz Fugio/*

Source0: Fugio.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ sed
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qttools
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: ffmpeg-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: opencv-devel
BuildRequires: fftw-devel
BuildRequires: lua-devel
BuildRequires: ffmpeg-devel
BuildRequires: eigen3-devel

%description
Fugio is an open visual programming system for building digital art and creative projects quickly, with no programming experience required

%prep
%setup -qn Fugio

%ifarch x86_64 amd64
sed -i -e "s/lib\/fugio/lib64\/fugio/g" CMakeLists.txt
%endif

sed -i -e "s/Fugio;//g" FugioApp/fugio.desktop

%build

mkdir -p build-tmp
cd build-tmp

%cmake -DCMAKE_BUILD_TYPE=RELEASE ..

make DESTDIR=%{buildroot} %{?_smp_mflags}

%install

cd build-tmp

make DESTDIR=%{buildroot} install

rm %{buildroot}%{_includedir}/.gitignore

desktop-file-install --vendor '' \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/fugio.desktop

%clean

rm -rf %{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/fugio/*
%{_datadir}/*

%changelog
* Tue Jan 21 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- initial version of the spec file
