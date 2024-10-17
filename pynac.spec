%define		old_libpynac		%mklibname pynac
%define		old_libpynac_devel	%mklibname pynac -d

Name:           pynac
Version:        0.6.9
Release:        1
Summary:        Manipulation of symbolic expressions
Group:		Sciences/Mathematics
License:        GPLv2+
URL:            https://www.sagemath.org/packages/upstream/pynac/index.html
Source0:	https://github.com/pynac/pynac/releases/download/pynac-%{version}/pynac-%{version}.tar.bz2
Source1:        %{name}.rpmlintrc

BuildRequires:  python2-devel
BuildRequires:	readline-devel
BuildRequires:	gmp-devel
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
export PYTHON=%__python2
export CC=gcc
export CXX=g++
export CXXFLAGS="%{optflags}"
%configure2_5x --disable-static
%make

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
