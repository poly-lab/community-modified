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

