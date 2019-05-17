# Disable production of debug package. Problem with fedora 23
# %global debug_package %{nil}

Name:    lebiniou-data
Version: 3.28
Release: 1%{?dist}
Summary: Lebiniou is an audio spectrum visualizer - data package
URL:     https://biniou.net/
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://dl.biniou.net/biniou/tar/lebiniou-data-3.28.tar.gz

BuildRequires: make

%description

This package contains data files for use with lebiniou - https://gitlab.com/lebiniou/lebiniou

%prep
%setup %{name}-%{version}

%build

%configure --prefix=%{_prefix} --libdir=%{_libdir}

%install

make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%doc README.md AUTHORS ChangeLog COPYING THANKS

%{_datadir}/*

%changelog
* Fri May 17 2019 Yann Collette <ycollette.nospam@free.fr> - 3.28-1
- initial spec file
