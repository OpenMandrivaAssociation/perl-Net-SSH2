%define upstream_name	 Net-SSH2
%define upstream_version 0.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Support for the SSH 2 protocol via libSSH2
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig(libssh2)
BuildRequires:	perl(Term::ReadKey)
Buildrequires:	perl-devel

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.390.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.390.0-1
+ Revision: 690299
- update to new version 0.39

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-1
+ Revision: 684780
- update to new version 0.38

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.360.0-1
+ Revision: 682138
- update to new version 0.36

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1
+ Revision: 673818
- update to new version 0.35

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.340.0-1
+ Revision: 672856
- update to new version 0.34

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-2mdv2011.0
+ Revision: 556064
- rebuild for perl 5.12

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2011.0
+ Revision: 553133
- update to 0.33

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 552475
- update to 0.31

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.1
+ Revision: 536207
- update to 0.29

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 0.280.0-2mdv2010.1
+ Revision: 534504
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.1
+ Revision: 460766
- update to 0.28

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.0
+ Revision: 437169
- update to 0.27

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 432825
- update to 0.25

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-2mdv2010.0
+ Revision: 420432
- force submit
- update to 0.24

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 418123
- update to 0.23

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-2mdv2010.0
+ Revision: 417002
- force rebuild
- update to 0.22

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 407867
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2010.0
+ Revision: 383532
- update to new version 0.21

* Fri Jun 05 2009 Olivier Thauvin <nanardon@mandriva.org> 0.20-1mdv2010.0
+ Revision: 383074
- 0.20

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2010.0
+ Revision: 370138
- update to new version 0.19

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.18-5mdv2009.0
+ Revision: 258133
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.18-4mdv2009.0
+ Revision: 246174
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - buildrequire libssh2-devel specifically

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2008.1
+ Revision: 152228
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 109590
- new version

* Tue Aug 28 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdv2008.0
+ Revision: 72862
- fix build


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.10-1mdv2007.0
+ Revision: 131671
- 0.10

* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 0.09-1mdv2007.1
+ Revision: 95157
- 0.09

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.08-2mdv2007.0
+ Revision: 53855
- rebuild
- Import perl-Net-SSH2

* Thu Jun 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2007.0
- New release 0.08
- fix compilation flags

* Sat Apr 29 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.07-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Tue Mar 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdk
- New release 0.07

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- fix buildrequires

* Wed Dec 21 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.05-2mdk
- Add BuildRequires: perl-Term-ReadKey

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 0.05-1mdk
- 0.05

* Fri Nov 18 2005 Olivier Thauvin <nanardon@mandriva.org> 0.04-1mdk
- initial contrib

