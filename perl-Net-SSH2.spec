%define upstream_name	 Net-SSH2
%define upstream_version 0.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Support for the SSH 2 protocol via libSSH2
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	libssh2-devel
BuildRequires:	perl(Term::ReadKey)
Buildrequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org) library.
It supports the SSH2 protocol (there is no support for SSH1) with all of the
key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
