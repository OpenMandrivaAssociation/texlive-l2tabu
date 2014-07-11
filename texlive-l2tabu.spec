# revision 24038
# category Package
# catalog-ctan /info/l2tabu/german
# catalog-date 2011-09-21 00:38:26 +0200
# catalog-license gpl
# catalog-version 2.3
Name:		texlive-l2tabu
Version:	2.3
Release:	8
Summary:	Obsolete packages and commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/german
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3-2
+ Revision: 753062
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3-1
+ Revision: 718790
- texlive-l2tabu
- texlive-l2tabu
- texlive-l2tabu
- texlive-l2tabu

