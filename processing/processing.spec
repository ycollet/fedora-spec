#
# spec file for package processing
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global gversion  3.5.4
%global grevision 270

# Disable production of debug package.
%global debug_package %{nil}

Name:           processing
Version:        %{gversion}.%{grevision}
Release:        1
Summary:        Processing Development Environment (PDE)
# Core is LGPL, others are GPL
License:        GPL-2.0+ and LGPL-2.0+
Group:          Development/Tools/IDE
Url:            https://processing.org/
# Source0 https://github.com/processing/processing/archive/processing-%{grevision}-%{gversion}.tar.gz
Source0:        https://download.processing.org/%{name}-%{gversion}-linux64.tgz
Source1:        %{name}.desktop

# Compiled, do not need JDK and ant
#BuildRequires:  ant
#BuildRequires:  java-devel >= 1.7.0
# Built-in JRE
#Requires:       java >= 1.7.0
# Avoid .so files being added to dependency list

AutoReqProv:    no
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64

%description
Processing is a flexible software sketchbook and a language for learning how to code within the context of the visual arts. Since 2001, Processing has promoted software literacy within the visual arts and visual literacy within technology. There are tens of thousands of students, artists, designers, researchers, and hobbyists who use Processing for learning and prototyping.

- Free to download and open source
- Interactive programs with 2D, 3D or PDF output
- OpenGL integration for accelerated 2D and 3D
- For GNU/Linux, Mac OS X, and Windows
- Over 100 libraries extend the core software
- Well documented, with many books available

%prep
%setup -qn processing-%{gversion}

%build

%install
install -dm 0755 %{buildroot}/opt/%{name}
cp -R * %{buildroot}/opt/%{name}/

install -dm 0755 %{buildroot}/%{_datadir}/pixmaps
install -m 0644 lib/icons/pde-256.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -dm 0755 %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Mar 14 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.4-1
- adjustement for Fedora 29 / 30 + update to 3.5.4-1

* Wed Sep 28 2016 guoyunhebrave@gmail.com
- Add _service file. Download binary tarball from Github

* Sun Sep 18 2016 guoyunhebrave@gmail.com
- Update to 3.2.1

* Thu Nov 24 2011 lars@linux-schulserver.de
- update to 1.5.1
