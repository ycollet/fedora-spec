The repo related to these packages can be found here:

https://copr.fedorainfracloud.org/coprs/ycollet/linuxmao/

This repo has old packages for Fedora 25, 26, 27, 28 and 29 and up to date packages for Fedora 30, 31 and 32.

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
$ mock -r /etc/mock/fedora-32-x86_64.cfg --rebuild polyphone-2.0.1-1.fc32.src.rpm
```

To enable a thirdparty repository, you must add it to /etc/mock/templates/fedora-32.tpl for example and then, enable it via the command line. For example:
```
$ mock -r /etc/mock/fedora-32-x86_64.cfg --enablerepo=ycollet-linuxmao --rebuild dgedit-0.1-2.fc32.src.rpm
```

The portion added to /etc/mock/templates/fedora-{30,31,32}.tpl is:

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
$ livecd-creator --verbose --config=fedora-30-live-jam-kde.ks --fslabel=LesCuizines --releasever 30
```

To create the LiceCD using livemedia-creator:

As a root user:
```
$ setenforce Permissive
$ livemedia-creator --make-iso --ks fedora-30-live-jam-kde.ks --project LesCuizines --iso-name livecd-fedora-30-mao.iso --iso-only --releasever 30 --volid LesCuizines --title LesCuizines --resultdir /var/lmc --no-virt
```

To check the potential changes from the kickstart file:
$ dnf install pykickstart.noarch rpmfusion-free-remix-kickstarts.noarch spin-kickstarts.noarch
$ ksflatten -c /usr/share/spin-kickstarts/fedora-live-xfce.ks -o xfce.ks
$ meld fedora-30-live-jam-kde.ks xfce.ks &

To test the ISO file:

Install QEmu-KVM and the SDL interface.

```
$ dnf install qemu-system-x86-core
$ dnf install qemu-ui-sdl qemu-audio-sdl
```

Without audio:
```
$ qemu-kvm -m 2048 -vga qxl -sdl -cdrom fedora-30-LesCuizines.iso
```
With audio and usb:
```
$ qemu-kvm -m 2048 -vga qxl -usb -soundhw hda -sdl -cdrom fedora-30-LesCuizines.iso
```
With audio, usb and with 2 cpus:
```
$ qemu-kvm -m 2048 -vga qxl -usb -soundhw hda -smp cpus=2 -sdl -cdrom fedora-30-LesCuizines.iso
```

To test the USB bootable file:
```
$ qemu-kvm -m 2048 -vga qxl -sdl -smp cpus=2 -usb -soundhw hda -drive file=fedora-30-LesCuizines.iso -boot menu=on
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
$ qemu-kvm -m 2048 -name LeCuizines -sdl -cdrom fedora-30-LesCuizines.iso -usb -device usb-host,hostbus=2,hostaddr=3
```
