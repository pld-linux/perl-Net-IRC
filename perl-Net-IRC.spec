%include	/usr/lib/rpm/macros.perl
Summary:	Net-IRC perl module
Summary(pl):	Modu³ perla Net-IRC
Name:		perl-Net-IRC
Version:	0.63
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-IRC-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-IRC - Perl interface to IRC.

%description -l pl
Net-IRC - interfejs perla do IRC.

%prep
%setup -q -n Net-IRC-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/IRC
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz irctest

%{perl_sitelib}/Net/IRC.pm
%{perl_sitelib}/Net/IRC
%{perl_sitearch}/auto/Net/IRC

%{_mandir}/man3/*
