Summary: 4th order crossover filters
Name: zita-lrx
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: clthreads-devel clxclient-devel freetype-devel
BuildRequires: libX11-devel libXft-devel cairo-devel
BuildRequires: desktop-file-utils

%description
Zita-lrx is a command line jack application providing 2, 3, or 4-band,
4th order crossover filters. The filter type is continuously variable
between Linkwitz-Riley (-6dB at the xover frequency) and Butterworth
(-3 dB at the xover frequency). Outputs are exactly phase matched in
the crossover regions.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-march=native|%{optflags}|' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README* examples/
%{_bindir}/zita-lrx

%changelog
* Thu Aug  8 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.0-1
- initial build.
