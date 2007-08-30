%define	name ewl
%define version 0.5.1.008
%define release %mkrel 8

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment widget library
Name: 		%{name}
Version:	%{version}
Release: 	%{release}
License: 	BSD
Group: 		System/Libraries
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.038, ecore-devel >= 0.9.9.038, edb-devel >= 1.0.5
BuildRequires:  edje-devel >= 0.5.0.038, embryo-devel >= 0.9.1.038
Buildrequires:	efreet-devel >= 0.0.3.002
BuildRequires:  emotion-devel >= 0.0.1.005
Buildrequires:  epsilon-devel >= 0.3.0.008
Buildrequires:  edje >= 0.5.0.038, embryo >= 0.9.1.038
Buildrequires:  imlib2-devel
BuildRequires:	multiarch-utils
Buildrequires:  libx11-devel

%description
Enlightened Widget Library (EWL)  provides a widget abstraction to creating
GUI's using Evas and Edje. The use of edje allows for easy creation of fairly
advanced themes.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Provides: %name = %version-%release

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}
Conflicts: libewl0-devel

%description -n %libnamedev
%{name} development headers and libraries

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
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
%{_libdir}/*.so.%{major}*

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

