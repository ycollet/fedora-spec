%global debug_package %{nil}

# Global variables for github repository
%global commit0 520198049b36c7d42efbea17000b91f151c88c5f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:     FoxDotQuark
Version:  0.1
Release:  1%{?dist}
Epoch:    1
Summary:  FoxDot Quark is a required tool to connect FoxDot and SuperCollider.

License:  Creative Commons Attribution-ShareAlike 4.0 International Public License
URL:      https://github.com/Qirky/%{name}
Source0:  https://github.com/Qirky/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Requires: supercollider
Requires: BatLib

%description
FoxDot Quark is a required tool to connect FoxDot and SuperCollider.

%prep
%setup -qn %{name}-%{commit0}

%build

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/FoxDot/
%__install -m 644 FoxDot.quark FoxDot.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/FoxDot/

%files
%{_datadir}/*

%changelog
* Wed Jun 6 2019 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release of the spec file
