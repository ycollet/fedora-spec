# Disable production of debug package.
%global debug_package %{nil}

Summary:       padthv1 is an old-school all-digital 4-oscillator subtractive polyphonic synthesizer with stereo fx.
Name:          padthv1
Version:       0.9.13
Release:       1%{?dist}
URL:           http://sourceforge.net/projects/%{name}
Source0:       https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:       GPLv2+

Requires:      hicolor-icon-theme

BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: lv2-devel >= 1.2.0
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: liblo-devel

%description
%{name} is an old-school all-digital 4-oscillator subtractive polyphonic synthesizer with stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of synthv1
Requires:      lv2
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
An LV2 plugin of the padthv1 synthesizer

%prep
%setup -q

# configure hard-codes prepending searches of /usr (already implicit, causes problems),
# and /usr/local (not needed here), so force it's non-use
sed -i.ac_with_paths -e "s|^ac_with_paths=.*|ac_with_paths=|g" configure configure.ac

autoconf -f
sed -i -e 's|-msse -mfpmath=sse -ffast-math|%{optflags} -fPIC|' padthv1_lv2.pro
sed -i -e 's|-msse -mfpmath=sse -ffast-math|%{optflags} -fPIC|' padthv1_jack.pro

%build

autoreconf

export QTDIR=%{_qt5_prefix}
%configure --enable-qt5 --enable-jack --enable-nsm --enable-liblo
make

%install

make DESTDIR=%{buildroot} install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so
install -m 0644 src/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING AUTHORS README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/man/man1/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml

%files -n lv2-%{name}
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Fri Mar 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.13-1
- update to 0.9.13-1

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.12-1
- Initial spec file
