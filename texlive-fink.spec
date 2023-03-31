Name:		texlive-fink
Version:	24329
Release:	2
Summary:	The LaTeX2e File Name Keeper
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fink
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fink.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
This package "looks over your shoulder" and keeps track of
files \input'ed (the LaTeX way) or \include'ed in your
document. You then have permanent access to the name of the
file currently being processed through the macro \finkfile.
FiNK also comes with support for AUC-TeX. As of version 2.2.1,
FiNK has been deprecated and is not maintained anymore. People
interested in FiNK's functionality are invited to use a package
named currfile instead.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
