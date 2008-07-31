%define module	Net-SSH2
%define name	perl-%{module}
%define version	0.18
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Support for the SSH 2 protocol via libSSH2
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	libssh2-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org) library.
It supports the SSH2 protocol (there is no support for SSH1) with all of the
key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n %{module}-%{version}

perl -pi -e 's~^my \$inc.*~my \$inc = "%_includedir";~' Makefile.PL
perl -pi -e 's~^my \$lib.*~my \$lib = "%_libdir";~' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"


%check
%{__make} test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/*/*
