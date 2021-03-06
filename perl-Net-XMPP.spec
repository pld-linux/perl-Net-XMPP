#
# Conditional build:
%bcond_with	tests	# perform "make test", tests require network connectivity
#
%define		pdir	Net
%define		pnam	XMPP
Summary:	Net::XMPP - XMPP Perl library
Summary(pl.UTF-8):	Net::XMPP - biblioteka Perla XMPP
Name:		perl-Net-XMPP
Version:	1.05
Release:	1
# and somewhere mentioned as "perl itself"
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6fdfeecde1b7eea1a24413e6557a97e2
URL:		http://search.cpan.org/dist/Net-XMPP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-LWP-Online
BuildRequires:	perl-XML-Stream >= 1.22
BuildRequires:	perl-YAML-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::XMPP is a convenient tool to use for any Perl script that would
like to utilize the XMPP Instant Messaging protocol. While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible
and easy to use. Net::XMPP is a wrapper around the rest of the
official Net::XMPP::xxxxxx packages.

%description -l pl.UTF-8
Net::XMPP to wygodne narzędzie do używania w dowolnym skrypcie
perlowym mającym używać protokołu XMPP Instant Messaging. O ile
biblioteka ta nie jest klientem samym w sobie, dostarcza wszystkich
funkcji backendu potrzebnych do zrobienia klienta CGI lub działającego
z linii poleceń. Net::XMPP to wrapper dla reszty oficjalnych pakietów
Net::XMPP::xxxxxx.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# avoid online tests
mv t/2_client_jabberd1.4.t t/2_client_jabberd1.4.t_
mv t/3_client_jabberd2.t t/3_client_jabberd2.t_

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
