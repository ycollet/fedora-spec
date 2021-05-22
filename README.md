+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++                                                         ++
++ WARNIHG !!                                              ++
++ This repository is now archived. The work continues on: ++
++ https://github.com/audinux/fedora-spec                  ++
++                                                         ++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

****************

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

To mirror the COPR repository:
$ mkdir -p rpm-copr/33
$ cd rpm-copr/33
$ dnf reposync --release=33 --repoid=copr:copr.fedorainfracloud.org:ycollet:linuxmao --destdir .  --downloadcomp

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

First: prepare the thirdparty files (GuitarPro files, soundfonts, images):
```
$ ./prepare.sh
```
This script will download a zip a put everything in /tmp/prepare/ directory.

As a root user:
```
$ livecd-creator --verbose --config=fedora-32-live-jam-xfce.ks --fslabel=Audinux --releasever 32
```

```
# To build using the EPEL 7 version of livecd-tools:

$ mock -r /etc/mock/epel-7-x86_64.cfg --isolation=simple --init --install wget unzip livecd-tools
$ mock -r /etc/mock/epel-7-x86_64.cfg --copyin fedora-32-live-jam-xfce.ks --copyin prepare.sh /builddir
$ mock -r /etc/mock/epel-7-x86_64.cfg --enable-network --shell

# To build using the Fedora 32 version of livecd-tools:

$ mock -r /etc/mock/fedora-32-x86_64.cfg --isolation=simple --init --install wget unzip livecd-tools
$ mock -r /etc/mock/fedora-32-x86_64.cfg --copyin fedora-32-live-jam-xfce.ks --copyin prepare.sh /builddir
$ mock -r /etc/mock/fedora-32-x86_64.cfg --enable-network --shell

# Then: preinstall the required files and start livecd-creator

$ cd /builddir
$ ./prepare.sh
$ livecd-creator --verbose --config=fedora-32-live-jam-xfce.ks --fslabel=Audinux --releasever 32
```

To create the LiceCD using livemedia-creator:

As a root user:
```
$ mock -r /etc/mock/fedora-32-x86_64.cfg --isolation=simple --init --install lorax-lmc-novirt wget unzip libblockdev-lvm libblockdev-btrfs libblockdev-swap libblockdev-loop libblockdev-crypto libblockdev-mpath libblockdev-dm libblockdev-mdraid libblockdev-nvdimm
$ mock -r /etc/mock/fedora-32-x86_64.cfg --copyin fedora-32-live-jam-xfce.ks --copyin prepare.sh /builddir
$ mock -r /etc/mock/fedora-32-x86_64.cfg --enable-network --shell
$ cd /builddir
$ ./prepare.sh
$ livemedia-creator --make-iso --ks fedora-32-live-jam-xfce.ks --project Audinux --iso-name livecd-fedora-32-mao.iso --iso-only --releasever 32 --volid Audinux --image-name Audinux --resultdir /var/lmc --no-virt --tmp /var/tmp
```

To check the potential changes from the kickstart file:
$ dnf install pykickstart.noarch rpmfusion-free-remix-kickstarts.noarch spin-kickstarts.noarch
$ ksflatten -c /usr/share/spin-kickstarts/fedora-live-xfce.ks -o xfce.ks
$ meld fedora-32-live-jam-xfce.ks xfce.ks &

To test the ISO file:

Install QEmu-KVM and the SDL interface.

```
$ dnf install qemu-system-x86-core qemu-kvm
$ dnf install qemu-ui-sdl qemu-audio-sdl
```

Without audio:
```
$ qemu-kvm -m 2048 -vga qxl -sdl -cdrom fedora-32-Audinux.iso
```
With audio and usb:
```
$ qemu-kvm -m 2048 -vga qxl -usb -soundhw hda -sdl -cdrom fedora-32-Audinux.iso
```
With audio, usb and with 2 cpus:
```
$ qemu-kvm -m 2048 -vga qxl -usb -soundhw hda -smp cpus=2 -sdl -cdrom fedora-32-Audinux.iso
```

