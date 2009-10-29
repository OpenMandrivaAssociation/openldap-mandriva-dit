# PLEASE NOTE THAT THIS PACKAGE IS STORED IN SVN
# DON'T UPLOAD IT WITHOUT FIRST COMMITING CHANGES TO SVN

Name: openldap-mandriva-dit
Summary: Sample DIT for OpenLDAP
Version: 0.18
Release: %mkrel 1
License: GPL
Group: System/Servers
# Source at http://svn.mandriva.com/cgi-bin/viewvc.cgi/mdv/corporate/cs4/devel/openldap-mandriva-dit/current/
Source0: mandriva-dit-base-template.ldif
Source1: mandriva-dit-access-template.conf
Source2: mandriva-dit-setup.sh
Source3: mandriva-dit-slapd-template.conf
Source4: README.mandriva.dit
Source5: LICENSE.mandriva.dit
Source6: README.dns.mandriva.dit
Source7: README.dhcp.mandriva.dit
Source8: README.sudo.mandriva.dit
Source9: README.samba.mandriva.dit
Source10: TODO.mandriva.dit
Source14: README.heimdal.mandriva.dit
Requires: openldap-servers >= 2.3
Requires: openldap-clients
# For when we have the schemas splitted off of openldap-servers
#Requires: openldap-extra-schemas
URL: http://qa.mandriva.com/twiki/bin/view/Main/OpenldapDit
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a template LDIF file, access control rules and a simple
installation script for a suggested DIT (Directory Information Tree) to use
with an OpenLDAP server. The main characteristic of this DIT is a granular
access control via several standard administration groups. Please see the
README file for more information.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/openldap/mandriva-dit
mkdir -p %{buildroot}%{_datadir}/openldap/scripts
mkdir -p %{buildroot}%{_sysconfdir}/openldap
install -m 0644 %{_sourcedir}/mandriva-dit-base-template.ldif %{buildroot}%{_datadir}/openldap/mandriva-dit
install -m 0644 %{_sourcedir}/mandriva-dit-access-template.conf %{buildroot}%{_datadir}/openldap/mandriva-dit
install -m 0644 %{_sourcedir}/mandriva-dit-slapd-template.conf %{buildroot}%{_datadir}/openldap/mandriva-dit
install -m 0755 %{_sourcedir}/mandriva-dit-setup.sh %{buildroot}%{_datadir}/openldap/scripts
install -m 0644 %{_sourcedir}/README.mandriva.dit README
install -m 0644 %{_sourcedir}/LICENSE.mandriva.dit LICENSE
install -m 0644 %{_sourcedir}/README.dns.mandriva.dit README.dns
install -m 0644 %{_sourcedir}/README.samba.mandriva.dit README.samba
install -m 0644 %{_sourcedir}/README.dhcp.mandriva.dit README.dhcp
install -m 0644 %{_sourcedir}/README.sudo.mandriva.dit README.sudo
install -m 0644 %{_sourcedir}/README.heimdal.mandriva.dit README.heimdal
install -m 0644 %{_sourcedir}/TODO.mandriva.dit TODO

# http://qa.mandriva.com/show_bug.cgi?id=23381
sed -i "s,@LIBDIR@,%{_libdir},g" \
	%{buildroot}%{_datadir}/openldap/mandriva-dit/mandriva-dit-slapd-template.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* LICENSE TODO
%{_datadir}/openldap/scripts/mandriva-dit-setup.sh
%{_datadir}/openldap/mandriva-dit

