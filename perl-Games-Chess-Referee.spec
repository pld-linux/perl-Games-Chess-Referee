%include	/usr/lib/rpm/macros.perl
Summary:	Games-Chess-Referee perl module
Summary(pl):	Modu³ perla Games-Chess-Referee
Name:		perl-Games-Chess-Referee
Version:	0.002
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Games/Games-Chess-Referee-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Games-Chess
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Games-Chess >= 0.002-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games-Chess-Referee module provides a mechanism to interpret (almost)
standard algebraic chess notation and to print out the resulting
positions. It makes use of the Games::Chess::Position and
Games::Chess::Piece classes by Gareth Rees, adding the chess rules and
more application functionality.

%description -l pl
Modu³ Games-Chess-Referee udostepnia mechanizm interpretacji (prawie)
standardowej algebraicznej notacji szachowej i wy¶wietlania
wyj¶ciowych pozycji. Wykorzystuje klasy autorstwa Garetha Ressa
Games::Chess::Position i Games::Chess::Piece, dodaj±c regu³y szachowe
i zwiêkszaj±c funkcjonalno¶æ aplikacji.

%prep
%setup -q -n Games-Chess-Referee-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tryme
%{perl_sitelib}/Games/Chess/Referee.pm
%{_mandir}/man3/*
