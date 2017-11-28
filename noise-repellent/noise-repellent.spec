%global debug_package %{nil}

# Global variables for github repository
%global commit0 a949eba8427228332781e8b153fe0400f97215a5
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           noise-repellent-lv2
Version:        0.1.4.%{shortcommit0}
Release:        1%{?dist}
Summary:        A lv2 plug-in for broadband noise reduction.

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/lucianodato/noise-repellent
Source0:        https://github.com/lucianodato/noise-repellent/archive/%{commit0}.tar.gz#/noise-repellent-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel
BuildRequires: fftw-devel

%description
A lv2 plug-in for broadband noise reduction.

Features
* Spectral gating and spectral subtraction suppression rule
* Adaptive and manual noise thresholds estimation
* Adjustable noise floor
* Adjustable offset of thresholds to perform over-subtraction
* Time smoothing and a masking estimation to reduce artifacts
* Basic onset detector to avoid transients suppression
* Whitening of the noise floor to mask artifacts and to recover higher frequencies
* Option to listen to the residual signal
* Soft bypass
* Noise profile saved with the session

Limitations
* The plug-in will introduce latency so it's not appropriate to be used while recording (23 ms for 44.1 kHz)
* It was developed to be used with Ardour however it is known to work with other hosts

%prep
%setup -qn noise-repellent-%{commit0}

%build

%make_build

%install 
%make_install PREFIX=%{buildroot}/usr LV2DIR=$PREFIX/%{_libdir}/lv2/ OPTIMIZATIONS= 

%files
%{_libdir}/lv2/*

%changelog
* Tue Nov 28 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1.4
- Initial build
