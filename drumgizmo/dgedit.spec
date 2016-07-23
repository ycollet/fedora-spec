Summary: Software Synthesizer
Name: dgedit
Version: 0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL:            http://git.drumgizmo.org/dgedit.git
Source0:        dgedit-0.1.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: qt4-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: libao-devel

%description
The DrumGizmo drumkit editor DGEdit is currently in a functioning, but very early phase of development. All of the essentials for importing, editing and exporting the raw drumkit recordings are there - but it is not exactly user friendly. 

%prep
%setup -qn %{name}-%version

%build

./autogen.sh
%configure
%{__make} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# desktop file categories
BASE="Application AudioVideo"
XTRA="X-Synthesis X-MIDI X-Jack"
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/dgedit

%changelog
* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- Initial release of spec file for 0.1
