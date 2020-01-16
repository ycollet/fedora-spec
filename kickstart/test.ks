#fedora-livedvd-jam-xfe.ks
# With XFCE Desktop

# Fedora Jam: For Musicians and audio enthusiasts
# Fedora Jam is a spin for anyone interested in creating 
# music 

# Maintainer: Yann Collette <ycollette.nospam@free.fr>

lang fr_FR.UTF-8
keyboard fr-latin9
timezone Europe/Paris

auth --useshadow --passalgo=sha512
# SELinux configuration
selinux --enforcing
firewall --enabled --service=mdns
xconfig --startxonboot
# Clear the Master Boot Record
zerombr
clearpart --all --initlabel
part / --size 16384 --fstype="ext4"
services --disabled="sshd" --enabled="NetworkManager"
network --bootproto=dhcp --device=link --activate
# Shutdown after installation
shutdown
rootpw --plaintext lescuizines

#enable threaded irqs
bootloader --location=none --append="threadirqs nopti"


repo --name=fedora  --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
repo --name=updates --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=updates-released-f$releasever&arch=$basearch

url --mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch

repo --name="CoprLinuxMAO" --baseurl=https://copr-be.cloud.fedoraproject.org/results/ycollet/linuxmao/fedora-$releasever-$basearch/

%packages

@standard
@core
@fonts

%end

#################################
# List packages to be installed #
#################################

%packages

# system packages

# Explicitly specified here:
# <notting> walters: because otherwise dependency loops cause yum issues.
kernel
kernel-modules
kernel-modules-extra
kernel-tools
kernel-rt-mao

# This was added a while ago, I think it falls into the category of
# "Diagnosis/recovery tool useful from a Live OS image".  Leaving this untouched
# for now.
memtest86+

syslinux

# Without this, initramfs generation during live image creation fails: #1242586
dracut-live
grub2
grub2-tools
grub2-efi
#shim
#shim-unsigned

%end
