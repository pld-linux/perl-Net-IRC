%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IRC
Summary:	Net::IRC perl module
Summary(pl):	Modu³ perla Net::IRC
Name:		perl-Net-IRC
Version:	0.73
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IRC - Perl interface to IRC.

%description -l pl
Net::IRC - interfejs perla do IRC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz irctest
%{perl_sitelib}/Net/IRC.pm
%{perl_sitelib}/Net/IRC
%{_mandir}/man3/*
