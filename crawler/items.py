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
    image_link = Field()
    video = Field()
    tags = Field()
    keywords = Field()
    comment1 = Field()
    ding1 = Field()
    comment2 = Field()
    ding2 = Field()
    comment3 = Field()
    ding3 = Field()
    comment_num = Field()
    path = Field()
    images = Field()
    image_urls = Field()
    image_paths = Field()

    def __str__(self):
        return ("ImgItem:%s"%(self['title']))

class ImgItem(Item):
    hashmd5 = Field()
    name = Field()
    link = Field()
    refer = Field()
    tags = Field()
    path = Field()
    height = Field()
    width = Field()
    image_urls = Field()
    image_paths = Field()
    images = Field()

    def __str__(self):
	return ("ImgItem:%s"%(self['link']))
