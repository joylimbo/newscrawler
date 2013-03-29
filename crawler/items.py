#coding:utf-8
from scrapy.item import Item, Field

class CrawlerItem(Item):
    pass

class SohuNewsItem(Item):
    title = Field()
    datetime = Field()
    source = Field()
    content = Field()
    image_link = Field()
    video_link = Field()
    keywords = Field()
    comment1 = Field()
    comment2 = Field()
    comment3 = Field()
    comment_num = Field()
    ding1 = Field()
    ding2 = Field()
    ding3 = Field()
    path = Field()
    images = Field()
    image_urls = Field()
    image_paths = Field()

    def __str__(self):
	return ("ImgItem:%s"%(self['title']))

class QQNewsItem(Item):
    title = Field()
    datetime  = Field()
    content = Field()
    image_link = Field()
    video_link = Field()
    tags = Field()
    keywords = Field()
    comment1 = Field()
    comment2 = Field()
    comment3 = Field()
    comment_num = Field()
    ding1 = Field()
    ding2 = Field()
    ding3 = Field()
    path = Field()
    images = Field()
    image_urls = Field()
    image_paths = Field()

    def __str__(self):
        return ("ImgItem:%s"%(self['title']))

class SinaNewsItem(Item):
    title = Field()
    datetime  = Field()
    content = Field()
    image_link = Field()
    video_link = Field()
    tags = Field()
    keywords = Field()
    comment1 = Field()
    comment2 = Field()
    comment3 = Field()
    comment_num = Field()
    ding1 = Field()
    ding2 = Field()
    ding3 = Field()
    path = Field()
    images = Field()
    image_urls = Field()
    image_paths = Field()

    def __str__(self):
        return ("ImgItem:%s"%(self['title']))


class VideoItem(Item):
    title = Field()
    subtitle = Field()

    def __str__(self):
	return ("VideoItem:%s"%(self['title']))

class UserItem(Item):
    name = Field()
    url = Field()
    comment_url = Field()
    platform = Field()
    amount = Field()

    def __str__(self):
	return ("UserItem:%s"%(self['name']))

class SinaRankItem(Item):
    id_num = Field()
    title = Field()
    keywords = Field()
    time = Field()
    media = Field()
    comment_url = Field()
    url = Field()

    def __str__(self):
        return ("SinaRankItem:%s"%(self['title']))

class ImgItem(Item):
 #   hashmd5 = Field()
  #  name = Field()
   # link = Field()
   # refer = Field()
   # tags = Field()
    path = Field()
    height = Field()
    width = Field()
   # image_urls = Field()
   # image_paths = Field()
   # images = Field()

   # def __str__(self):
#	return ("ImgItem:%s"%(self['link']))
