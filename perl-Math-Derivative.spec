%define upstream_name    Math-Derivative
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Numeric 1st and 2nd order differentiation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*
