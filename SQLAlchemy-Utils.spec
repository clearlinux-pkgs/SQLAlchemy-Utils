#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SQLAlchemy-Utils
Version  : 0.36.1
Release  : 46
URL      : https://files.pythonhosted.org/packages/85/d8/e889f8071c17773ca0ea3a67a4897ca008e7aff4e5bde0e5b9ef1ee29f1f/SQLAlchemy-Utils-0.36.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/d8/e889f8071c17773ca0ea3a67a4897ca008e7aff4e5bde0e5b9ef1ee29f1f/SQLAlchemy-Utils-0.36.1.tar.gz
Summary  : Various utility functions for SQLAlchemy.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: SQLAlchemy-Utils-license = %{version}-%{release}
Requires: SQLAlchemy-Utils-python = %{version}-%{release}
Requires: SQLAlchemy-Utils-python3 = %{version}-%{release}
Requires: Babel
Requires: SQLAlchemy
Requires: anyjson
Requires: cryptography
Requires: ipaddr
Requires: passlib
Requires: six
BuildRequires : Babel
BuildRequires : SQLAlchemy
BuildRequires : anyjson
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : ipaddr
BuildRequires : passlib
BuildRequires : six

%description
SQLAlchemy-Utils
----------------

Various utility functions and custom data types for SQLAlchemy.

%package license
Summary: license components for the SQLAlchemy-Utils package.
Group: Default

%description license
license components for the SQLAlchemy-Utils package.


%package python
Summary: python components for the SQLAlchemy-Utils package.
Group: Default
Requires: SQLAlchemy-Utils-python3 = %{version}-%{release}
Provides: sqlalchemy-utils-python

%description python
python components for the SQLAlchemy-Utils package.


%package python3
Summary: python3 components for the SQLAlchemy-Utils package.
Group: Default
Requires: python3-core
Provides: pypi(SQLAlchemy-Utils)

%description python3
python3 components for the SQLAlchemy-Utils package.


%prep
%setup -q -n SQLAlchemy-Utils-0.36.1
cd %{_builddir}/SQLAlchemy-Utils-0.36.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582917340
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SQLAlchemy-Utils
cp %{_builddir}/SQLAlchemy-Utils-0.36.1/LICENSE %{buildroot}/usr/share/package-licenses/SQLAlchemy-Utils/03648fd95f199cb384e921cebbdc6b42ef07cb96
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SQLAlchemy-Utils/03648fd95f199cb384e921cebbdc6b42ef07cb96

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
