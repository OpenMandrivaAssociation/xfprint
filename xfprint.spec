%define Werror_cflags %nil

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Print dialog and printer manager for Xfce
Name:		xfprint
Version:	4.6.1
Release:	7
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		xfprint-4.6.1-cups-1.6.patch
BuildRequires:	a2ps
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
Buildrequires:	cups-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.6.0
BuildRequires:	pkgconfig(libxfconf-0)
Requires:	a2ps

%description
The printing helper is a graphical frontend for printing,
a printer management, and a job queue management. It doesn't
let you configure printers but only use printing systems that
have already been configured properly.

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/doc/*
%{_datadir}/gtk-doc/html/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the Xfce Printer Manager
Group:		Graphical desktop/Xfce

%description -n %{libname}
Libraries for the Xfce Printer Manager.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and header files for the Xfce Printer Manager
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Libraries and header files for the Xfce Printer Manager.

%files -n %{devname}
%{_libdir}/pkgconfig/xfprint-1.0.pc
%{_libdir}/libxfprint.so
%dir %{_includedir}/xfce4/libxfprint
%{_includedir}/xfce4/libxfprint/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
export LIBS="-lX11"
%configure2_5x \
	--disable-letter \
	--enable-cups \
	--disable-static

%install
%makeinstall_std

# disable rpath
chrpath -d %{buildroot}/%{_libdir}/xfce4/xfprint-plugins/*.so

%find_lang %{name}

desktop-file-install \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

