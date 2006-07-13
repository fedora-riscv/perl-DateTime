%define DTTimeZone_version 0.46
%define DTLocale_version 0.22

Name:           perl-DateTime
Version:        0.31
Release:        2%{?dist}
Epoch:          1
Summary:        DateTime Perl module
License:        GPL or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime/
Source0:        http://www.cpan.org/modules/by-module/DateTime/DateTime-%{version}.tar.gz
Source1:        http://www.cpan.org/modules/by-module/DateTime/DateTime-TimeZone-%{DTTimeZone_version}.tar.gz
Source2:        http://www.cpan.org/modules/by-module/DateTime/DateTime-Locale-%{DTLocale_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate) >= 0.76
BuildRequires:  perl(Class::Singleton) >= 1.03
BuildRequires:  perl(Pod::Man) >= 1.14
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(DateTime::Format::ICal)
BuildRequires:  perl(DateTime::Format::Strptime)
Requires:       perl(Params::Validate) >= 0.76
Requires:       perl(Class::Singleton) >= 1.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl-DateTime-TimeZone = %{DTTimeZone_version}
Provides:       perl-DateTime-Locale = %{DTLocale_version}
Provides:       perl(DateTime::TimeZoneCatalog)
Provides:       perl(DateTimePP)
Provides:       perl(DateTimePPExtra)

%description
The DateTime.pm module aims to provide a complete, correct, and easy to use
date/time object implementation. Currently it handles many date
calculations, date math (addition and subtraction), and provides convenient
methods for retrieving portions of a date/time.

%prep
%setup -q -T -c -n DateTimeBundle -a 0
%setup -q -T -D -n DateTimeBundle -a 1
%setup -q -T -D -n DateTimeBundle -a 2

cat > filter-provides.sh << EOF
#!/bin/sh
# Remove redundant unversioned provides of perl(DateTime) and perl(DateTime::TimeZone)
exec %{__perl_provides} $* | egrep -v '^perl[(]DateTime(::TimeZone)?[)]$'
EOF
%define __perl_provides %{_builddir}/DateTimeBundle/filter-provides.sh
chmod 755 filter-provides.sh

%build
cd DateTime-Locale-%{DTLocale_version}
%{__perl} Build.PL installdirs=vendor
./Build
cd -

cd DateTime-TimeZone-%{DTTimeZone_version}
%{__perl} Build.PL installdirs=vendor
./Build
cd -

cd DateTime-%{version}
PERLLIB=../DateTime-Locale-%{DTLocale_version}/blib/lib
PERLLIB=$PERLLIB:../DateTime-TimeZone-%{DTTimeZone_version}/blib/lib
export PERLLIB
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
cd -

%install
rm -rf %{buildroot}

cd DateTime-Locale-%{DTLocale_version}
./Build install destdir=%{buildroot}
cd -

cd DateTime-TimeZone-%{DTTimeZone_version}
./Build install destdir=%{buildroot}
cd -

cd DateTime-%{version}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
cd -

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w %{buildroot}/*

# Move documentation into bundle area
mkdir DT::Locale DT::TimeZone
mv DateTime-%{version}/{CREDITS,Changes,LICENSE,README,TODO} .
mv DateTime-Locale-%{DTLocale_version}/{Changes,LICENSE.icu} DT::Locale
mv DateTime-TimeZone-%{DTTimeZone_version}/{Changes,README} DT::TimeZone

%check
# Have to use PERL5LIB rather than PERLLIB here because the test scripts
# clobber PERLLIB
PERL5LIB=$(pwd)/DateTime-%{version}/blib/arch:$(pwd)/DateTime-%{version}/blib/lib
PERL5LIB=$PERL5LIB:$(pwd)/DateTime-Locale-%{DTLocale_version}/blib/lib
PERL5LIB=$PERL5LIB:$(pwd)/DateTime-TimeZone-%{DTTimeZone_version}/blib/lib
export PERL5LIB

cd DateTime-Locale-%{DTLocale_version}
./Build test
cd -

cd DateTime-TimeZone-%{DTTimeZone_version}
./Build test
cd -

make -C DateTime-%{version} test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CREDITS Changes LICENSE README TODO DT::Locale DT::TimeZone
%{_mandir}/man3/*
# DateTime::TimeZone and DateTime::Locale modules are arch-independent
%{perl_vendorlib}/DateTime/
# DateTime module is arch-specific
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DateTime/
%{perl_vendorarch}/DateTime*.pm

%changelog
* Thu Jul 13 2006 Steven Pritchard <steve@kspei.com> 1:0.31-2
- BR DateTime::Format::ICal and DateTime::Format::Strptime for better
  test coverage.

* Wed May 24 2006 Steven Pritchard <steve@kspei.com> 1:0.31-1
- Update DateTime to 0.31.
- Update DateTime::TimeZone to 0.46.

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 1:0.30-3
- Bump Epoch (argh, 0.2901 > 0.30 to rpm)
- Update DateTime::TimeZone to 0.42

* Sat Feb 18 2006 Steven Pritchard <steve@kspei.com> 0.30-2
- Update DateTime::TimeZone to 0.41

* Tue Jan 10 2006 Steven Pritchard <steve@kspei.com> 0.30-1
- Update DateTime to 0.30
- Update DateTime::TimeZone to 0.40

* Fri Sep 16 2005 Paul Howarth <paul@city-fan.org> 0.2901-2
- Unpack each tarball only once
- Use Module::Build's build script where available
- Help each module find the others when needed
- Clean up files list
- Include additional documentation from DT::Locale & DT::TimeZone
- Add BR: perl(File::Find::Rule) & perl(Test::Pod) to improve test coverage
- Remove unversioned provides of perl(DateTime) & perl(DateTime::TimeZone)

* Wed Aug 31 2005 Steven Pritchard <steve@kspei.com> 0.2901-1
- Specfile autogenerated.
