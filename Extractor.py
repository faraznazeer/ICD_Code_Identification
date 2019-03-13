<<<<<<< HEAD
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.xhtml.writer import XHTMLWriter
import re

class Extract:
    def __init__(self, files):
        import re
=======
class Extractor:
    def __init__(self, files):
        from ParseRTF import striprtf
>>>>>>> c2fd89bc194af12e9e335e5c0a21f3254b026bb6
        assert type(files) is list, "List of file paths expected"
        self.files = files
        self.terminate = ["history", "discharge advise", "procedure"]
        self.result = {}
        for document in files:
            text=''
            doc = open(document, "r").readlines()
            for lines in doc:
                text+=lines
            text=striprtf(text)
            text=text.split('\n')
            append = False
            extract = []
            for i in text:
                i = i.lower()
                if "diagnosis" in i:
                    append = True
                else:
                    for word in self.terminate:
                        if word in i:
                            append = False
                if append:
                    extract.append(i)
            diagnosis = []
            diagnosis = extract
            if len(diagnosis)>0:
                if ":" in diagnosis[0]:
                    diagnosis[0] = diagnosis[0].split(":")[1]
            i = 0
            while i < len(diagnosis):
                diagnosis[i]=diagnosis[i].strip()
                if diagnosis[i].strip() == '':
                    del diagnosis[i]
                    i = i - 1
                i += 1
            self.result[document] = diagnosis
    def getalldiagnosis(self):
        return self.result
    def getdiagnosis(self, document):
        assert document in self.files, "Specified file doesn't exist"
        return self.result[document]
