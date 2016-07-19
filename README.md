To build the spec file:
- copy it into your rpmbuild/SPEC directory
- run:
```
$ spectool -g to download the source file
```
- copy the source file into rpmbuild/SOURCE
- run:
```
$ rpmbuild -ba filename.spec
```
The result can be found in:
- RPMS/noarch
- RPMS/x86_64

Install the rpm file using yum:
as a root user: 
```
$ yum install filename.rpm
```

To test the rebuild of the package using mock:
```
$ mock -r fedora-22-x86_64 --rebuild polyphone-1.6.0-1.fc22.src.rpm
```

To enable a thirdparty repository, you must add it to /etc/mock/fedora-22-x86_64.cfg for example and then, enable it via the command line. For example:
```
$ mock -r fedora-22-x86_64 --enablerepo=ycollet-linuxmao --rebuild dgedit-0.1-1.fc22.src.rpm
```

The portion added to /etc/mock/fedora-2{1,2,3}-x86_64.cfg is:
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
```

This is the content of the repo conf file found in /etc/yum.repo.d.

To create the LiveCD:

As a root used:
```
$ livecd-creator --verbose --config=fedora-23-live-jam-kde.ks --fslabel=LesCuizines
```

ToDo:
- Add Requires in kxstudio
- Fix portalmod / swh build
- Fix portalmod / mda build
