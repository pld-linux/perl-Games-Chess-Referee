%define	pdir	Games
%define	pnam	Chess-Referee
%include	/usr/lib/rpm/macros.perl
Summary:	Games-Chess-Referee perl module
Summary(pl):	Modu³ perla Games-Chess-Referee
Name:		perl-Games-Chess-Referee
Version:	0.002
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Games-Chess
Requires:	perl-Games-Chess >= 0.002-3
BuildArch:	noarch
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
