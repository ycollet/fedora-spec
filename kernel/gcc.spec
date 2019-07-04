# Disable production of debug package.
%global debug_package %{nil}

Summary: gcc for kernel compilation
Name:    gcc
Version: 8.3.0
Release: 1%{?dist}
License: GPLv3+
Group:   Developpment
URL:     https://gcc.gnu.org/

Source0: https://ftp.gnu.org/gnu/gcc/gcc-8.3.0/gcc-8.3.0.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ make
BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo texinfo-tex
BuildRequires: systemtap-sdt-devel
BuildRequires: gmp-devel mpfr-devel libmpc-devel
BuildRequires: python2-devel python3-devel
BuildRequires: glibc-devel
BuildRequires: elfutils-devel
BuildRequires: elfutils-libelf-devel

Requires: binutils

%description
An "old" version of gcc used to compile the kernel RT

%prep
%setup -qn %{name}-%{version}

%build

./configure --enable-languages=c --prefix=/opt/%{name}-%{version} --with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--enable-checking=release --with-system-zlib --disable-gomp \
	--with-gcc-major-version-only --program-suffix=-83 --disable-multilib

make %{?_smp_mflags}

%install

make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/%{name}-%{version}/*

%changelog
* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 8.3.0-1
- initial release
