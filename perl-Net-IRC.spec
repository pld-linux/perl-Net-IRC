%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IRC
Summary:	Net::IRC perl module
Summary(pl):	Modu³ perla Net::IRC
Name:		perl-Net-IRC
Version:	0.73
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitelib}/Net/IRC.pm
%{perl_sitelib}/Net/IRC
%{_mandir}/man3/*
