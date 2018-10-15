%define kmaj 4
%define kmin 18
%define kpat 12
%define kver %{kmaj}.%{kmin}.%{kpat}
%define krel 3
%define krt  7
%define kversion %{kver}

Name: kernel-rt-mao
Summary: The Linux Real Time Kernel
Version: %{kversion}.rt%{krt}
Release: %{krel}%{?dist}
License: GPL
Group: System Environment/Kernel
Vendor: The Linux Community
URL: http://www.kernel.org

Source0: https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-%{kversion}.tar.gz
Source1: kernel-config-%{kmaj}.%{kmin}

Patch0: https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/%{kmaj}.%{kmin}/older/patch-%{kversion}-rt%{krt}.patch.gz

BuildRequires: openssl-devel, openssl
BuildRequires: kmod, patch, bash, tar, git
BuildRequires: bzip2, xz, findutils, gzip, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: rpm-build, rpm, elfutils, elfutils-libelf-devel
BuildRequires: sparse
BuildRequires: pesign >= 0.10-4
BuildRequires: grub2-tools
BuildRequires: sed

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
%setup -q -n linux-%{kversion}

%patch0 -p1

cp %{SOURCE1} .config
sed -i -e "s/EXTRAVERSION =/EXTRAVERSION = -rt%{krt}/g" Makefile
echo "" > localversion-rt

make oldconfig

%build

make clean &&  make %{?_smp_mflags}

%install
KBUILD_IMAGE=$(make image_name)

%ifarch ia64
  mkdir -p $RPM_BUILD_ROOT/boot/efi $RPM_BUILD_ROOT/lib/modules
%else
  mkdir -p $RPM_BUILD_ROOT/boot     $RPM_BUILD_ROOT/lib/modules
%endif

INSTALL_MOD_PATH=$RPM_BUILD_ROOT make %{?_smp_mflags} KBUILD_SRC= mod-fw= INSTALL_MOD_STRIP=1 CONFIG_MODULE_COMPRESS=1 CONFIG_MODULE_COMPRESS_XZ=1 modules_install

%ifarch ia64
  cp $KBUILD_IMAGE $RPM_BUILD_ROOT/boot/efi/vmlinuz-%{kversion}-rt%{krt}
  ln -s efi/vmlinuz-%{kversion}-%{krt} $RPM_BUILD_ROOT/boot/
%else
  cp $KBUILD_IMAGE $RPM_BUILD_ROOT/boot/vmlinuz-%{kversion}-rt%{krt}
%endif

make %{?_smp_mflags} INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr KBUILD_SRC= headers_install
cp System.map $RPM_BUILD_ROOT/boot/System.map-%{kversion}-rt%{krt}
cp .config    $RPM_BUILD_ROOT/boot/config-%{kversion}-rt%{krt}

rm -f    $RPM_BUILD_ROOT/lib/modules/%{kversion}-rt%{krt}/{build,source}
mkdir -p $RPM_BUILD_ROOT/usr/src/kernels/%{kversion}-rt%{krt}
EXCLUDES="--exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude .tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.ko.xz --exclude=*.cmd --exclude=Documentation --exclude=firmware --exclude .config.old --exclude .missing-syscalls.d"
tar $EXCLUDES -cf- . | (cd $RPM_BUILD_ROOT/usr/src/kernels/%{kversion}-rt%{krt}; tar xvf -)

%clean
rm -rf $RPM_BUILD_ROOT

# restart grub: grub2-mkconfig -o /boot/grub2/grub.cfg

%post
if [ -x /sbin/installkernel -a -r /boot/vmlinuz-%{kversion}-rt%{krt} -a -r /boot/System.map-%{kversion}-rt%{krt} ]; then
  cp /boot/vmlinuz-%{kversion}-rt%{krt}    /boot/.vmlinuz-%{kversion}-rt%{krt}
  cp /boot/System.map-%{kversion}-rt%{krt} /boot/.System.map-%{kversion}-rt%{krt}
  rm -f /boot/vmlinuz-%{kversion}-rt%{krt} /boot/System.map-%{kversion}-rt%{krt}
  /sbin/installkernel %{kversion}-rt%{krt} /boot/.vmlinuz-%{kversion}-rt%{krt} /boot/.System.map-%{kversion}-rt%{krt}
  rm -f /boot/.vmlinuz-%{kversion}-rt%{krt} /boot/.System.map-%{kversion}-rt%{krt}
fi

rpm --eval '%{rhel}' | grep -q ^7 && grub2-mkconfig -o /boot/grub2/grub.cfg

%postun
rpm --eval '%{rhel}' | grep -q ^7 && grub2-mkconfig -o /boot/grub2/grub.cfg
test -e /boot/initramfs-%{kversion}-rt%{krt}.img && rm -f /boot/initramfs-%{kversion}-rt%{krt}.img

%files
%defattr (-, root, root)
/lib/modules/%{kversion}-rt%{krt}
/boot/*

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{kversion}-rt%{krt}

%changelog
* Wed Oct 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.12-rt7-3
- add 4.18.12-rt7 kernel

* Tue Sep 18 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.7-rt5-3
- add 4.18.7-rt5 kernel

* Sat Sep 8 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.18-rt11-3
- add 4.16.18-rt11 kernel

* Sun Jul 22 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.18-rt10-3
- add 4.16.18-rt10 kernel

* Sat Jun 23 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.15-rt7-3
- add 4.16.15-rt7 kernel

* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-3
- fix a huge config problem

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.14.40-2
- add 4.14.40-rt30 kernel (4.16 kernels are xrunning)

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-2
- add 4.16.12-rt5 kernel

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.8-rt2-2
- add 4.16.8-rt2 kernel
