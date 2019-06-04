%global debug_package %{nil}

Name:           FoxDot
Version:        0.7.1
Release:        1%{?dist}
Epoch:          1
Summary:        FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider.

License:        Creative Commons Attribution-ShareAlike 4.0 International Public License
URL:            https://github.com/Qirky/FoxDot
Source0:        https://github.com/Qirky/FoxDot/archive/%{version}.tar.gz
BuildRequires:  python3-devel python2-devel
BuildRequires:  supercollider-devel 
BuildRequires:  python3-setuptools

%description
FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider. It also comes with its own IDE, which means it can be used straight out of the box; all you need is Python and SuperCollider and you're ready to go!

%package -n python2-foxdot
Summary:        FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider.
Requires:       supercollider

%description -n python2-foxdot
FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider. It also comes with its own IDE, which means it can be used straight out of the box; all you need is Python and SuperCollider and you're ready to go!

%package -n python3-foxdot
Requires:       supercollider
Summary:        FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider.
%{?python_provide:%python_provide python3-foxdot}

%description -n python3-foxdot
FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider. It also comes with its own IDE, which means it can be used straight out of the box; all you need is Python and SuperCollider and you're ready to go!

%prep
%autosetup -n %{name}-%{version} -p1

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
%set_build_flags

pushd %{py3dir}
    %{__python3} setup.py build
popd

%{__python2} setup.py build

%install

# first install python3 so the binaries are overwritten by the python2 ones
pushd %{py3dir}
    %{__python3} setup.py install --root %{buildroot}
pushd %{buildroot}%{_bindir} &> /dev/null
popd &> /dev/null

popd

    %{__python2} setup.py install --root %{buildroot}
pushd %{buildroot}%{_bindir} &> /dev/null

%files -n python3-foxdot
%doc LICENSE MANIFEST README.md changelog
%{python3_sitelib}/%{name}/__pycache__/*
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{name}/demo
%{python3_sitelib}/%{name}/lib
%{python3_sitelib}/%{name}/osc
%{python3_sitelib}/%{name}/snd
%{python3_sitelib}/%{name}-*.egg-info

%files -n python2-foxdot
%doc LICENSE MANIFEST README.md changelog
%{_bindir}/%{name}
%dir %{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}/*.py
%{python2_sitelib}/%{name}/*.pyc
%{python2_sitelib}/%{name}/*.pyo
%{python2_sitelib}/%{name}/demo
%{python2_sitelib}/%{name}/lib
%{python2_sitelib}/%{name}/osc
%{python2_sitelib}/%{name}/snd
%{python2_sitelib}/%{name}-*.egg-info

%changelog
* Tue Jun 4 2019 Yann Collette <ycollette dot nospam at free.fr> 0.7.1-1
- initial release of the spec file
