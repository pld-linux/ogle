Summary:	DVD Player
Summary(pl):	Program do odtwarzania filmów z DVD
Name:		ogle
Version:	0.9.2
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	a76a9892bdb807a4bcf859d15a91f0f9
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	XFree86-devel
BuildRequires:	a52dec-libs-devel >= 0.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdcss-devel >= 1.2.2
BuildRequires:	libdvdread-devel >= 0.9.4
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
(the first) DVD player for Linux that supports DVD menus!

%description -l pl
(pierwszy) odtwarzacz DVD dla Linuksa obs³uguj±cy DVD menu!

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

%build
cp -f /usr/share/automake/config.sub .
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-xmltest
sed -i -e "s,@XML_CFLAGS@,`xml2-config --cflags`,g" {ac3,dvd_cli,mpeg2_video,ogle,vmg}/Makefile
cp libtool libtool.ok
sed -e 's#AS="$(CC)"#AS="$CC"#g' libtool.ok > libtool
chmod 755 libtool
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%post	-p "/sbin/ldconfig -n %{_libdir}/ogle"
%postun	-p "/sbin/ldconfig -n %{_libdir}/ogle"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ogle
%attr(755,root,root) %{_libdir}/ogle/ogle_*
%attr(755,root,root) %{_libdir}/ogle/lib*.so.*.*
%{_mandir}/man?/*
%{_datadir}/ogle*

%files devel
%defattr(644,root,root,755)
%{_libdir}/ogle/lib*.la
%attr(755,root,root) %{_libdir}/ogle/lib*.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/ogle/lib*.a
