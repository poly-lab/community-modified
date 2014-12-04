# Copyright (C) 2014 Accuvant, Inc. (bspengler@accuvant.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class PreventsSafeboot(Signature):
    name = "prevents_safeboot"
    description = "Attempts to block SafeBoot use by removing registry keys"
    severity = 3
    categories = ["generic"]
    authors = ["Accuvant"]
    minimum = "1.2"

    def run(self):
        if self.check_write_key(pattern=".*\\\\System\\\\(CurrentControlSet|ControlSet001)\\\\Control\\\\SafeBoot\\\\.*", regex=True):
            return True
        return False
