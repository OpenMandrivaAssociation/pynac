%define		_disable_ld_as_needed		1
%define		_disable_ld_no_undefined	1

%define		name		pynac
%define		libname		%mklibname %{name}
%define		devname		%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPL
Summary:	Modified GiNaC that replaces the dependency on CLN by Python
Version:	0.2.3
Release:	%mkrel 1
# pynac-%{version}.spkg from sage tarball renamed
Source:		pynac-%{version}.tar.bz2
URL:		http://wiki.sagemath.org/spkg/pynac
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	automake
BuildRequires:	libreadline-devel
BuildRequires:	python-devel

%description
A modified version of GiNaC that replaces the dependency on CLN by Python.

%package	-n %{libname}
Summary:	Modified GiNaC that replaces the dependency on CLN by Python
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libname}
A modified version of GiNaC that replaces the dependency on CLN by Python.

%package	-n %{devname}
Summary:	Modified GiNaC that replaces the dependency on CLN by Python
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	lib%{name} = %{version}-%{release}

%description	-n %{devname}
A modified version of GiNaC that replaces the dependency on CLN by Python.

%prep
%setup -q -n pynac-%{version}/src

autoreconf

%build
%configure --disable-static

%make CPPFLAGS=-I%{py_incdir} PKG_CONFIG_PATH=%{_libdir}/pkgconfig

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files		-n %{devname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
