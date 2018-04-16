Name:           schismtracker
Version:        20180209
Release:        1%{?dist}
Summary:        Module tracker software for creating music

Group:          Applications/Multimedia
License:        GPLv3+
URL:            https://github.com/schismtracker/schismtracker
Source0:        schismtracker-20180209.zip
# download https://github.com/schismtracker/schismtracker/archive/schismtracker-master.zip
# unzip schismtracker-master.zip
# mv schismtracker-master schismtracker-20180209
# zip -r schismtracker-20180209.zip schismtracker-20180209
# rm -rf schismtracker-20180209

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  SDL-devel

%description
Schism Tracker is a free and open-source reimplementation of [Impulse
Tracker](https://github.com/schismtracker/schismtracker/wiki/Impulse-Tracker),
a program used to create high quality music without the requirements of
specialized, expensive equipment, and with a unique "finger feel" that is
difficult to replicate in part. The player is based on a highly modified
version of the [Modplug](https://openmpt.org/legacy_software) engine, with a
number of bugfixes and changes to [improve IT].

%prep
%setup -q

%build

autoreconf --force --install
mkdir auto
%configure
make DESTDIR=%{buildroot} %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS INSTALL README.md
%{_bindir}/schismtracker
%{_datadir}/pixmaps/*
%{_datadir}/man/*
%{_datadir}/applications/*


%changelog
* Sat Apr 14 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180209-1
- Initial version of the package

