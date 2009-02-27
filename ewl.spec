%define	name ewl
%define version 0.5.3.050
%define release %mkrel 1

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightenment widget library
Name: 		%{name}
Version:	%{version}
Release: 	%{release}
License: 	BSD
Group: 		System/Libraries
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050
BuildRequires:	ecore-devel >= 0.9.9.050
BuildRequires:  edje-devel >= 0.5.0.050, edje => 0.5.0.050
BuildRequires:	embryo-devel >= 0.9.9.050, embryo >= 0.9.9.050
Buildrequires:	efreet-devel >= 0.0.5.050
BuildRequires:  emotion-devel >= 0.1.0.042
Buildrequires:  epsilon-devel >= 0.3.0.012
Buildrequires:  imlib2-devel
Buildrequires:  X11-devel

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
%{name} development headers and libraries.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

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
%{_libdir}/%name/engines/*.so
%{_libdir}/%name/plugins/*.so
%{_libdir}/%name/tests/*.so

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%{_libdir}/%name/engines/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/%name/engines/*.a
%{_libdir}/%name/engines/*.la
%{_libdir}/%name/plugins/*.a
%{_libdir}/%name/plugins/*.la
%{_libdir}/%name/tests/*.a
%{_libdir}/%name/tests/*.la
%{_includedir}/%name
%{_datadir}/%name/examples

