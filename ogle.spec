Summary:	DVD Player
Summary(pl):	Program do odtwarzania filmów z DVD
Name:		ogle
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/%{name}-%{version}.tar.gz
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
(the first) DVD player for Linux that supports DVD menus!

%description -l pl
(pierwszy) odtwarzacz DVD dla Linuxa obsługujący DVD menu!

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl):	Pliki nagłówkowe wymagane przez programy używające libaviplay
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
libaviplay.

%package static
Summary:	Static libaviplay libraries
Summary(pl):	Statyczne biblioteki libaviplay
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libaviplay libraries.

%description -l pl static
Statyczne biblioteki libaviplay.

%prep
%setup -q

%build
rm -f missing 
rm -f acinclude.m4
libtoolize --copy --force
aclocal
autoconf
automake -a -c

%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

# for some wired reason these are not installed by make install (unless ogle-devel is installed)
if ! [ -f %{_libdir}/ogle/libdvdcontrol.la ] ; then
	install ogle/.libs/libdvdcontrol.lai $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.la
	install ogle/.libs/libdvdcontrol.a $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.a
	install ogle/.libs/libdvdcontrol.so.1.0.0U $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.so.1.0.0
	ln -sf libdvdcontrol.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.so 
fi

%post	-p "/sbin/ldconfig -n %{_libdir}/ogle"
%postun	-p "/sbin/ldconfig -n %{_libdir}/ogle"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ogle/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ogle/lib*.la
%attr(755,root,root) %{_libdir}/ogle/lib*.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/ogle/lib*.a
