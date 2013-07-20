%define		old_libpynac		%mklibname pynac
%define		old_libpynac_devel	%mklibname pynac -d

%{!?pyver: %global pyver %(%{__python} -c "import sys ; print(sys.version[:3])")}

Name:           pynac
Version:        0.2.5
Release:        2%{?dist}
Summary:        Manipulation of symbolic expressions
License:        GPLv2+
URL:            http://pynac.sagemath.org/
#Source0:        http://pynac.sagemath.org/download/pynac-%%{version}.spkg
Source0:        http://sagemath.org/packages/standard/pynac-%{version}.spkg
Source1:        %{name}.rpmlintrc

BuildRequires:  python-devel
BuildRequires:	readline-devel
%rename %{old_libpynac}

%description
Pynac is a derivative of the C++ library GiNaC, which allows manipulation of
symbolic expressions. It currently provides the backend for symbolic
expressions in Sage.

The main difference between Pynac and GiNaC is that Pynac relies on Sage to
provide the operations on numerical types, while GiNaC depends on CLN for this
purpose.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%rename %{old_libpynac_devel}

%description    devel
Headers and libraries for developing with %{name}.

%prep
%setup -q

%build
cd src
export CXXFLAGS="%{optflags} -I%{_includedir}/python%{pyver}"
%configure --disable-static
make %{?_smp_mflags}

%install
cd src
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc src/AUTHORS src/ChangeLog src/COPYING src/NEWS src/README
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
