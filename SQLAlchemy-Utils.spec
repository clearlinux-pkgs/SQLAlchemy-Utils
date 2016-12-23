#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SQLAlchemy-Utils
Version  : 0.32.9
Release  : 18
URL      : http://pypi.debian.net/SQLAlchemy-Utils/SQLAlchemy-Utils-0.32.9.tar.gz
Source0  : http://pypi.debian.net/SQLAlchemy-Utils/SQLAlchemy-Utils-0.32.9.tar.gz
Summary  : Various utility functions for SQLAlchemy.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: SQLAlchemy-Utils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
SQLAlchemy-Utils
================
|Build Status| |Version Status| |Downloads|
Various utility functions, new data types and helpers for SQLAlchemy.

%package python
Summary: python components for the SQLAlchemy-Utils package.
Group: Default
Provides: sqlalchemy-utils-python

%description python
python components for the SQLAlchemy-Utils package.


%prep
%setup -q -n SQLAlchemy-Utils-0.32.9

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
