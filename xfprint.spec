%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Print dialog and printer manager for Xfce
Name:		xfprint
Version:	4.4.2
Release:	%mkrel 2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0: 	%{name}-%{version}.tar.bz2
Requires:	a2ps
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	a2ps
Buildrequires:	cups-devel
BuildRequires:	cups-common
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
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
Provides:	xfprint-devel = %{version}-%{release}
Provides:	libxfprint-devel = %{version}-%{release}
Provides:	%mklibname %{name} 0 -d
Obsoletes:	%mklibname %{name} 0 -d

%description -n %{develname}
Libraries and header files for the Xfce Printer Manager.

%prep
%setup -q

%configure2_5x \
	--enable-letter \
	--enable-cups

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded devel files
rm -f %{buildroot}%{_libdir}/xfce4/xfprint-plugins/*.*a
rm -f %{buildroot}%{_libdir}/xfce4/mcs-plugins/*.*a

# disable rpath
chrpath -d %{buildroot}/%{_libdir}/xfce4/xfprint-plugins/*

%find_lang %{name}

desktop-file-install \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
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
