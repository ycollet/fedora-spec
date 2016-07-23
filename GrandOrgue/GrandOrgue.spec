Name:         GrandOrgue
Version:      0.3.1
Release:      1%{?dist}
Summary:      GrandOrgue is a sample based pipe organ simulator.
Group:        Applications/Multimedia
License:      GPLv2+

URL:          http://sourceforge.net/projects/ourorgan
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 2141 http://svn.code.sf.net/p/ourorgan/svn/trunk ourorgan-2141
#  tar cvfz ourorgan-2141.tar.gz ourorgan-2141
%define revision 2141
Source0:      ourorgan-%{revision}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: wxGTK3-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: systemd-devel

%description
GrandOrgue is a sample based pipe organ simulator.

%prep
%setup -qn ourorgan-%{revision}

%build

%cmake -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
       .

make VERBOSE=1 %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category X-Sound \
        --add-category=Midi \
        --add-category=Audio \
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
%doc README license.txt AUTHORS
%{_bindir}/%{name}
%{_datadir}/*

%changelog
* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- Initial version
