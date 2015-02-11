Summary:	OpenSSH public key management tool
Name:		ssh-keydb
Version:	0.2
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	https://pypi.python.org/packages/2.7/s/ssh-keydb/ssh_keydb-%{version}dev-py2.7.egg
# Source0-md5:	bdee78b4a62515e72cb9244efdf5c566
URL:		https://code.google.com/p/ssh-keydb/
BuildRequires:	python >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSSH public key management tool.

%prep
%setup -qc

mv ssh_keydb/COPYING .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
cp -a ssh_keydb $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/ssh_keydb
%{py_sitescriptdir}/ssh_keydb/*.py[co]
%dir %{py_sitescriptdir}/ssh_keydb/plugins
%{py_sitescriptdir}/ssh_keydb/plugins/*.py[co]
