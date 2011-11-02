Name:		texlive-l2tabu
Version:	2.3
Release:	1
Summary:	Obsolete packages and commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/german
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The "sins" of LaTeX users, and how to correct them. The
document provides a list of obsolete packages and commands
(this original is in German; it has been translated into
English, French, Italian and Spanish).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu/CHANGES
%doc %{_texmfdistdir}/doc/latex/l2tabu/README
%doc %{_texmfdistdir}/doc/latex/l2tabu/l2tabu.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu/l2tabu.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
