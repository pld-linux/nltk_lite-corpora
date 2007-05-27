Summary:	Natural Language Toolkit Database
Summary(pl.UTF-8):	Baza danych dla pakietu Natural Language Toolkit
Name:		nltk_lite-corpora
Version:	0.7.5
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/nltk/%{name}-%{version}.zip
# Source0-md5:	9bc74c1b4c1fe5f0254eb9cd10e68d0f
URL:		http://nltk.sourceforge.net/
BuildRequires:	unzip
Requires:	python-nltk_lite
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Langauge Toolkit (NLTK-Lite) database.

%description -l pl.UTF-8
Baza danych dla pakietu Natural Language Toolkit (NLTK-Lite).

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/nltk_lite

cp -a * $RPM_BUILD_ROOT%{_datadir}/nltk_lite

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/nltk_lite
