%define kmaj 4
%define kmin 14
%define kpat 40
%define kver %{kmaj}.%{kmin}.%{kpat}
%define krel 2
%define krt  30
%define kversion %{kver}-%{krel}-rt%{krt}

Name: kernel-rt-mao
Summary: The Linux Real Time Kernel
Version: %{kver}
Release: %{krel}%{?dist}
License: GPL
Group: System Environment/Kernel
Vendor: The Linux Community
URL: http://www.kernel.org
Source0: https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-%{version}.tar.gz
Source1: kernel-config-%{kmaj}.%{kmin}
Source2: https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/4.14/older/patch-%{version}-rt%{krt}.patch.gz

BuildRequires: openssl-devel, openssl
BuildRequires: kmod, patch, bash, tar, git
BuildRequires: bzip2, xz, findutils, gzip, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: rpm-build, rpm, elfutils, elfutils-libelf-devel
BuildRequires: sparse
BuildRequires: pesign >= 0.10-4
BuildRequires: grub2-tools

BuildRoot: %{_tmppath}/%{name}-%{PACKAGE_VERSION}-root
Provides:  kernel-rt-mao-%{version}
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
The Linux Real Time Kernel, the operating system core itself

%package headers
Summary: Header files for the Linux real time kernel for use by glibc
Group: Development/System
%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package devel
Summary: Development package for building real time kernel modules to match the %{version} kernel
Group: System Environment/Kernel
AutoReqProv: no
%description devel
This package provides real time kernel headers and makefiles sufficient to build modules
against the %{version} kernel package.

%prep
%setup -q -n linux-%{version}
sed -i.ORIG '/^EXTRAVERSION/ s/=/= -%{krel}-rt%{krt}/g' Makefile
cp %{SOURCE1} .config
make olddefconfig

%build

cp_vmlinux()
{
  eu-strip --remove-comment -o "$2" "$1"
}

make clean &&  make %{?_smp_mflags}

%install
KBUILD_IMAGE=$(make image_name)

%ifarch ia64
  mkdir -p $RPM_BUILD_ROOT/boot/efi $RPM_BUILD_ROOT/lib/modules
%else
  mkdir -p $RPM_BUILD_ROOT/boot $RPM_BUILD_ROOT/lib/modules
%endif

INSTALL_MOD_PATH=$RPM_BUILD_ROOT make %{?_smp_mflags} KBUILD_SRC= mod-fw= INSTALL_MOD_STRIP=1 CONFIG_MODULE_COMPRESS=1 CONFIG_MODULE_COMPRESS_XZ=1 modules_install

%ifarch ia64
  cp $KBUILD_IMAGE $RPM_BUILD_ROOT/boot/efi/vmlinuz-%{kversion}
  ln -s efi/vmlinuz-%{kversion} $RPM_BUILD_ROOT/boot/
%else
  cp $KBUILD_IMAGE $RPM_BUILD_ROOT/boot/vmlinuz-%{kversion}
%endif

make %{?_smp_mflags} INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr KBUILD_SRC= headers_install
cp System.map $RPM_BUILD_ROOT/boot/System.map-%{kversion}
cp .config $RPM_BUILD_ROOT/boot/config-%{kversion}

rm -f $RPM_BUILD_ROOT/lib/modules/%{kversion}/{build,source}
mkdir -p $RPM_BUILD_ROOT/usr/src/kernels/%{kversion}
EXCLUDES="--exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude .tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.ko.xz --exclude=*.cmd --exclude=Documentation --exclude=firmware --exclude .config.old --exclude .missing-syscalls.d"
tar $EXCLUDES -cf- . | (cd $RPM_BUILD_ROOT/usr/src/kernels/%{kversion};tar xvf -)

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /sbin/installkernel -a -r /boot/vmlinuz-%{kversion} -a -r /boot/System.map-%{kversion} ]; then
  cp /boot/vmlinuz-%{kversion}    /boot/.vmlinuz-%{kversion}-mao
  cp /boot/System.map-%{kversion} /boot/.System.map-%{kversion}-mao
  rm -f /boot/vmlinuz-%{kversion} /boot/System.map-%{kversion}
  /sbin/installkernel %{kversion} /boot/.vmlinuz-%{kversion}-mao /boot/.System.map-%{kversion}-mao
  rm -f /boot/.vmlinuz-%{kversion}-mao /boot/.System.map-%{kversion}-mao
fi

rpm --eval '%{rhel}' | grep -q ^7 && grub2-mkconfig -o /boot/grub2/grub.cfg

%postun
rpm --eval '%{rhel}' | grep -q ^7 && grub2-mkconfig -o /boot/grub2/grub.cfg
test -e /boot/initramfs-%{kversion}.img && rm -f /boot/initramfs-%{kversion}.img

%files
%defattr (-, root, root)
/lib/modules/%{kversion}
/boot/*

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{kversion}

%changelog
* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.14.40-2
- add 4.14.40-rt30 kernel (4.16 kernels are xrunning)

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-2
- add 4.16.12-rt5 kernel

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.8-rt2-2
- add 4.16.8-rt2 kernel
