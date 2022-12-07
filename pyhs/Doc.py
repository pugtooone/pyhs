import os

class Doc:
    def __init__(self, directory):
        """
        initialize DocList obj
        Parameter: Path obj of JobDir
        """
        self.docDir = directory / 'Documents'

    def get_doc_list(self):
        self.docList = os.listdir(self.docDir)
        return self.docList

    # globbing pattern for counting the documents, which is universal to all instances: {'pattern to search for': 'document'}
    docPattern = {'*Post-production*': 'post-production guideline', '*Shoot Brief*': 'shoot brief', '*Retouch Note*': 'retouch note', 'Swatches': 'swatches', 'Overlays': 'overlays', '*Feedback*': 'feedback document', 'References': 'reference images'}

    def get_doc_items(self):
        """
        return a string of document items for email usage
        """
        self.docCountList = []
        # append the documents(values) to the docCountList(list), if pattern(keys) present
        for pattern, doc in Doc.docPattern.items():
            if self._doc_glob(pattern):
                self.docCountList.append(doc)

        #docItems with only 1 document
        if len(self.docCountList) == 1:
            self.docItems = 'the ' + self.docCountList[0]
        elif len(self.docCountList) == 0: 
            return None
        #docItems with more than 1 document
        else:
            for i in range(len(self.docCountList) - 1):
                self.docCountList[i] = 'the ' + self.docCountList[i]
            self.docCountList[-1] = 'and the ' + self.docCountList[-1]
            self.docItems = ', '.join(self.docCountList)

        return self.docItems

    def _doc_glob(self, pattern):
        """
        internal pattern search method for get_doc_list()
        could change to re for case-insensitive matching
        """
        try:
            if next(self.docDir.glob(pattern)):
                return True
        except StopIteration:
            return False
