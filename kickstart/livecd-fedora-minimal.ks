lang en_US.UTF-8
keyboard us
timezone US/Eastern
auth --useshadow --passalgo=sha512
# FAILS IF ENFORCING
# selinux --enforcing
firewall --disabled
part / --size 2048

repo --name=development --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=rawhide&arch=$basearch

%packages
@standard

kernel
kernel-modules
kernel-modules-extra
kernel-tools
kernel-rt-mao

shim-x64
grub2-efi-x64-cdboot

%end
