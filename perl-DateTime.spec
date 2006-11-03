%define DTTimeZone_version 0.54
%define DTLocale_version 0.3101

Name:           perl-DateTime
Version:        0.35
Release:        1%{?dist}
Epoch:          1
Summary:        Date and time objects
License:        GPL or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz
Source1:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{DTTimeZone_version}.tar.gz
Source2:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{DTLocale_version}.tar.gz
Patch0:         DateTime-LeapSecond-utf8.patch
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
DateTime is a class for the representation of date/time combinations, and
is part of the Perl DateTime project. For details on this project please
see http://datetime.perl.org/. The DateTime site has a FAQ which may help
answer many "how do I do X?" questions. The FAQ is at
http://datetime.perl.org/faq.html.

%prep
%setup -q -T -c -n DateTimeBundle -a 0
%setup -q -T -D -n DateTimeBundle -a 1
%setup -q -T -D -n DateTimeBundle -a 2

cd DateTime-%{version}
%patch0 -p1
cd -

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
find %{buildroot} -depth  -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

# Move documentation into bundle area
mkdir DT::Locale DT::TimeZone
mv DateTime-%{version}/{CREDITS,Changes,LICENSE,README,TODO} .
mv DateTime-Locale-%{DTLocale_version}/{Changes,LICENSE.cldr} DT::Locale
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
* Fri Nov 03 2006 Steven Pritchard <steve@kspei.com> 1:0.35-1
- Update to DateTime 0.35.
- Update to DateTime::Locale 0.3101.
- LICENSE.icu seems to have been renamed LICENSE.cldr.
- Update to DateTime::TimeZone 0.54.
- Use fixperms macro instead of our own chmod incantation.
- Convert DateTime::LeapSecond to UTF-8 to avoid a rpmlint warning.

* Tue Aug 29 2006 Steven Pritchard <steve@kspei.com> 1:0.34-3
- Update to DateTime::TimeZone 0.48.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 1:0.34-2
- Update to DateTime::TimeZone 0.47.

* Mon Aug 14 2006 Steven Pritchard <steve@kspei.com> 1:0.34-1
- Update to DateTime 0.34.

* Fri Jul 28 2006 Steven Pritchard <steve@kspei.com> 1:0.32-1
- Update to DateTime 0.32.
- Improve Summary, description, and source URLs.
- Fix find option order.

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
