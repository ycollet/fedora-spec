%global debug_package %{nil}

# Global variables for github repository
%global commit0 c1de1f9512cc684b77198b35e627b71260dd1c94
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           r128gain
Version:        0.9.3
Release:        1%{?dist}
Epoch:          1
Summary:        r128gain is a multi platform command line tool to scan your audio files and tag them with loudness metadata (ReplayGain v2 or Opus R128 gain format), to allow playback of several tracks or albums at a similar loudness level.

License:        GPLv2+
URL:            https://github.com/desbma/r128gain.git

Source0:        https://github.com/desbma/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python3-devel python2-devel
BuildRequires:  python3-setuptools

%description
r128gain is a multi platform command line tool to scan your audio files and tag them with loudness metadata (ReplayGain v2 or Opus R128 gain format), to allow playback of several tracks or albums at a similar loudness level. r128gain can also be used as a Python module from other Python projects to scan and/or tag audio files.

%prep
%setup -qn %{name}-%{commit0}

%build
%set_build_flags

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

%files
%doc LICENSE README.md
%{python3_sitelib}/%{name}/__pycache__/*
%{_bindir}/%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{name}-*.egg-info

%changelog
* Thu Oct 10 2019 Yann Collette <ycollette dot nospam at free.fr> 0.9.3-1
- initial release of the spec file
