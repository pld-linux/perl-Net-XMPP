#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	XMPP
Summary:	Net::XMPP - XMPP Perl library
Summary(pl):	Net::XMPP - biblioteka Perla XMPP
Name:		perl-Net-XMPP
Version:	1.0
Release:	1
# and somewhere mentioned as "perl itself"
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6338484aa0d394e68c01666ca34e5241
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Stream >= 1.22
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::XMPP is a convenient tool to use for any perl script that would
like to utilize the XMPP Instant Messaging protocol. While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible
and easy to use. Net::XMPP is a wrapper around the rest of the
official Net::XMPP::xxxxxx packages.

#%%description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Net/XMPP.pm
%{perl_vendorlib}/Net/XMPP
%{_mandir}/man3/*
