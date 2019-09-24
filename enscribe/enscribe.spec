%global debug_package %{nil}

Summary: Enscribe creates digital audio watermark images from photgraphic images.
Name:    enscribe
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://www.coppercloudmusic.com/enscribe/
Source0: http://coppercloudmusic.com/enscribe/enscribe-%{version}.tgz
Patch0: enscribe_01-makefile.patch
Patch1: enscribe_02-FFTblocksizenorm.patch
Patch2: enscribe_03-fix-typo.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: gd-devel
BuildRequires: libsndfile-devel
BuildRequires: freetype-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: zlib-devel
BuildRequires: sed

%description
Enscribe creates digital audio watermark images from photgraphic images. 
These images can only be seen using a third party frequency vs time display, 
such as my favorite, Baudline (http://www.baudline.com).
Images are still visible even after such audio mangling techniques as MP3/Ogg 
compression, reverb, chorus, etc. Heavy EQ and flange can stripe out vertical 
sections, but they can also ruin an otherwise good song too.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Force Fedora's optflags
sed -i 's|gcc |gcc %{optflags} |' makefile

%build
rm -rf $RPM_BUILD_ROOT

make DESTDIR=%{buildroot} PREFIX=%{_prefix}

%install

make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

# mkdir -p $RPM_BUILD_ROOT%{_bindir}/
# %__install -m 644 enscribe %{buildroot}%{_bindir}/enscribe

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/*

%changelog
* Tue Sep 24 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- initial release
