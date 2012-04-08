%define Werror_cflags %nil

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Print dialog and printer manager for Xfce
Name:		xfprint
Version:	4.6.1
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	libxfcegui4-devel >= 4.6.0
BuildRequires:	xfconf-devel >= 4.6.0
BuildRequires:	a2ps
Buildrequires:	cups-devel
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
Requires:	a2ps
Requires:	%{libname} = %{version}-%{release}

%description
The printing helper is a graphical frontend for printing,
a printer management, and a job queue management. It doesn't
let you configure printers but only use printing systems that
have already been configured properly.

%package -n %{libname}
Summary:	Libraries for the Xfce Printer Manager
Group:		Graphical desktop/Xfce

%description -n %{libname}
Libraries for the Xfce Printer Manager.

%package -n %{develname}
Summary:	Libraries and header files for the Xfce Printer Manager
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%mklibname %{name} 0 -d
Obsoletes:	%mklibname %{name} 0 -d

%description -n %{develname}
Libraries and header files for the Xfce Printer Manager.

%prep
%setup -q

%configure2_5x \
	--disable-letter \
	--enable-cups \
	--disable-static

%install
%makeinstall_std

# disable rpath
chrpath -d %{buildroot}/%{_libdir}/xfce4/xfprint-plugins/*.so

%find_lang %{name} %{name}.lang

desktop-file-install \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/doc/*
%{_datadir}/gtk-doc/html/

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/xfprint-1.0.pc
%{_libdir}/libxfprint.*a
%{_libdir}/libxfprint.so
%dir %{_includedir}/xfce4/libxfprint
%{_includedir}/xfce4/libxfprint/*
