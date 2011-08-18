Name:           perl-DateTime
Epoch:          2
Version:        0.70
Release:        2%{?dist}
Summary:        Date and time object
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz
# circular dependency - only used for one test
#BuildRequires:  perl(DateTime::Format::Strptime) >= 1.2000
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime::Locale) >= 0.41
BuildRequires:  perl(DateTime::TimeZone) >= 1.09
BuildRequires:  perl(Math::Round)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate) >= 0.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Local) >= 1.04
BuildRequires:  perl(XSLoader)
Requires:       perl(DateTime::Locale) >= 0.41
Requires:       perl(DateTime::TimeZone) >= 1.09
Requires:       perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# not automatically detected
Provides:       perl(DateTimePP) = %{version}
Provides:       perl(DateTimePPExtra) = %{version}

%{?perl_default_filter}

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
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
RELEASE_TESTING=1 ./Build test

%files
%doc Changes CREDITS LICENSE README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DateTime*
%{_mandir}/man3/*

%changelog
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
