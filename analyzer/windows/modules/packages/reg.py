# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from __future__ import absolute_import

from lib.common.abstracts import Package


class Reg(Package):
    """Reg analysis package."""

    PATHS = [
        ("SystemRoot", "System32", "reg.exe"),
    ]

    def start(self, path):
        regexe = self.get_path("reg.exe")
        reg_args = 'import "{0}"'.format(path)
        return self.execute(regexe, reg_args, path)
