%define Werror_cflags %nil

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Print dialog and printer manager for Xfce
Name:		xfprint
Version:	4.6.1
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.6.0
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

export LIBS="-lX11"
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
%{_libdir}/libxfprint.so
%dir %{_includedir}/xfce4/libxfprint
%{_includedir}/xfce4/libxfprint/*


%changelog
* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 4.6.1-5
+ Revision: 790105
- Fix gold linker build

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild
    - drop old stuff from spec file

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-4
+ Revision: 633063
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-3mdv2011.0
+ Revision: 579670
- rebuild for new xfce 4.7.0

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.1
+ Revision: 543316
- rebuild for mdv 2010.1

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368581
- update to new version 4.6.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349261
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345706
- New upstream release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333952
- update to new version 4.5.99.1
- use versionate buildrequires on xfconf-devel

* Thu Jan 15 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329688
- update to new version 4.5.93
- add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-2mdv2009.1
+ Revision: 303497
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Tue Nov 11 2008 Oden Eriksson <oeriksson@mandriva.com> 4.5.91-2mdv2009.1
+ Revision: 302196
- rebuilt against new libxcb

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294764
- Xfce4.6 beta1 is landing on cooker
- tune up buildrequires

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-4mdv2009.0
+ Revision: 269798
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2009.0
+ Revision: 194469
- do not package COPYING ile

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 157760
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109976
- New release 4.4.2

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-4mdv2008.0
+ Revision: 71321
- new devel library policy
- fix provides

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 71241
- remove X-MandrivaLinux from desktop file
- update description

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 32889
- drop __libtoolize
- tune up desktop file
- enable cups
- use macros in %%post and %%postun
- spec file clean

* Mon Apr 23 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 17607
- New release 4.4.1

