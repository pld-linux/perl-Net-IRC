%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IRC
Summary:	Net::IRC perl module
Summary(pl):	Modu³ Perla Net::IRC
Name:		perl-Net-IRC
Version:	0.75
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	57587a48ddece7a995c6b138003ee798
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IRC - Perl interface to IRC.

%description -l pl
Net::IRC - interfejs Perla do IRC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Net/IRC.pm
%{perl_vendorlib}/Net/IRC
%{_mandir}/man3/*
