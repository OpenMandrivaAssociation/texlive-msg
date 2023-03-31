Name:		texlive-msg
Version:	49578
Release:	2
Summary:	A package for LaTeX localisation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/msg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed to localise any document class or
package. This should be very useful for end-users who could
obtain messages in their own preferred language. It is really
easy to use by writers of other classes and packages.
Volunteers are urged to test the package, report, and even to
localise the message file to their own language. Documentation
is provided in English.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/msg/french_msg-msg.tex
%{_texmfdistdir}/tex/latex/msg/german_msg-msg.tex
%{_texmfdistdir}/tex/latex/msg/msg-msg.tex
%{_texmfdistdir}/tex/latex/msg/msg.sty
%{_texmfdistdir}/tex/latex/msg/norsk_msg-msg.tex
%doc %{_texmfdistdir}/doc/latex/msg/CHANGES
%doc %{_texmfdistdir}/doc/latex/msg/README
%doc %{_texmfdistdir}/doc/latex/msg/README_msg_doc.txt
%doc %{_texmfdistdir}/doc/latex/msg/msg.pdf
%doc %{_texmfdistdir}/doc/latex/msg/msgguide.pdf
%doc %{_texmfdistdir}/doc/latex/msg/msgguide.tex
%doc %{_texmfdistdir}/doc/latex/msg/msgtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/msg/Makefile
%doc %{_texmfdistdir}/source/latex/msg/msg.dtx
%doc %{_texmfdistdir}/source/latex/msg/msg.ins
%doc %{_texmfdistdir}/source/latex/msg/msgfiles.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
