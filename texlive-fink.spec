%global tl_name fink
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.1
Release:	%{tl_revision}.1
Summary:	The LaTeX2e File Name Keeper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fink
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package "looks over your shoulder" and keeps track of files
\input'ed (the LaTeX way) or \include'ed in your document. You then have
permanent access to the name of the file currently being processed
through the macro \finkfile. FiNK also comes with support for AUC-TeX.
As of version 2.2.1, FiNK has been deprecated and is not maintained
anymore. People interested in FiNK's functionality are invited to use a
package named currfile instead.

