''' Piranha - Simple Amazon scraper

Piranha is a simple Amazon scraper. Using the Amazon Product Advertising API, Piranha searches Amazon for you. Nuff said.

Scraper by Adam Engel.

'''

import requests as r
import xmltodict
import datetime as d
from pprint import PrettyPrinter

p = PrettyPrinter()

class Piranha:

    itemsearchvalidparameters = ['Actor','Artist','AudienceRating','Author','Availability','Brand','BrowseNode','Composer','Condition','Conductor','Director','IncludeReviewsSummary','ItemPage','Keywords','Manufacturer','MaximumPrice','MerchantId','MinimumPrice','MinPercentageOff','Orchestra','Power','Publisher','RelatedItemPage','RelationshipType','SearchIndex','Sort','Title','TruncateReviewsAt','VariationPage','ResponseGroup']
    
    def __init__(self, AWSAccessKeyId, AWSSecretKey, AssociateId):
        self.access = AWSAccessKeyId
        self.secret = AWSSecretKey
        self.assoc = AssociateId
        self.baseurl = "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&AWSAccessKeyId=%s&AssociateTag=%s&Timestamp=%d&Signature=[Request Signature]"%(self.access, self.assoc, )
    
    def ItemSearch(self, **kwargs):
        print(type(kwargs))
        print(kwargs)
        url = self.baseurl
        for arg in kwargs:
            url += ("&%s=%s"%(arg, kwargs[arg])) # Creates the search URL
        print(url)
        data = r.get(url)
        # return data.json()
        print(data)
        
    # def ItemLookup(self, **kwargs):
