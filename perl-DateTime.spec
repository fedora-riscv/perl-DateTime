Name:           perl-DateTime
Epoch:          2
Version:        1.24
Release:        1%{?dist}
Summary:        Date and time object for Perl
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module::Build) >= 0.28
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime::Locale) >= 0.41
BuildRequires:  perl(DateTime::TimeZone) >= 1.74
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Validate) >= 1.03
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Optional Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
# Cwd not used
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# circular dependency - perl(DateTime::Format::Strptime) >= 1.2000
# Pod::Coverage::TrustPod not used
# Pod::Wordlist not used
BuildRequires:  perl(Storable)
# Test::Code::TidyAll 0.24 not used
# Test::CPAN::Changes not used
# Test::CPAN::Meta::JSON not used
# Test::DependentModules not used
# Test::EOL not used
# Test::NoTabs not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Test::Spelling 0.12 not used
# Test::Version not used
BuildRequires:  perl(Test::Warn)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(XSLoader)

# Avoid provides from DateTime.so
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((DateTime::Locale|DateTime::TimeZone|Params::Validate)\\)$

%description
DateTime is a class for the representation of date/time combinations.  It
represents the Gregorian calendar, extended backwards in time before its
creation (in 1582). This is sometimes known as the "proleptic Gregorian
calendar". In this calendar, the first day of the calendar (the epoch), is the
first day of year 1, which corresponds to the date which was (incorrectly)
believed to be the birth of Jesus Christ.

%prep
%setup -q -n DateTime-%{version}

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes CREDITS README.md TODO
%{perl_vendorarch}/auto/DateTime/
%{perl_vendorarch}/DateTime/
%{perl_vendorarch}/DateTime.pm
%{_mandir}/man3/DateTime.3*
%{_mandir}/man3/DateTime::Duration.3*
%{_mandir}/man3/DateTime::Infinite.3*
%{_mandir}/man3/DateTime::LeapSecond.3*

