# Created by pyp2rpm-3.3.5
%global pypi_name transifex-client

Name:           python-%{pypi_name}
Version:        0.14.3
Release:        1
Summary:        A command line interface for Transifex
Group:          Development/Python
License:        GPLv2
URL:            https://www.transifex.com
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(gitpython) < 4
BuildRequires:  python3dist(python_slugify > 5
BuildRequires:  (python3dist(requests) >= 2.19.1 with python3dist(requests) < 3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) < 2
BuildRequires:  (python3dist(urllib3) >= 1.24.2 with python3dist(urllib3) < 2)

%description
Transifex Command-Line Tool [![image]( [![image]( [![codecov]( [![PyPI
version](

%prep
%autosetup  -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/tx
%{python3_sitelib}/txclib
%{python3_sitelib}/transifex_client-%{version}-py%{python3_version}.egg-info

