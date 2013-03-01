#coding:utf-8
from scrapy.item import Item, Field

class CrawlerItem(Item):
    pass
class TuanItem(Item):
    goodsid = Field()
    date = Field()
    market = Field()
    title = Field()
    price = Field()
    content = Field()
    lon = Field()
    lat = Field()


    def __str__(self):
        return ("TuanItem:%s"%(self['title']))

class StoreItem(Item):
    market = Field()
    store = Field()
    name = Field()
    desc = Field()
    addr = Field()
    traffic = Field()
    phone = Field()
    localShopTotal = Field()
    businessHours = Field()
    city = Field()
    lon = Field()
    lat = Field()

    def __str__(self):
        return ("StoreItem:%s"%(self['name']))

class NewsItem(Item):
    title = Field()
    datetime  = Field()
    content = Field()
    images = Field()
    video = Field()

