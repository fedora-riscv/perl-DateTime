#!/bin/sh

@@PERL_REQ@@ "$@" | sed -e '/^perl(Win32::.*$/d'