To test the USB bootable file:
```
$ qemu-kvm -m 2048 -vga qxl -sdl -smp cpus=2 -usb -soundhw hda -drive file=fedora-32-Audinux.iso -boot menu=on
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
$ qemu-kvm -m 2048 -name Audinux -sdl -cdrom fedora-32-Audinux.iso -usb -device usb-host,hostbus=2,hostaddr=3
```

Write ISO to USB:

You can use dd:
```
$ dd if=Audinux.iso of=/dev/sdc bs=1024
```
Or mediawriter:
```
$ dnf install mediawriter
$ mediawriter
```

Once the USB key is installed, you can add data persistency using livecd-iso-to-disk:
```
$ dnf install livecd-tools
```

Locate where is your usb disk:
```
$ dmesg | tail
or
$ lsblk
```

Then, reformat to ext4 the usb disk:
```
$ mkfs.ext4 /dev/sdb
```

To add a persistent home directory of size 2Go:
```
$ livecd-iso-to-disk --reset-mbr --format --msdos --home-size-mb 2048 Audinux.iso /dev/sdb
```

To add a data persistency on your USB key:
```
$ livecd-iso-to-disk --reset-mbr --format --msdos --unencrypted-home --overlay-size-mb 2048 Audinux.iso /dev/sdb
```

To add both data persistency add home persistency on your USB key:
```
$ livecd-iso-to-disk --reset-mbr --format --msdos --unencrypted-home --overlay-size-mb 2048 --home-size-mb 2048 Audinux.iso /dev/sdb
```

You can find a lot of informations related to USB stick and tools to generate these sticks here:
https://docs.pagure.org/docs-fedora/create-and-use-live-image.html

How to use a spec file:

If you use a red hat derivative, you can rebuild the rpm packages from the spec file.
Most of the time, you can copy the .spec file in your rpmbuild/SPEC directory.
Some times, there are some sources package to copy in rpmbuild/SOURCE directory. You have to check is the spec file, there are some indications on how to get the source code.

After that, if there are no indications on how to get the source code:
```
$ spectool -g <package_name>.spec
```
in rpmbuild/SPEC.
This command will download the some required source files.
You must then move the downloaded files from rpmbuild/SPEC to rpmbuild/SOURCE.
Otherwise, have a look in the spec file for instructions on how to get the source code.

And now, it's time to build the package:
```
$ rpmbuild -ba .spec
```
The package to be manually installed via dnf / yum or rpm are located in rpmbuild/RPMS
The source package is located in rpmbuild/SRPMS.

You can also check the following link:
https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/

# To test a GUI packages:

Install the package to be tested + dnf (if you want to install something else) + libX11-xcb (some GUI requires this package to be able to start inside the chroot).
```
$ mock -r /etc/mock/fedora-33-x86_64.cfg --dnf --install linux-show-player-0.5.2-1.fc33.noarch.rpm dnf libX11-xcb
```

Now, enable X session connections to the host:
```
$ xhost +
```

Then, start a shell chroot (and enable network connection if you want to complete manually the installation):
```
$ mock -r /etc/mock/fedora-33-x86_64.cfg --enable-network --shell
```

Export the host display when you are in the chroot:
```
<mock-chroot> sh-5.0# export DISPLAY=:0.0
```

And now start the application you wanted to test:
```
<mock-chroot> sh-5.0# linux-show-player
```

After the tests, exit from the chroot:
```
<mock-chroot> sh-5.0# exit
```

And cleanup the chroot:
```
$ mock -r /etc/mock/fedora-33-x86_64.cfg --clean
```

# Addentum

