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
