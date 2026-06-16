Name:      zint
Version:   2.16.0
Release:   2%{?dist}
Summary:   A barcode generator and library
License:   GPLv3+
URL:       http://www.zint.org.uk
Source:    %{name}-%{version}.tar.gz
Group:     Applications/Engineering
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: cmake
BuildRequires: libpng-devel
BuildRequires: zlib-devel

%description
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the library.
Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and
  Kanji character sets.
- Full GS1 support including data verification and automated insertion of
  FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0) characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in the following file formats: PNG, GIF, EPS, WMF, BMP, TIF, SVG.
- Verification stage for SBN, ISBN and ISBN-13 data.


%prep
%setup -q -n %{name}-%{version}/upstream

# remove bundled getopt sources (we use the corresponding Fedora package instead)
rm -rf getopt

%build
%cmake CMakeLists.txt
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_libdir}/cmake
rm -rf $RPM_BUILD_ROOT/%{_includedir}
rm -rf $RPM_BUILD_ROOT/%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}
%{_libdir}/libzint.so*

%changelog

* Sat Feb 1 2020 Harald Oehlmann <oehhar@sourceforge.net> - 2.7.1
- Version -> 2.7.1

* Thu Dec 5 2019 Harald Oehlmann <oehhar@sourceforge.net> - 2.7.0
- Version -> 2.7.0

* Wed Sep 18 2019 Harald Oehlmann <oehhar@sourceforge.net> - 2.6.6
- Version -> 2.6.6

* Mon Sep 1 2019 Harald Oehlmann <oehhar@sourceforge.net> - 2.6.5
- Version -> 2.6.5

* Fri Aug 30 2019 Harald Oehlmann <oehhar@sourceforge.net> - 2.6.4
- Version -> 2.6.4

* Thu Feb 15 2018 Robin Stuart <rstuart114@gmail.com> - 2.6.3
- Version -> 2.6.3

* Sun Oct 22 2017 Robin Stuart <rstuart114@gmail.com> - 2.6.2
- Version -> 2.6.2

* Sun Aug 27 2017 Robin Stuart <rstuart114@gmail.com> - 2.6.1
- Version -> 2.6.1

* Thu May 11 2017 Robin Stuart <rstuart114@gmail.com> - 2.6.0
- Update version number

* Sat May 22 2010 Martin Gieseking <martin.gieseking@uos.de> - 2.3.1-2
- Added patch to fix export issue

* Fri May 21 2010 Martin Gieseking <martin.gieseking@uos.de> - 2.3.1-1
- initial package
