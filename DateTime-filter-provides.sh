#!/bin/sh
#
# Remove redundant unversioned provides of
# perl(DateTime) and perl(DateTime::TimeZone).

@@PERL_PROV@@ "$@" | sed -e '/^perl(DateTime\(::TimeZone\)\?)$/d'
