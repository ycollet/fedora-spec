Name:    jamulus
Version: 3.5.6
Release: 6%{?dist}
Summary: Internet jam session software
URL:     https://github.com/corrados/jamulus/

License: GPLv2

# original tarfile can be found here:
Source0: https://github.com/corrados/jamulus/archive/r3_5_6.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: opus-devel
BuildRequires: desktop-file-utils

%description
jamulus is a client / server software which allow to perform
real-time rehearsal over the internet. It uses Jack Audio Connection Kit
and Opus audio codec to manage the audio session. 

%prep
%autosetup -n %{name}-r3_5_6

# Remove Opus source code, we use Opus library from Fedora
rm -rf libs/opus

%build

pushd .
cd src/res/translation
lrelease-qt5 *.ts
popd

%if 0%{?fedora} >= 32
  %qmake_qt5 Jamulus.pro CONFIG+="noupcasename opus_shared_lib"
%else
  # -fcf-protection produce an error in an object generatoin ...
  qmake-qt5 Jamulus.pro \
            QMAKE_CFLAGS_DEBUG="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection" \
            QMAKE_CFLAGS_RELEASE="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection" \
            QMAKE_CXXFLAGS_DEBUG="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection" \
            QMAKE_CXXFLAGS_RELEASE="%{__global_compiler_flags} -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection" \
            CONFIG+="noupcasename opus_shared_lib" 
%endif

%make_build VERBOSE=1

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -p %{name} %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 -p distributions/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 -p distributions/%{name}.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Jun 9 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.6-6
- update to 3.5.6-6

* Mon Jun 8 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-6
- fix spec file

* Sun Jun 7 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-5
- fix spec file

* Sat May 30 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-4
- fix debug package

* Thu May 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-3
- compile with fedora opus package
- fix install

* Thu May 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-2
- fix an executable right problem

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-1
- update 3.5.5-1

* Mon May 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.4-1
- update 3.5.4-1

* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.3-1
- update 3.5.3-1

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.2-1
- update 3.5.2-1

* Mon Apr 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.1-1
- update 3.5.1-1

* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.0-1
- update 3.5.0-1

* Sun Apr 12 2020 Yann Collette <ycollette.nospam@free.fr> - 3.4.7-1
- update 3.4.7-1

* Tue Mar 31 2020 Yann Collette <ycollette.nospam@free.fr> - 3.4.4-1
- update 3.4.4-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1
- update for Fedora 29

* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.4.2-1

* Sat May 30 2015 Yann Collette <ycollette.nospam@free.fr> - 3.4.1-1
- Initial release
