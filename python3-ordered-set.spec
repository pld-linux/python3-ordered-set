# Conditional build:
%bcond_with	tests	# unit tests

%define		module	ordered-set
Summary:	A mutable set that remembers the order of its entries
Name:		python3-%{module}
Version:	4.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	2a9ba8d1a962c26f9a4fbe246b62ee77
URL:		https://github.com/seperman/ordered-set
BuildRequires:	python3-modules >= 1:3.2
#BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An OrderedSet is a mutable data structure that is a hybrid of a list
and a set. It remembers the order of its entries, and every entry has
an index number that can be looked up.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitescriptdir}/ordered_set
%{py3_sitescriptdir}/ordered_set/*.py
%{py3_sitescriptdir}/ordered_set/__pycache__
%{py3_sitescriptdir}/ordered_set-%{version}-py*.egg-info

