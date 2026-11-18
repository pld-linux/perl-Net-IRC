%define		pdir	Net
%define		pnam	IRC
Summary:	Net::IRC perl module
Summary(pl.UTF-8):	Moduł Perla Net::IRC
Name:		perl-Net-IRC
Version:	0.79
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5849c6e482ade4367d783e04a4530ee6
Patch0:		%{name}-no-prompt.patch
URL:		http://search.cpan.org/dist/Net-IRC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IRC - Perl interface to IRC.

%description -l pl.UTF-8
Net::IRC - interfejs Perla do IRC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

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
%doc Changes README
%{perl_vendorlib}/Net/IRC.pm
%{perl_vendorlib}/Net/IRC
%{_mandir}/man3/*
