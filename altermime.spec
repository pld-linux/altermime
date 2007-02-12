Summary:	alterMIME - a small program which is used to alter MIME-encoded mailpacks
Summary(pl.UTF-8):	alterMIME - mały program do modyfikowania przesyłek kodowanych MIME
Name:		altermime
Version:	0.3.7
Release:	1
License:	BSD
Group:		Networking/Utilities
# 403
#Source0:	http://pldaniels.com/altermime/%{name}-%{version}.tar.gz
Source0:	http://sce-tindy.tecnik93.com/FreeBSD/ports/altermime/sources/%{name}-%{version}.tar.gz
# Source0-md5:	534a68f9fed6867511c50e1e7bdf7722
URL:		http://www.pldaniels.com/altermime/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
alterMIME is a small program which is used to alter your MIME-encoded
mailpacks as typically received by Inflex, Xamime and AMaViS.

What can alterMIME do?
- Insert disclaimers
- Insert arbitary X-headers
- Modify existing headers
- Remove attachments based on filename or content-type
- Replace attachments based on filename

%description -l pl.UTF-8
alterMIME to mały program służący do modyfikowania przesyłek
kodowanych MIME, takich jak zwykle odbierane przez Infleksa, Xamime
czy AMaViSa.

alterMIME potrafi:
- wstawiać oświadczenia
- wstawiać dowolne X-nagłówki
- modyfikować istniejące nagłówki
- usuwać załączniki na podstawie nazwy pliku lub typu (content-type)
- zastępować załączniki na podstawie nazwy pliku

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install altermime	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README LICENCE
%attr(755,root,root) %{_bindir}/*
