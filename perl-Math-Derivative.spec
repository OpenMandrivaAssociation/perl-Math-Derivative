%define upstream_name    Math-Derivative
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Numeric 1st and 2nd order differentiation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This Perl package exports functions for performing numerical first
(Derivative1) and second Derivative2) order differentiation on vectors of data.
They both take references to two arrays containing the x and y ordinates of the
data and return an array of the 1st or 2nd derivative at the given x ordinates.
Derivative2 may optionally be given values to use for the first dervivative at
the start and end points of the data - otherwiswe 'natural' values are used.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 403855
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-10mdv2009.0
+ Revision: 257797
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-9mdv2009.0
+ Revision: 245838
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.01-7mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-7mdv2008.0
+ Revision: 86584
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-5mdk
- Fix According to perl Policy
    - Source URL
- use mkrel

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdk 
- better url
- spec cleanup
- don't ship useless empty dirs
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-2mdk 
- rpmbuildupdate aware

* Mon Jan 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-1mdk
- first mdk release