%changelog
* Tue Mar  1 2016 Paul Howarth <paul@city-fan.org> - 2:1.24-1
- Update to 1.24
  - The last release partially broke $dt->time; if you passed a value to use
    as unit separator, it was ignored (CPAN RT#112585)

* Mon Feb 29 2016 Paul Howarth <paul@city-fan.org> - 2:1.23-1
- Update to 1.23
  - Fixed several issues with the handling of non-integer values passed to
    from_epoch() (GH#11)
    - This method was simply broken for negative values, which would end up
      being incremented by a full second, so for example -0.5 became 0.5
    - The method did not accept all valid float values; specifically, it did
      not accept values in scientific notation
    - Finally, this method now rounds all non-integer values to the nearest
      millisecond, which matches the precision we can expect from Perl itself
      (53 bits) in most cases
  - Make all DateTime::Infinite objects return the system's representation of
    positive or negative infinity for any method that returns a number or
    string representation (year(), month(), ymd(), iso8601(), etc.); previously
    some of these methods could return "Nan", "-Inf--Inf--Inf", and other
    confusing outputs (CPAN RT#110341)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Paul Howarth <paul@city-fan.org> - 2:1.21-1
- Update to 1.21
  - Make all tests pass with the current DateTime::Locale
- Explicitly BR: perl-devel, needed for EXTERN.h

* Fri Jul 24 2015 Petr Pisar <ppisar@redhat.com> - 2:1.20-1
- 1.20 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.18-2
- Perl 5.22 rebuild

* Tue Jan  6 2015 Paul Howarth <paul@city-fan.org> - 2:1.18-1
- 1.18 bump

* Mon Jan  5 2015 Paul Howarth <paul@city-fan.org> - 2:1.17-1
- 1.17 bump
- Use %%license
- Make %%files list more explicit

* Mon Jan  5 2015 Paul Howarth <paul@city-fan.org> - 2:1.14-1
- 1.14 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.12-2
- Perl 5.20 rebuild

* Tue Sep 02 2014 Petr Pisar <ppisar@redhat.com> - 2:1.12-1
- 1.12 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.10-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Petr Pisar <ppisar@redhat.com> - 2:1.10-1
- 1.10 bump

* Fri Mar 14 2014 Paul Howarth <paul@city-fan.org> - 2:1.08-1
- 1.08 bump

* Mon Feb 10 2014 Paul Howarth <paul@city-fan.org> - 2:1.07-1
- 1.07 bump

* Fri Jan 03 2014 Petr Pisar <ppisar@redhat.com> - 2:1.06-1
- 1.06 bump

* Tue Dec 10 2013 Petr Pisar <ppisar@redhat.com> - 2:1.04-1
- 1.04 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 2:1.03-2
- Perl 5.18 rebuild

* Tue Jun 25 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.03-1
- 1.03 bump

* Tue Apr 02 2013 Petr Šabata <contyk@redhat.com> - 2:1.01-1
- 1.01 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Petr Pisar <ppisar@redhat.com> - 2:0.78-1
- 0.78 bump

* Thu Oct 18 2012 Petr Pisar <ppisar@redhat.com> - 2:0.77-1
- 0.77 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 2:0.70-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Iain Arnell <iarnell@gmail.com> 2:0.70-2
- Additional (Build)Requires from unofficial review

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 2:0.70-1
- Unbundle DateTime::TimeZone and DateTime::Locale
- Bump epoch and revert to upstream versioning
- Specfile regenerated by cpanspec 1.78.
- Update description

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1:0.7000-3
- Perl mass rebuild

* Mon Jul 04 2011 Iain Arnell <iarnell@gmail.com> 1:0.7000-2
- update DateTime::TimeZone to 1.35 (Olson 2011h)
- add rpm 4.9 filtering macros

* Fri May 13 2011 Iain Arnell <iarnell@gmail.com> 1:0.7000-1
- update DateTime to 0.70

* Wed May 04 2011 Iain Arnell <iarnell@gmail.com> 1:0.6900-1
- update DateTime to 0.69
- update DateTime::TimeZone to 1.34 (Olson 2011g)

* Sun Apr 24 2011 Iain Arnell <iarnell@gmail.com> 1:0.6600-6
- fix the testing for loop

* Sun Apr 24 2011 Iain Arnell <iarnell@gmail.com> 1:0.6600-5
- update DateTime::TimeZone to 1.33 (Olson 2011f)

* Wed Apr 06 2011 Iain Arnell <iarnell@gmail.com> 1:0.6600-4
- update DateTime::TimeZone to 1.32 (Olson 2011e)

* Sat Mar 26 2011 Iain Arnell <iarnell@gmail.com> 1:0.6600-3
- update DateTime::TimeZone to 1.31
- DateTime::TimeZone no longer has Build.PL; use Makefile.PL
- whitespace cleanup
- clean up .packlist

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6600-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Steven Pritchard <steve@kspei.com> 1:0.6600-1
- Update DateTime to 0.66.
- Update DateTime::TimeZone to 1.26.
- Update URL for FAQ in description.
- BR Class::Load and parent.

* Sat Oct 09 2010 Iain Arnell <iarnell@gmail.com> 1:0.6300-1
- Update DateTime to 0.63
- Update DateTime::TimeZone to 1.22
- DateTime license changed from "GPL+ or Artistic" to "Artistic 2.0"
- Fix DTLocale/Changelog encoding

* Mon Jun 14 2010 Petr Sabata <psabata@redhat.com> - 1:0.5300-4
- perl-DateTime-Locale-0.45 update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.5300-3
- Mass rebuild with perl-5.12.0

* Wed Jan 27 2010 Stepan Kasal <skasal@redhat.com> - 1:0.5300-2
- new upstream version of DateTime-TimeZone

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 1:0.5300-1
- new upstream version
- use Build.PL as Makefile.PL no longer exists
- use iconv to recode to utf-8, not a patch
- update BuildRequires
- drop Provides: perl(DateTime::TimeZoneCatalog), it is no longer there
- use filtering macros

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:0.4501-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4501-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4501-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 09 2008 Steven Pritchard <steve@kspei.com> 1:0.4501-1
- Update to DateTime 0.4501.

* Mon Nov 10 2008 Steven Pritchard <steve@kspei.com> 1:0.4401-1
- Update to DateTime 0.4401.
- Update to DateTime::Locale 0.42.
- Update to DateTime::TimeZone 0.8301.

* Mon Sep 08 2008 Steven Pritchard <steve@kspei.com> 1:0.4304-2
- Update to DateTime::TimeZone 0.7904.

* Tue Jul 15 2008 Steven Pritchard <steve@kspei.com> 1:0.4304-1
- Update to DateTime 0.4304.
- Update to DateTime::TimeZone 0.78.
- Update to DateTime::Locale 0.41.

* Tue Jul 08 2008 Steven Pritchard <steve@kspei.com> 1:0.4302-2
- Update to DateTime::TimeZone 0.7701.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 1:0.4302-1
- Update to DateTime 0.4302.
- Update to DateTime::TimeZone 0.77.
- Update to DateTime::Locale 0.4001.
- BR List::MoreUtils.
- Define IS_MAINTAINER so we run the pod tests.

* Thu May 15 2008 Steven Pritchard <steve@kspei.com> 1:0.42-1
- Update to DateTime 0.42.
- Update to DateTime::TimeZone 0.75.
- Update FAQ URL in description.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.41-5
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.41-4
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:0.41-3
- rebuild for new perl

* Tue Dec 11 2007 Steven Pritchard <steve@kspei.com> 1:0.41-2
- Update License tag.
- Update to DateTime::TimeZone 0.70.

* Mon Sep 17 2007 Steven Pritchard <steve@kspei.com> 1:0.41-1
- Update to DateTime 0.41.
- Update to DateTime::Locale 0.35.
- Update to DateTime::TimeZone 0.67.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1:0.39-2
- Rebuild for selinux ppc32 issue.

* Sun Jul 22 2007 Steven Pritchard <steve@kspei.com> 1:0.39-1
- Update to DateTime 0.39.
- Update to DateTime::TimeZone 0.6603.

* Thu Jul 05 2007 Steven Pritchard <steve@kspei.com> 1:0.38-2
- BR Test::Output.

* Mon Jul 02 2007 Steven Pritchard <steve@kspei.com> 1:0.38-1
- Update to DateTime 0.38.
- Update to DateTime::TimeZone 0.6602.
- BR Test::Pod::Coverage.

* Mon Apr 02 2007 Steven Pritchard <steve@kspei.com> 1:0.37-3
- Drop BR DateTime::Format::* to avoid circular build deps.

* Mon Apr 02 2007 Steven Pritchard <steve@kspei.com> 1:0.37-2
- Filter Win32::TieRegistry dependency.
- Do the provides filter like we do in cpanspec.
- Drop some macro usage.

* Sat Mar 31 2007 Steven Pritchard <steve@kspei.com> 1:0.37-1
- Update to DateTime 0.37.
- Update to DateTime::TimeZone 0.63.

* Tue Mar 13 2007 Steven Pritchard <steve@kspei.com> 1:0.36-2
- Update to DateTime::Locale 0.34.
- Update to DateTime::TimeZone 0.62.

* Mon Jan 22 2007 Steven Pritchard <steve@kspei.com> 1:0.36-1
- Update to Date::Time 0.36.
- Update to DateTime::Locale 0.33.
- Update to DateTime::TimeZone 0.59.

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
