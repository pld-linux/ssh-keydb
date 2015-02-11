Summary:	OpenSSH public key management tool
Name:		ssh-keydb
Version:	1.0
Release:	0.3
License:	GPL v3
Group:		Applications
#Source0:	https://pypi.python.org/packages/2.7/s/ssh-keydb/ssh_keydb-%{version}dev-py2.7.egg
# tar cjf ssh-keydb.tar ssh-keydb --exclude-vcs
Source0:	%{name}.tar.bz2
# Source0-md5:	d1a9e17cf978a8d61fea6f4ea467df16
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
mv ssh-keydb/* .

mv ssh_keydb/COPYING .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
%{__python} setup.py install \
	--record=INSTALLED_FILES \
	--skip-build \
	--optimize=2 \
	--single-version-externally-managed \
	--root=$RPM_BUILD_ROOT

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ssh-keydb
%dir %{py_sitescriptdir}/ssh_keydb
%{py_sitescriptdir}/ssh_keydb/*.py[co]
%dir %{py_sitescriptdir}/ssh_keydb/plugins
%{py_sitescriptdir}/ssh_keydb/plugins/*.py[co]
%{py_sitescriptdir}/ssh_keydb_server-%{version}-py*.egg-info

%{py_sitescriptdir}/ssh_keydb/*.py
%{py_sitescriptdir}/ssh_keydb/plugins/*.py
