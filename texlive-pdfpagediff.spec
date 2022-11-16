Name:		texlive-pdfpagediff
Version:	37946
Release:	1
Summary:	Find difference between two PDF's
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpagediff
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpagediff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpagediff.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Find difference between two PDF's

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pdfpagediff
%doc %{_texmfdistdir}/doc/latex/pdfpagediff

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
