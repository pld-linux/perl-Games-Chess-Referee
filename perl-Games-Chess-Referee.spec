#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Chess-Referee
Summary:	Games::Chess::Referee - work with chess positions and games
Summary(pl):	Games::Chess::Referee - operacje na pozycjach i partiach szachowych
Name:		perl-Games-Chess-Referee
Version:	0.002
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6fda8f33fee2cdceffb26d72508d5ffa
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Games-Chess
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Games-Chess >= 0.002-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::Chess::Referee module provides a mechanism to interpret
(almost) standard algebraic chess notation and to print out the
resulting positions. It makes use of the Games::Chess::Position and
Games::Chess::Piece classes by Gareth Rees, adding the chess rules and
more application functionality.

%description -l pl
Modu³ Games::Chess::Referee udostêpnia mechanizm interpretacji
(prawie) standardowej algebraicznej notacji szachowej i wy¶wietlania
wyj¶ciowych pozycji. Wykorzystuje klasy autorstwa Garetha Ressa
Games::Chess::Position i Games::Chess::Piece, dodaj±c regu³y szachowe
i zwiêkszaj±c funkcjonalno¶æ aplikacji.

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
%doc README tryme
%dir %{perl_vendorlib}/Games/Chess
%{perl_vendorlib}/Games/Chess/Referee.pm
%{_mandir}/man3/*
