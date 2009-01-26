%define Werror_cflags %nil

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Print dialog and printer manager for Xfce
Name:		xfprint
Version:	4.5.99.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	a2ps
Buildrequires:	cups-devel
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
Requires:	a2ps
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

# disable rpath
chrpath -d %{buildroot}/%{_libdir}/xfce4/xfprint-plugins/*.so

%find_lang %{name}

desktop-file-install \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_libdir}/xfce4/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/doc/*
%{_datadir}/gtk-doc/html/

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/xfprint-1.0.pc
%{_libdir}/libxfprint.*a
%{_libdir}/libxfprint.so
%dir %{_includedir}/xfce4/libxfprint
%{_includedir}/xfce4/libxfprint/*
