%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Chess-Referee
Summary:	Games::Chess::Referee Perl module
Summary(cs):	Modul Games::Chess::Referee pro Perl
Summary(da):	Perlmodul Games::Chess::Referee
Summary(de):	Games::Chess::Referee Perl Modul
Summary(es):	Módulo de Perl Games::Chess::Referee
Summary(fr):	Module Perl Games::Chess::Referee
Summary(it):	Modulo di Perl Games::Chess::Referee
Summary(ja):	Games::Chess::Referee Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Games::Chess::Referee ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Games::Chess::Referee
Summary(pl):	Modu³ Perla Games::Chess::Referee
Summary(pt):	Módulo de Perl Games::Chess::Referee
Summary(pt_BR):	Módulo Perl Games::Chess::Referee
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Games::Chess::Referee
Summary(sv):	Games::Chess::Referee Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Games::Chess::Referee
Summary(zh_CN):	Games::Chess::Referee Perl Ä£¿é
Name:		perl-Games-Chess-Referee
Version:	0.002
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Games-Chess
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README tryme
%dir %{perl_sitelib}/Games/Chess
%{perl_sitelib}/Games/Chess/Referee.pm
%{_mandir}/man3/*
