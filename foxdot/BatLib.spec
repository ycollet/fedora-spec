%global debug_package %{nil}

# Global variables for github repository
%global commit0 89abb1b6732a867630b9f2cdb3eef30ec25fda87
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:     BatLib
Version:  0.1
Release:  1%{?dist}
Epoch:    1
Summary:  Various helper classes I use, and external methods my other Quarks use.

License:  Creative Commons Attribution-ShareAlike 4.0 International Public License
URL:      https://github.com/supercollider-quarks/%{name}
Source0:  https://github.com/supercollider-quarks/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Requires: supercollider

%description
Various helper classes I use, and external methods my other Quarks use.

%prep
%setup -qn %{name}-%{commit0}

%build

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/
%__install -m 644 BatLib.quark  CoverMe.sc  Executor.sc   LessKeys.sc  StageLimiter.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/

%__install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/
%__install -m 644 external_methods/score_nrt_notifier.sc external_methods/window_center_rect.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/

%__install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/osx/scide_scapp/
%__install -m 644 external_methods/osx/scide_scapp/image_from_sound.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/osx/scide_scapp/

%files
%{_datadir}/*

%changelog
* Wed Jun 6 2019 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release of the spec file
