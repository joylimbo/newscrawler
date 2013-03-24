import requests
import re

from md5 import md5
from datetime import datetime
from cStringIO import StringIO
from PIL import Image
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from crawler.settings import PROJECT_PATH

class images_process(ImagesPipeline):
    def get_images(self, response, request, info):
        key = self.image_key(request.url)
        orig_image = Image.open(StringIO(response.body))

        width, height = orig_image.size

        image, buf = self.convert_image(orig_image)
        yield key, image, buf

    def get_media_requests(self, item, info):
        for image_url in item['image_link']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        else:
	    item['path'] = image_paths
	return item

class mongo_storage(object):
    
    def __init__(self):
        #connection = pymongo.Connection(MONGODB['host'],MONGODB['port'])
        #self.db = connection[MONGODB['name']]
        self.date = datetime.now().strftime("%Y-%m-%d")
    
    def process_item(self,item,spider):
        if 'ImgItem' == item.__class__.__name__:
            self.process_img_item(item)
        elif 'UserItem' == item.__class__.__name__:
	    f1=open(PROJECT_PATH+"/data/news/rank/sina_rank.txt",'a')
	    f1.write("<name>")
	    f1.write(str(item['name'].encode('utf-8')))
	    #f1.write(str(item['title'].encode('utf-8')))
	    #f1.write("\n")
	    #f1.write("amount:")
	    #f1.write(str(item['amount']))
	    f1.write("\n")
	    f1.write("<url>")
	    f1.write(str(item['url']))
	    f1.write("\n")
	    f1.write("<comment_url>")
	    f1.write(str(item['comment_url']))
	    f1.write("\n")
	    f1.close()
       
	elif 'NewsItem' == item.__class__.__name__:
        #print dict(item)
            f=open(PROJECT_PATH+"/data/news/tencent/2013-3-24/"+item['title']+".txt",'w')
	    item['content'] = re.sub(ur'<[^>]*>','\n',re.sub(ur'\]\]>','',item['content']))
	    f.write("<title>")
            f.write(str(item['title'].encode('utf-8')))
            #f.write("\n*******************************\n")
	    f.write("\n<date>")
            f.write(str(item['datetime'].encode('utf-8')))
            #f.write("\n*******************************\n")
	    f.write("\n<keywords>")
            f.write(str(item['keywords'].encode('utf-8')))
            #f.write("\n*******************************\n")
	    f.write("\n<content>")
            f.write(str(item['content'].replace("<br>","\n").encode('utf-8')))
            #f.write("\n*******************************\n")
            #f.write("No.1\n")
	    #f.write(str(item['comment1'].encode('utf-8')))
            #f.write(str(item['ding1'].encode('utf-8')))
	    #f.write("No.2\n")
	    #f.write(str(item['comment2'].encode('utf-8')))
	    #f.write(str(item['ding2'].encode('utf-8')))
	    #f.write("No.3\n")
	    #f.write(str(item['comment3'].encode('utf-8')))
	    #f.write(str(item['ding3'].encode('utf-8')))
	    #f.write("\n")
            #f.write(str(item['comment_num'].encode('utf-8')))
	    #f.write("\n******************************\n")
            #f.write(str(item['image_link']))
	    f.write("\n<path>")
            f.write(str(item['path']))
	    #f.write(str(item['tags']))
            f.close()
        return item
