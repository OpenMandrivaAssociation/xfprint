
%define lib_major       0
%define lib_name        %mklibname xfprint %{lib_major}
%define version		4.4.1
%define release		1
%define __libtoolize /bin/true

Summary: 	Print dialog and printer manager for Xfce
Name: 		xfprint
Version: 	%{version}
Release: 	%mkrel %{release}
License:	BSD
URL: 		http://www.xfce.org/
Source0: 	%{name}-%{version}.tar.bz2
Group:		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	a2ps 
BuildRequires: 	glib2-devel >= 2.0.6
BuildRequires: 	libxfcegui4-devel >= %{version}
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	a2ps
Buildrequires:	cups-devel 
BuildRequires:	cups-common
BuildRequires:	chrpath

%description
Xfprint contains a print dialog and a printer manager for Xfce.

%package -n %{lib_name}
Summary:	Libraries for the Xfce Printer Manager
Group:		Graphical desktop/Xfce

%description -n %{lib_name}
Libraries for the Xfce Printer Manager.

%package -n %{lib_name}-devel
Summary:	Libraries and header files for the Xfce Printer Manager
Group:		Development/Other
Requires:	%{lib_name} = %{version}
Provides:	xfprint-devel

%description -n %{lib_name}-devel
Libraries and header files for the Xfce Printer Manager.


%prep
%setup -q -n %{name}-%{version}

%configure2_5x --enable-letter

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/xfprint-plugins/*.*a 
rm -f %{buildroot}/%{_libdir}/xfce4/mcs-plugins/*.*a

# disable rpath
chrpath -d $RPM_BUILD_ROOT/%{_libdir}/xfce4/xfprint-plugins/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_bindir}/* 
%{_libdir}/xfce4/*
%{_datadir}/applications/*.desktop
#%{_datadir}/icons/* 
%{_datadir}/xfce4/doc/*

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libxfprint.so.*
%{_datadir}/gtk-doc/html/
%{_iconsdir}/hicolor/*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/xfprint-1.0.pc
%{_libdir}/libxfprint.*a
%{_libdir}/libxfprint.so
%dir %{_includedir}/xfce4/libxfprint
%{_includedir}/xfce4/libxfprint/*


