Name:           buzztrax
Version:        0.10.2
Release:        5%{?dist}
Summary:        Buzztrax is a music composer similar to tracker applications.

License:        LGPL2.1
URL:            http://www.buzztrax.org 
Source0:        http://files.buzztrax.org/releases/%{name}-%{version}.tar.gz
Patch0:         buzztrax-0001-fix-build.patch

BuildRequires:  gstreamer1-devel gstreamer1-plugins-base-devel libxml2-devel
BuildRequires:  clutter-gtk-devel gtk+-devel gettext-devel gtk-doc
BuildRequires:  intltool libtool gstreamer1-plugins-good desktop-file-utils orc-compiler
BuildRequires:  alsa-lib-devel libgudev-devel fluidsynth-devel goffice-devel
BuildRequires:  chrpath

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for

%prep

%setup -qn %{name}-%{version}

%patch0 -p1

%build

export QA_SKIP_RPATHS=1

%configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-dllwrapper=no

%{__make} DESTDIR=%{buildroot} %{_smp_mflags} CFLAGS="%{optflags} -Wno-error"

%install

rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=%{buildroot} install

chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libbuzztrax-core.so.1.1.0
chrpath --delete $RPM_BUILD_ROOT/usr/lib/buzztrax-songio/libbtbsl.so
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/buzztrax-cmd
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/buzztrax-edit

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-edit.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-songio-buzz.desktop

%post
/bin/touch --no-create %{_datadir}/icons/gnome &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/gnome &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/gnome &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/gnome &>/dev/null || :

%files
%license COPYING
%doc README.md
%{_datadir}/gtk-doc/html/buzztrax-*
%{_bindir}/buzztrax-cmd
%{_bindir}/buzztrax-edit
/usr/lib/buzztrax-songio/*
%{_libdir}/buzztrax
%{_libdir}/gstreamer-1.0/libbuzztrax*
%{_libdir}/gstreamer-1.0/libgstbml.*
%{_libdir}/gstreamer-1.0/libgstsidsyn.*
%{_libdir}/gstreamer-1.0/libgstfluidsynth.*
%{_libdir}/libbml.*
%{_libdir}/libbuzztrax-core.*
%{_libdir}/libbuzztrax-gst.*
%{_libdir}/libbuzztrax-ic.*
%{_datadir}/buzztrax
%{_datadir}/icons/gnome/*/apps/%{name}*.png
%{_datadir}/icons/gnome/*/apps/%{name}*.svg
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}-%{version}.mo
%{_datadir}/mime/packages/%{name}*.xml
%{_datadir}/GConf/gsettings/buzztrax.convert
%{_datadir}/gstreamer-1.0/presets/GstBtEBeats.prs
%{_datadir}/gstreamer-1.0/presets/GstBtSimSyn.prs
%{_datadir}/applications/%{name}-edit.desktop
%{_datadir}/applications/%{name}-songio-buzz.desktop
%{_datadir}/appdata/buzztrax.appdata.xml
%{_datadir}/glib-2.0/schemas/org.buzztrax.gschema.xml

%files devel
%{_includedir}/libbml
%{_includedir}/libbuzztrax-core
%{_includedir}/libbuzztrax-gst
%{_includedir}/libbuzztrax-ic
%{_libdir}/pkgconfig/libbml.pc
%{_libdir}/pkgconfig/libbuzztrax-core.pc
%{_libdir}/pkgconfig/libbuzztrax-gst.pc
%{_libdir}/pkgconfig/libbuzztrax-ic.pc

%changelog
* Thu Apr 30 2020 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-5
- Fix for Fedora 

* Sun Oct 23 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-4
- changed source

* Fri Oct 14 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-3
- added orc dep

* Fri Oct 14 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-2
- update spec to update icons on install

* Fri Oct 14 2016 L.L.Robinson <baggypants@fedoraproject.org>
- 
