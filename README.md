The repo related to these packages can be found here:

https://copr.fedorainfracloud.org/coprs/ycollet/linuxmao/

This repo has old packages for Fedora 25 and up to date packages for Fedora 26 and 27.

To build the spec file:
- copy it into your rpmbuild/SPEC directory
- run:
```
$ spectool -g <package_name.spec> # to download the source file
```
- copy the source file into rpmbuild/SOURCE
- run:
```
$ rpmbuild -ba filename.spec
```
The result can be found in:
- RPMS/noarch
- RPMS/x86_64

The SRPMS file is located in:
- SRPMS

Install the rpm file using yum:
as a root user: 
```
$ yum install filename.rpm
# or
$ dnf install filename.rpm
```

To test the rebuild of the package using mock:
```
$ mock -r fedora-26-x86_64 --rebuild polyphone-1.6.0-1.fc26.src.rpm
```

To enable a thirdparty repository, you must add it to /etc/mock/fedora-26-x86_64.cfg for example and then, enable it via the command line. For example:
```
$ mock -r fedora-26-x86_64 --enablerepo=ycollet-linuxmao --rebuild dgedit-0.1-1.fc26.src.rpm
```

The portion added to /etc/mock/fedora-2{5,6,7}-x86_64.cfg is:
```
[ycollet-linuxmao]
name=Copr repo for linuxmao owned by ycollet
baseurl=https://copr-be.cloud.fedoraproject.org/results/ycollet/linuxmao/fedora-$releasever-$basearch/
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://copr-be.cloud.fedoraproject.org/results/ycollet/linuxmao/pubkey.gpg
enabled=1
enabled_metadata=1

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=604800
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
skip_if_unavailable = 1
keepcache = 0

[planetccrma]
name=Planet CCRMA $releasever - $basearch
baseurl=http://ccrma.stanford.edu/planetccrma/mirror/fedora/linux/planetccrma/$releasever/$basearch
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-planetccrma
gpgcheck=1

[planetcore]
name=Planet CCRMA Core $releasever - $basearch
baseurl=http://ccrma.stanford.edu/planetccrma/mirror/fedora/linux/planetcore/$releasever/$basearch
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-planetccrma
gpgcheck=1
```

This is the content of the repo conf file found in /etc/yum.repo.d.

To create the LiveCD using livecd-creator:

As a root user:
```
$ livecd-creator --verbose --config=fedora-26-live-jam-kde.ks --fslabel=LesCuizines --releasever 26
```

To create the LiceCD using livemedia-creator:

As a root user:
```
$ setenforce Permissive
$ livemedia-creator --make-iso --ks fedora-26-live-jam-kde.ks --project LesCuizines --iso-name livecd-fefora26-mao.iso --iso-only --releasever 26 --volid LesCuizines --title LesCuizines --resultdir /var/lmc --no-virt
```

To test the ISO file:
Without audio:
```
$ qemu-kvm -m 2048 -vga qxl -cdrom fedora-26-LesCuizines.iso
```
With audio and usb:
```
$ qemu-kvm -m 2048 -vga qxl -usb -soundhw hda -cdrom fedora-26-LesCuizines.iso
```
With audio, usb and with 2 cpus:
```
$ qemu-kvm -m 2048 -vga qxl -usb -soundhw hda -smp cpus=2 -cdrom fedora-26-LesCuizines.iso
```

To test the USB bootable file:
```
$ qemu-kvm -m 2048 -vga qxl -smp cpus=2 -usb -soundhw hda -drive file=fedora-26-LesCuizines.iso -boot menu=on
```

To mount a usb device:
```
# lsusb
...
Bus 002 Device 003: ID 18d1:4e11 Google Inc. Nexus One
```

(Note the Bus and device numbers).
Manually, using qemu-kvm command line

```
$ qemu-kvm -m 2048 -name LeCuizines -cdrom fedora-26-LesCuizines.iso -usb -device usb-host,hostbus=2,hostaddr=3
```

