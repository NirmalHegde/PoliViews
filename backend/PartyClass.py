
class Party():

    def __init__(self, name):

        self.name = name
        self.summary = ""
        self.relatedlink = {
            "link": None,
            "sentiment": None,
            "title": None,
            "summary":None,
            "picture":None 
        }
        self.responseformat = {}
        
    def addSummary(self, text):

        self.summary = text

    def addRelatedLink(self, link, sentiment, title, summary, picture):
        
        self.relatedlink["link"] = link
        self.relatedlink["sentiment"] = sentiment
        self.relatedlink["title"] = title
        self.relatedlink['summary'] = summary
        self.relatedlink['picture'] = picture

    def formatResponse(self):

        self.responseformat = {
            "summary": self.summary,
            "relatedlinks": {
                "link": self.relatedlink["link"],
                "title": self.relatedlink['title'],
                "summary": self.relatedlink['summary'],
                "picture": self.relatedlink["picture"],
                "sentiment": self.relatedlink['sentiment']
            }
        }

        return self.responseformat