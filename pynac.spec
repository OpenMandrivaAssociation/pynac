%define		_disable_ld_as_needed		1
%define		_disable_ld_no_undefined	1

%define		name		pynac
%define		libpynac	%mklibname %{name}
%define		libpynac_devel	%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPLv2+
Summary:	Modified GiNaC that replaces the dependency on CLN by Python
Version:	0.2.4
Release:	1
# pynac-%{version}.spkg from sage tarball renamed
Source:		pynac-%{version}.tar.bz2
URL:		http://wiki.sagemath.org/spkg/pynac
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	automake
BuildRequires:	readline-devel
%py_requires -d

%description
A modified version of GiNaC that replaces the dependency on CLN by Python.

%package	-n %{libpynac}
Summary:	Modified GiNaC that replaces the dependency on CLN by Python
Group:		System/Libraries

%description	-n %{libpynac}
A modified version of GiNaC that replaces the dependency on CLN by Python.

%package	-n %{libpynac_devel}
Summary:	Modified GiNaC that replaces the dependency on CLN by Python
Group:		Development/C++
Requires:	%{libpynac} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libpynac_devel}
A modified version of GiNaC that replaces the dependency on CLN by Python.

%prep
%setup -q -n pynac-%{version}/src

autoreconf

%build
%configure --disable-static

%make CPPFLAGS=-I%{py_incdir} PKG_CONFIG_PATH=%{_libdir}/pkgconfig

%install
%makeinstall_std
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS ChangeLog COPYING NEWS README %{buildroot}%{_docdir}/%{name}

%files		-n %{libpynac}
%doc %{_docdir}/%{name}
%{_libdir}/lib*.so.*

%files		-n %{libpynac_devel}
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


%changelog
* Tue Aug 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2.4-1
+ Revision: 815557
- Update to latest upstream release.

* Mon Aug 29 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2.3-1
+ Revision: 697340
- Update to latest upstream release.

* Wed Nov 10 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.2.1-1mdv2011.0
+ Revision: 595698
- Update to pynac 0.2.1.

* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.2.0.p3-2mdv2011.0
+ Revision: 593486
+ rebuild (emptylog)

* Wed Jul 14 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.2.0.p3-1mdv2011.0
+ Revision: 552962
- Update to version 0.2.0 patchlevel 3.

* Fri Feb 26 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.1.11-1mdv2010.1
+ Revision: 512168
- Update to latest upstream release

* Mon Jan 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.1.10-1mdv2010.1
+ Revision: 486288
- Update to pynac 0.1.10.

* Mon Aug 31 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.1.8.p2-1mdv2010.0
+ Revision: 423113
- update to latest upstream patchlevel (corrects sage trac #6256)

* Wed Jun 17 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.1.8-1mdv2010.0
+ Revision: 386513
- Update to latest upstream release.

* Mon May 18 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-3mdv2010.0
+ Revision: 377373
+ rebuild (emptylog)

* Thu May 14 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-2mdv2010.0
+ Revision: 375749
+ rebuild (emptylog)

* Tue May 12 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-1mdv2010.0
+ Revision: 374979
- Initial import of pynac, required by sagemath (and using it's version).
  Modified GiNaC that replaces the dependency on CLN by Python
  http://wiki.sagemath.org/spkg/pynac
- pynac

