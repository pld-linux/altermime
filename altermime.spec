Summary:	alterMIME is a small program which is used to alter mime-encoded mailpacks
Name:		altermime
Version:	0.3.6
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://pldaniels.com/altermime/%{name}-%{version}.tar.gz
# Source0-md5:	a9dc3962b00e4a6d6f3b93f10858bd35
URL:		http://www.pldaniels.com/altermime/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
alterMIME is a small program which is used to alter your mime-encoded
mailpacks as typically received by Inflex, Xamime and AMaViS.

What can alterMIME do?
- Insert disclaimers
- Insert arbitary X-headers
- Modify existing headers
- Remove attachments based on filename or content-type
- Replace attachments based on filename

%prep
%setup  -q

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