For livecd-creator, there is problem during fsck phase and I needed to comment out a test:
```
diff --git a/imgcreate/fs.py b/imgcreate/fs.py
index bd03075..2023050 100644
--- a/imgcreate/fs.py
+++ b/imgcreate/fs.py
@@ -142,9 +142,9 @@ def resize2fs(fs, size=None, minimal=False, ops=''):
 
     if ops != 'nocheck':
         ret = e2fsck(fs)
-        if ret != 0:
-            raise ResizeError("fsck after resize returned an error (%d)!" %
-                              (ret,))
+        #if ret != 0:
+        #    raise ResizeError("fsck after resize returned an error (%d)!" %
+        #                      (ret,))
 
     return 0
```
Bug in livecd-creator:
```
 Exécution du scriptlet: kernel-core-5.8.11-200.fc32.x86_64                                                                                                 1803/1803 
/etc/dracut.conf.d/99-liveos.conf:filesystems+="vfat msdos isofs ext4 xfs btrfs squashfs "
/etc/dracut.conf.d/99-liveos.conf:add_drivers+="sr_mod sd_mod ide-cd cdrom =ata sym53c8xx aic7xxx ehci_hcd uhci_hcd ohci_hcd usb_storage usbhid uas firewire-sbp2 firewire-ohci sbp2 ohci1394 ieee1394 mmc_block sdhci sdhci-pci pata_pcmcia mptsas virtio_blk virtio_pci virtio_scsi virtio_net virtio_mmio virtio_balloon virtio-rng  "

dracut: WARNING: <key>+=" <values> ": <values> should have surrounding white spaces!
dracut: WARNING: This will lead to unwanted side effects! Please fix the configuration file.

dracut: No '/dev/log' or 'logger' included for syslog logging
dracut-install: ERROR: installing 'sr_mod'
dracut: FAILED:  /usr/lib/dracut/dracut-install -D /var/tmp/dracut.P90ngs/initramfs --kerneldir /lib/modules/5.8.11-200.fc32.x86_64/ -m sr_mod sd_mod ide_cd cdrom =ata sym53c8xx aic7xxx ehci_hcd uhci_hcd ohci_hcd usb_storage usbhid uas firewire-sbp2 firewire-ohci sbp2 ohci1394 ieee1394 mmc_block sdhci sdhci-pci pata_pcmcia mptsas virtio_blk virtio_pci virtio_scsi virtio_net virtio_mmio virtio_balloon virtio-rng
dracut-install: ERROR: installing 'ext4'
dracut: FAILED:  /usr/lib/dracut/dracut-install -D /var/tmp/dracut.P90ngs/initramfs --kerneldir /lib/modules/5.8.11-200.fc32.x86_64/ -m vfat msdos isofs ext4 xfs btrfs squashfs
```

After installing grub2-efi-x64-cdboot in the ks file:
```
The authconfig command is not available.
Removed /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
success
The 'rhgb' entity is not available.
The '/usr/lib/anaconda-runtime/checkisomd5' entity is not available.
The 'checkisomd5' entity is not available.
The 'rhgb' entity is not available.
The '/usr/lib/anaconda-runtime/checkisomd5' entity is not available.
The 'checkisomd5' entity is not available.
Unmounting directory /var/tmp/imgcreate-rk0djegr/install_root
Losetup remove /dev/loop1
Traceback (most recent call last):
  File "/home/collette/repositories/github/livecd-tools/tools/livecd-creator", line 258, in <module>
    sys.exit(main())
  File "/home/collette/repositories/github/livecd-tools/tools/livecd-creator", line 232, in main
    creator.configure()
  File "/home/collette/repositories/github/livecd-tools/imgcreate/creator.py", line 800, in configure
    self._create_bootconfig()
  File "/home/collette/repositories/github/livecd-tools/imgcreate/live.py", line 259, in _create_bootconfig
    self._configure_bootloader(self.__ensure_isodir())
  File "/home/collette/repositories/github/livecd-tools/imgcreate/live.py", line 843, in _configure_bootloader
    self._configure_efi_bootloader(isodir)
  File "/home/collette/repositories/github/livecd-tools/imgcreate/live.py", line 829, in _configure_efi_bootloader
    cfg += self.__get_efi_image_stanzas(isodir, self.name)
  File "/home/collette/repositories/github/livecd-tools/imgcreate/live.py", line 796, in __get_efi_image_stanzas
    cfg += self.__get_efi_image_stanza(fslabel = self.fslabel,
  File "/home/collette/repositories/github/livecd-tools/imgcreate/live.py", line 774, in __get_efi_image_stanza
    if self._isDracut:
AttributeError: 'x86LiveImageCreator' object has no attribute '_isDracut'
```

