%global tl_name l2tabu
%global tl_revision 63708

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Obsolete packages and commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/l2tabu/german
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The "sins" of LaTeX users, and how to correct them. The document
provides a list of obsolete packages and commands. This original is in
German; it has been translated into English, French, Italian, and
Spanish.

