Summary:	DVD Player
Summary(pl):	Program do odtwarzania filmów z DVD
Name:		ogle
Version:	0.8.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
URL:		http://www.dtek.chalmers.se/~dvd/
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-a52dec.patch	
BuildRequires:	XFree86-devel
BuildRequires:	a52dec-libs-devel >= 0.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libxml2-devel >= 2.4.5
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
(the first) DVD player for Linux that supports DVD menus!

%description -l pl
(pierwszy) odtwarzacz DVD dla Linuxa obs³uguj±cy DVD menu!

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce libaviplay
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
libaviplay.

%package static
Summary:	Static libaviplay libraries
Summary(pl):	Statyczne biblioteki libaviplay
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libaviplay libraries.

%description static -l pl
Statyczne biblioteki libaviplay.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--disable-xmltest
cp libtool libtool.ok
sed -e 's#AS="$(CC)"#AS="$CC"#g' libtool.ok > libtool
chmod 755 libtool
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

# for some wired reason these are not installed by make install (unless ogle-devel is installed)
if ! [ -f %{_libdir}/ogle/libdvdcontrol.la ] ; then
       install ogle/.libs/libdvdcontrol.lai $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.la
       install ogle/.libs/libdvdcontrol.a $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.a
       install ogle/.libs/libdvdcontrol.so.3.2.0 $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.so.3.2.0
       ln -sf libdvdcontrol.so.3.2.0 $RPM_BUILD_ROOT%{_libdir}/ogle/libdvdcontrol.so
fi

gzip -9nf README

%post	-p "/sbin/ldconfig -n %{_libdir}/ogle"
%postun	-p "/sbin/ldconfig -n %{_libdir}/ogle"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ogle
%attr(755,root,root) %{_libdir}/ogle/ogle_*
%attr(755,root,root) %{_libdir}/ogle/lib*.so.*.*
%{_mandir}/man?/*
%{_datadir}/ogle*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ogle/lib*.la
%attr(755,root,root) %{_libdir}/ogle/lib*.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/ogle/lib*.a
