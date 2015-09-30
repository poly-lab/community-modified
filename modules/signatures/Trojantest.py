__author__ = 'liebesu'
# Copyright (C) 2013 Claudio "nex" Guarnieri (@botherder)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
    import re2 as re
except ImportError:
    import re

from lib.cuckoo.common.abstracts import Signature

class NetworkHTTP(Signature):
    name = "trojantest"
    description = "trojantest"
    severity = 3
    confidence = 30
    categories = ["http"]
    authors = ["liebesu"]
    minimum = "0.5"

    filter_analysistypes = set(["file"])

    def run(self):
        balcklist = [
            "217.23.8.164:*",
            ]

        if "network" in self.results:
            if "http" in self.results["network"]:
                for req in self.results["network"]["http"]:
                    is_whitelisted = False
                    for white in balcklist:
                        if re.match(white, req["uri"], re.IGNORECASE):
                            is_balcklisted = True
                    if not is_whitelisted:
                        return True

        return False
