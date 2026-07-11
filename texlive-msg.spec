%global tl_name msg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.51
Release:	%{tl_revision}.1
Summary:	A package for LaTeX localisation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/msg
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is designed to localise any document class or package. This
should be very useful for end-users who could obtain messages in their
own preferred language. It is really easy to use by writers of other
classes and packages. Volunteers are urged to test the package, report,
and even to localise the message file to their own language.
Documentation is provided in English.

