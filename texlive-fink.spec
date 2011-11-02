Name:		texlive-fink
Version:	2.2.1
Release:	1
Summary:	The LaTeX2e File Name Keeper
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fink
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package "looks over your shoulder" and keeps track of
files \input'ed (the LaTeX way) or \include'ed in your
document. You then have permanent access to the name of the
file currently being processed through the macro \finkfile.
FiNK also comes with support for AUC-TeX. As of version 2.2.1,
FiNK has been deprecated and is not maintained anymore. People
interested in FiNK's functionality are invited to use a package
named currfile instead.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fink/fink.sty
%doc %{_texmfdistdir}/doc/latex/fink/NEWS
%doc %{_texmfdistdir}/doc/latex/fink/README
%doc %{_texmfdistdir}/doc/latex/fink/THANKS
%doc %{_texmfdistdir}/doc/latex/fink/fink.el
%doc %{_texmfdistdir}/doc/latex/fink/fink.pdf
%doc %{_texmfdistdir}/doc/latex/fink/header.inc
#- source
%doc %{_texmfdistdir}/source/latex/fink/fink.dtx
%doc %{_texmfdistdir}/source/latex/fink/fink.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}