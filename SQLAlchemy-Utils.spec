#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SQLAlchemy-Utils
Version  : 0.33.9
Release  : 29
URL      : https://files.pythonhosted.org/packages/7b/2e/7b7634446fcbb37f666a708c366337482d13ffc259e96b2fff93b28a8e24/SQLAlchemy-Utils-0.33.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/2e/7b7634446fcbb37f666a708c366337482d13ffc259e96b2fff93b28a8e24/SQLAlchemy-Utils-0.33.9.tar.gz
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
Requires: enum34
Requires: ipaddr
Requires: passlib
Requires: six
BuildRequires : SQLAlchemy
BuildRequires : buildreq-distutils3
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

%description python3
python3 components for the SQLAlchemy-Utils package.


%prep
%setup -q -n SQLAlchemy-Utils-0.33.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543991460
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SQLAlchemy-Utils
cp LICENSE %{buildroot}/usr/share/package-licenses/SQLAlchemy-Utils/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SQLAlchemy-Utils/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
