# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

Name:    loudness-scanner
Version: 0.5.1
Release: 1%{?dist}
Summary: A loudness scanner (according to the EBU R128 standard)
URL:     https://github.com/jiixyj/loudness-scanner
Group:   Applications/Multimedia

Source0: loudness-scanner.tar.gz

# git clone https://github.com/jiixyj/loudness-scanner
# cd loudness-scanner
# git checkout v0.5.1
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz loudness-scanner.tar.gz loudness-scanner/*
# rm -rf loudness-scanner

License: MIT

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt-devel
BuildRequires: glib2-devel
BuildRequires: cmake
BuildRequires: libsndfile-devel
BuildRequires: taglib-devel
BuildRequires: mpg123-devel
BuildRequires: libmpcdec-devel
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: ffmpeg-devel
BuildRequires: librsvg2-devel
BuildRequires: gtk2-devel
BuildRequires: chrpath
BuildRequires: harfbuzz-devel
BuildRequires: speexdsp-devel

%description
loudness-scanner is a tool that scans your music files according to the EBU
R128 standard for loudness normalisation. It optionally adds ReplayGain
compatible tags to the files.

%prep
%setup -qn %{name}

%build

mkdir build
cd build
%cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_C_FLAGS="-fPIC -I/usr/include/harfbuzz/" ..
make VERBOSE=1 %{?_smp_mflags}

%install

cd build
make DESTDIR=%{buildroot} install

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 644 loudness $RPM_BUILD_ROOT/%{_bindir}/
install -pm 644 loudness-drop-gtk $RPM_BUILD_ROOT/%{_bindir}/
install -pm 644 loudness-drop-qt5 $RPM_BUILD_ROOT/%{_bindir}/

chrpath --delete $RPM_BUILD_ROOT/usr/bin/*

%files
%doc COPYING README.md
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*

%changelog
* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- fix for Fedora 31

* Thu Sep 12 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- Initial spec file
