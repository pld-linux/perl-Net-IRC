%include	/usr/lib/rpm/macros.perl
Summary:	Net-IRC perl module
Summary(pl):	Modu³ perla Net-IRC
Name:		perl-Net-IRC
Version:	0.70
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-IRC-%{version}.tar.gz
Patch0:		%{name}-ipv6.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-IRC - Perl interface to IRC.

%description -l pl
Net-IRC - interfejs perla do IRC.

%prep
%setup -q -n Net-IRC-%{version}
%patch0 -p1

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
