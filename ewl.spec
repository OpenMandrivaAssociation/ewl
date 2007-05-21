%define	name	ewl
%define	version 0.0.4.008
%define release %mkrel 1

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment widget library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		System/Libraries
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.038, ecore-devel >= 0.9.9.038, edb-devel
BuildRequires:	multiarch-utils
BuildRequires:  edje-devel >= 0.5.0.038, embryo-devel, efreet-devel >= 0.0.3.002
BuildRequires:  emotion-devel, epsilon-devel

%description
Enlightened Widget Library (EWL)  provides a widget abstraction to creating
GUI's using Evas and Edje. The use of edje allows for easy creation of fairly
advanced themes.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%_sysconfdir/%name/%name.cfg
%dir %{_datadir}/%name

%{_datadir}/%name/themes
%{_datadir}/%name/images
%{_libdir}/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/%name
%{_bindir}/%name-config
%multiarch %multiarch_bindir/%name-config
%{_datadir}/aclocal/*.m4
%{_datadir}/%name/examples


%changelog
* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.0.4.008-1mdv2008.0
- snapshot 20070516


* Tue Apr 24 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.4.007-1mdv2008.0
+ Revision: 17858
- 0.0.4.007
 - Don't buildrequire emotion-devel
- Import ewl



* Sat Mar 25 2006 Austin Acton <austin@mandriva.org> 0.0.4.006-0.20060323.1mdk
- new cvs checkout
- buildrequires embryo

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.0.4.005-0.20060216.1mdk
- new cvs checkout

* Wed Jan 18 2006 Austin Acton <austin@mandriva.org> 0.0.4.005-0.20060117.1mdk
- new cvs checkout

* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.0.4.004-0.20051124.1mdk
- new cvs checkout

* Fri Nov 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.0.4.004-0.20051109.2mdk
- rebuild against openssl-0.9.8

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.0.4.004-0.20051109.1mdk
- new cvs checkout

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.4.004-0.20050904.2mdk
- Fix BuildRequires

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.0.4.004-0.20050904.1mdk
- new cvs checkout

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.0.4.004-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.0.4.003-0.20050627.1mdk
- new cvs checkout

* Wed Jun 08 2005 Austin Acton <austin@mandriva.org> 0.0.4.003-0.20050608.1mdk
- new cvs checkout

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.0.4.003-0.20050524.1mdk
- new cvs checkout
- multiarch binaries

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 0.0.4.003-0.20050511.1mdk
- initial package
