#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Chess-Referee
Summary:	Games::Chess::Referee - work with chess positions and games
Summary(pl.UTF-8):	Games::Chess::Referee - operacje na pozycjach i partiach szachowych
Name:		perl-Games-Chess-Referee
Version:	0.003
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d7d6d20e33c8ba4be51550a64d5ac6ae
BuildRequires:	perl-Games-Chess
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Games-Chess >= 0.002-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(Games::Chess::Piece)

%description
Games::Chess::Referee module provides a mechanism to interpret
(almost) standard algebraic chess notation and to print out the
resulting positions. It makes use of the Games::Chess::Position and
Games::Chess::Piece classes by Gareth Rees, adding the chess rules and
more application functionality.

%description -l pl.UTF-8
Moduł Games::Chess::Referee udostępnia mechanizm interpretacji
(prawie) standardowej algebraicznej notacji szachowej i wyświetlania
wyjściowych pozycji. Wykorzystuje klasy autorstwa Garetha Ressa
Games::Chess::Position i Games::Chess::Piece, dodając reguły szachowe
i zwiększając funkcjonalność aplikacji.

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
%doc README
%attr(755,root,root) %{_bindir}/mkbd
%attr(755,root,root) %{_bindir}/tryme
%dir %{perl_vendorlib}/Games/Chess
%{perl_vendorlib}/Games/Chess/Referee.pm
%{perl_vendorlib}/Games/Chess/Rules.pm
%dir %{perl_vendorlib}/Games/Chess/Piece
%{perl_vendorlib}/Games/Chess/Piece/General.pm
%{perl_vendorlib}/Games/Chess/Piece/Pawn.pm
%{_mandir}/man3/*
