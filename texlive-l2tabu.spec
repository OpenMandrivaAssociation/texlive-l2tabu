Name:		texlive-l2tabu
Version:	63708
Release:	2
Summary:	Obsolete packages and commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/german
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
