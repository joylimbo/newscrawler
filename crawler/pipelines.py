#import pymongo
from datetime import datetime
from cStringIO import StringIO
from PIL import Image
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from crawler.settings import MONGODB

class images_process(ImagesPipeline):
    def get_images(self, response, request, info):
	key = self.image_key(request.url)
	orig_image = Image.open(StringIO(response.body))

	width, height = orig_image.size

	image, buf = self.convert_image(orig_image)
	yield key, image, buf

    def get_media_request(self, item, info):
	for image_url in item['image_link']:
	    yield Request(image_url)

    def item_completed(self, results, item, info):
	image_paths = [x['path'] for ok, x in results if ok]
	if not image_paths:
	    raise DropItem("Item contains no images")
	item['name'] = image_paths[0][8::]
	return item

class mongo_storage(object):
    
    def __init__(self):
        #connection = pymongo.Connection(MONGODB['host'],MONGODB['port'])
        #self.db = connection[MONGODB['name']]
        self.date = datetime.now().strftime("%Y-%m-%d")

    def process_item(self,item,spider):
	if 'TuanItem' == item.__class__.__name__:
	    self.process_tuan_item(item)
	elif 'StoreItem' == item.__class__.__name__:
	    self.process_store_item(item)
	elif 'ImgItem' == item.__class__.__name__:
	    self.process_img_item(item)
	else:
	   
	    #print dict(item)
	    f=open(item['title'],'w')
	    f.write(str(item['title'].encode('utf-8')))
	    f.write("\n*******************************\n")
	    #f.write(str(item['datetime'].encode('utf-8')))
	    #f.write("\n*******************************\n")
	    #f.write(str(item['keywords'].encode('utf-8')))
	    #f.write("\n*******************************\n")
	    #f.write(str(item['content'].encode('utf-8')))
	    #f.write("\n*******************************\n")
	    #f.write(str(item['comments'].encode('utf-8')))
            #f.write("\n")
	    #f.write(str(item['comments_best'].encode('utf-8')))
	    #f.write("\n")
	    #f.write(str(item['images'].encode('utf-8')))
	    f.write(str(item['image_link']))
	    #f.write(str(item['tags']))
	    f.close()
	return item

    def process_tuan_item(self,item):
	print dict(item)
	#if self.db.tuan.find({"goodsid":item['goodsid'],"market":item['market']}).count() is 0:
        #    self.db.tuan.insert(dict(item))
        pass

    def process_store_item(self,item):
        print dict(item)
        #if self.db.store.find({"lon":item['lon'],"lat":item['lat']}).count() is 0:
        #    self.db.store.insert(dict(item))
        pass
