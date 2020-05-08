# Global variables for github repository
%global commit0 7232969a1d02eea926ab5592d2a0bc0c54003d05
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    nanoinvaders
Version: 0.1
Release: 1%{?dist}
Summary: Play space invaders in an audio plugin

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/clearly-broken-software/nanoinvaders
Source0: nanoinvaders.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libsamplerate-devel

%description
Play space invaders in an audio plugin

%prep
%setup -qn %{name}

%build

make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install 

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/
%__install -m 755 -d %{buildroot}/%{_libdir}/vst/

cp bin/%{name} %{buildroot}/%{_bindir}/
cp bin/%{name}-vst.so %{buildroot}/%{_libdir}/vst/
cp -r bin/%{name}.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*


%changelog
* Fri May 8 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