With:
```
dracut-live
grub2
grub2-tools
grub2-efi
# grub2-efi-x64-cdboot
shim-x64
# shim-unsigned-x64

kernel
kernel-modules
kernel-modules-extra
kernel-tools
```

```
The 'rhgb' entity is not available.
The '/usr/lib/anaconda-runtime/checkisomd5' entity is not available.
The 'checkisomd5' entity is not available.
Missing EFI file (/boot/efi/EFI/*/gcdx64.efi)
Missing EFI file (/boot/efi/EFI/*/fonts/unicode.pf2)
Failed to copy EFI files, no EFI Support will be included.
usage: mkefiboot [-h] [--debug] [-d] [-a] [-l LABEL] [-i ICONFILE] [-n DISKNAME] [-p PRODUCT] EFIBOOTDIR OUTPUTFILE
mkefiboot: error: /var/tmp/imgcreate-d14k30jg/iso-2murjnwc/EFI/BOOT is not a directory
usage: mkefiboot [-h] [--debug] [-d] [-a] [-l LABEL] [-i ICONFILE] [-n DISKNAME] [-p PRODUCT] EFIBOOTDIR OUTPUTFILE
mkefiboot: error: /var/tmp/imgcreate-d14k30jg/iso-2murjnwc/EFI/BOOT is not a directory
setfiles: /etc/selinux/targeted/contexts/files/file_contexts: line 1394 has invalid context system_u:object_r:motd_var_run_t:s0
setfiles: /etc/selinux/targeted/contexts/files/file_contexts: line 1394 has invalid context system_u:object_r:motd_var_run_t:s0
/etc/selinux/targeted/contexts/files/file_contexts: Invalid argument
Error creating Live CD : SELinux relabel failed.
Unmounting directory /var/tmp/imgcreate-d14k30jg/install_root
Losetup remove /dev/loop1
```

To use the "patched" version of livecdtools:
```
$ git clone https://github.com/ycollet/livecd-tools.git
$ git checkout livecd-tools-27.1
$ git cherry-pick 27fefb509baf8642b5e382c56e0a941cf81ba7b2
$ git cherry-pick 487f1d24030c30897485365a399500b631dd36c4
$ export PYTHONPATH=<livecd-tools-dir>:$PYTHONPATH
$ export PATH=<livecd-tools-dir>/tools:PATH

$ livecd-creator --verbose --config=fedora-32-live-jam-xfce.ks --fslabel=Audinux --releasever 32
```

Manage kernel-rt-mao in livecd-creator:
In /usr/lib/python3.8/site-packages/imgcreate/live.py:
* at the beginning of "def __is_default_kernel", add

    if kernel.startswith(b"kernel-rt"):
        return False

    if kernel.startswith(b"kernel-core"):
        return False

* in def __get_image_stanzas(self, isodir):
  remove
              elif kernel.startswith("kernel-"):
                long = "%s (%s)" % (self.product, kernel[7:])

In /usr/lib/python3.8/site-packages/imgcreate/fs.py:
In def resize2fs(fs, size=None, minimal=False, ops=''):

	# COMMENT THIS PART
        #if ret != 0:
        #    raise ResizeError("fsck after resize returned an error (%d)!" %
        #                      (ret,))
