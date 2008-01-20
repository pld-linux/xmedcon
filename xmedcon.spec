# TODO: tpc
Summary:	(X)MedCon - image conversion utility
Summary(pl.UTF-8):	(X)MedCon - narzędzie do konwersji obrazów
Name:		xmedcon
Version:	0.10.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/xmedcon/%{name}-%{version}.tar.bz2
# Source0-md5:	fdd0f929ae6e4c477b993a694b69d303
Patch0:		%{name}-link.patch
URL:		http://xmedcon.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project stands for Medical Image Conversion. It consists of a
library, a flexible command-line utility and a graphical front-end
based on GTK+ toolkit.

Its main purpose is image conversion while preserving valuable medical
study information. The currently supported formats are: Acr/Nema 2.0,
Analyze (SPM), Concorde/uPET, DICOM 3.0, CTI ECAT 6/7, InterFile 3.3
and PNG or Gif87a/89a towards desktop applications.

%description -l pl.UTF-8
Ten projekt ma na celu konwersję obrazów medycznych. Składa się z
biblioteki, elastycznego narzędzia linii poleceń i graficznego
interfejsu opartego na bibliotece GTK+.

Głównym celem programu jest konwersja obrazów z zachowaniem
wartościowych informacji medycznych. Aktualnie obsługiwane formaty to:
Acr/Nema 2.0, Analyze (SPM), Concorde/uPET, DICOM 3.0, CTI ECAT 6/7,
InterFile 3.3 oraz PNG lub Gif87a/89a na potrzeby aplikacji
użytkownika.

%package -n medcon
Summary:	MedCon command-line conversion utility
Summary(pl.UTF-8):	MedCon - narzędzie do konwersji z linii poleceń
Group:		Applications/Graphics
Requires:	%{name}-libs = %{version}-%{release}

%description -n medcon
MedCon command-line medical image conversion utility.

%description -n medcon -l pl.UTF-8
MedCon - narzędzie do konwersji obrazów medycznych z linii poleceń.

%package libs
Summary:	(X)MedCon medical image conversion library
Summary(pl.UTF-8):	Biblitoka (X)MedCon do konwersji obrazów medycznych
Group:		Libraries

%description libs
(X)MedCon medical image conversion library.

%description libs -l pl.UTF-8
Biblitoka (X)MedCon do konwersji obrazów medycznych.

%package devel
Summary:	Header files for (X)MedCon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki (X)MedCon
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	libpng-devel
Requires:	zlib-devel

%description devel
Header files for (X)MedCon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki (X)MedCon.

%package static
Summary:	Static (X)MedCon library
Summary(pl.UTF-8):	Statyczna biblioteka (X)MedCon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static (X)MedCon library.

%description static -l pl.UTF-8
Statyczna biblioteka (X)MedCon.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmedcon
%{_mandir}/man1/xmedcon.1*

%files -n medcon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/medcon
%{_mandir}/man1/medcon.1*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS README REMARKS
%attr(755,root,root) %{_libdir}/libmdc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmdc.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmedcon-config
%attr(755,root,root) %{_libdir}/libmdc.so
%{_libdir}/libmdc.la
%{_includedir}/medcon.h
%{_includedir}/m-*.h
%{_aclocaldir}/xmedcon.m4
%{_mandir}/man1/xmedcon-config.1*
%{_mandir}/man3/medcon.3*
%{_mandir}/man4/m-*.4*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmdc.a
