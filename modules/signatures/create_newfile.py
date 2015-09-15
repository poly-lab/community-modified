__author__ = 'liebesu'
from lib.cuckoo.common.abstracts import Signature
class Cmd(Signature):
    name = "create"
    description = "create link "
    severity = 2
    confidence = 50
    categories = ["create link"]
    authors = ["liebesu"]
    minimum = "1.2"
    def run(self):
        file_indicators=["\\\*.link"]
        found = True
     for indicator in file_indicators:
            file_match = self.check_file(pattern=indicator, regex=True, all=True)
            if file_match:
                for match in file_match:
                    self.data.append({"file" : match })
                found = True
        return found


