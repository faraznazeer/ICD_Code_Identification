class Extract:
    def __init__(self, files):
        from pyth.plugins.rtf15.reader import Rtf15Reader
        from pyth.plugins.xhtml.writer import XHTMLWriter
        import re
        assert type(files) is list, "List of file paths expected"
        self.files = files
        self.result = {}
        for document in files:
            doc = Rtf15Reader.read(open(document, "rb"))
            text = XHTMLWriter.write(doc, pretty=True)
            append = False
            extract = []
            for i in text:
                i = i.lower()
                if "diagnosis" in i:
                    append = True
                elif "history" in i or "discharge advise" in i or "procedure" in i:
                    append = False
                if append:
                    extract.append(i)
            diagnosis = []
            for i in extract:
                diagnosis += re.findall('(?<=>)([^<]+)(?=[^<]*<)', i, re.S)
            if ":" in diagnosis[0]:
                diagnosis[0] = diagnosis[0].split(":")[1]
            i = 0
            while i < len(diagnosis):
                if diagnosis[i].strip() == '':
                    del diagnosis[i]
                    i = i - 1
                i += 1
            self.result[document] = diagnosis

    def getlalldiagnosis(self):
        return self.result

    def getdiagnosis(self, document):
        assert document in self.files, "specified file doesn't exist"
        return self.result[document]
