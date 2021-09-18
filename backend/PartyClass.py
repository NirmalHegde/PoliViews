
class Party():

    def __init__(self, name):

        self.name = name
        self.summary = ""
        self.relatedlink = {
            "link": None,
            "sentiment": None 
        }
        
    def addSummary(self, text):

        self.summary = text

    def addRelatedLink(self, link, sentiment):
        
        self.relatedlink["link"] = link
        self.relatedlink["sentiment"] = sentiment
