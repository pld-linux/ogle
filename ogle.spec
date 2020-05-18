Summary:	DVD Player
Summary(pl.UTF-8):	Program do odtwarzania filmów z DVD
Name:		ogle
Version:	0.9.2
Release:	12
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	a76a9892bdb807a4bcf859d15a91f0f9
Patch0:		%{name}-cvs-20070625.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-libdvdread4.patch
Patch3:		am.patch
Patch4:		format-security.patch
URL:		http://www.dtek.chalmers.se/~dvd/
BuildRequires:	a52dec-libs-devel >= 0.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdcss-devel >= 1.2.2
BuildRequires:	libdvdread-devel >= 4.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.5
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
(the first) DVD player for Linux that supports DVD menus!

%description -l pl.UTF-8
(pierwszy) odtwarzacz DVD dla Linuksa obsługujący DVD menu!

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl.UTF-8):	Pliki nagłówkowe wymagane przez programy używające libaviplay
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2-devel >= 2.4.5

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
libaviplay.

%package static
Summary:	Static libaviplay libraries
Summary(pl.UTF-8):	Statyczne biblioteki libaviplay
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libaviplay libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libaviplay.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-libdir-suffix=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/ifo_dump
%attr(755,root,root) %{_bindir}/ogle
%dir %{_libdir}/ogle
%attr(755,root,root) %{_libdir}/ogle/libdvdcontrol.so.*
%attr(755,root,root) %{_libdir}/ogle/libmsgevents.so.*
%dir %{_libexecdir}/ogle
%attr(755,root,root) %{_libexecdir}/ogle/ogle_*
%{_mandir}/man1/ogle.1*
%{_mandir}/man5/oglerc.5*
%{_datadir}/ogle

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ogle/libdvdcontrol.so
%attr(755,root,root) %{_libdir}/ogle/libmsgevents.so
%{_libdir}/ogle/libdvdcontrol.la
%{_libdir}/ogle/libmsgevents.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/ogle/libdvdcontrol.a
%{_libdir}/ogle/libmsgevents.a
