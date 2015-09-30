__author__ = 'liebesu'
from lib.cuckoo.common.abstracts import Signature
class Liebesu_Setch(Signature):
       name = "sethc back door"
    description = "has used cmd instead sethc"
    confidence = 50
    severity = 2
    categories = ["antivirus"]
    authors = ["liebesu"]
    minimum = "0.5"

    def run (self):
        md5_indicators = ["c597db66cfbdbda27eb666b859f64ab0"
                           ,"8C545F6F1BA83C15B8B02EE4AA62FF11"
                          ,""
                          ]
        self.check_file=(pattern="\\")
        return



