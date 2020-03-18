%global debug_package %{nil}

# Global variables for github repository
%global commit0 5d9de9547ab87f175fabeb94c96ffcc07f7c3d6f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:      FoxDot
Version:   0.8.5
Release:   1%{?dist}
Epoch:     1
Summary:   FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider.

License:   Creative Commons Attribution-ShareAlike 4.0 International Public License
URL:       https://github.com/Qirky/FoxDot

Source0:   https://github.com/Qirky/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python3-devel
BuildRequires: supercollider-devel 
BuildRequires: python3-setuptools

%description
FoxDot is a Python3 programming environment that provides a fast and user-friendly abstraction to SuperCollider. It also comes with its own IDE, which means it can be used straight out of the box; all you need is Python and SuperCollider and you're ready to go!

%prep
%setup -qn %{name}-%{commit0}

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
%set_build_flags

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

%files
%doc LICENSE README.md changelog
%{python3_sitelib}/%{name}/__pycache__/*
%{_bindir}/%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{name}/demo
%{python3_sitelib}/%{name}/lib
%{python3_sitelib}/%{name}/osc
%{python3_sitelib}/%{name}/snd
%{python3_sitelib}/%{name}/rec/.null
%{python3_sitelib}/%{name}-*.egg-info

%changelog
* Wed Mar 18 2020 Yann Collette <ycollette dot nospam at free.fr> 0.8.5-1
- update to 0.8.5

* Thu Oct 10 2019 Yann Collette <ycollette dot nospam at free.fr> 0.8.3-1
- update to 0.8.3

* Wed Jun 5 2019 Yann Collette <ycollette dot nospam at free.fr> 0.7.16-1
- update to 0.7.16

* Tue Jun 4 2019 Yann Collette <ycollette dot nospam at free.fr> 0.7.1-1
- initial release of the spec file
