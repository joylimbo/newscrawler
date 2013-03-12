#import pymongo
from datetime import datetime
from scrapy.exceptions import DropItem
from scrapy import log
from crawler.settings import MONGODB

class mongo_storage(object):
    
    #f=open('sohu','wb')
    def __init__(self):
        #connection = pymongo.Connection(MONGODB['host'],MONGODB['port'])
        #self.db = connection[MONGODB['name']]
        self.date = datetime.now().strftime("%Y-%m-%d")

    def process_item(self,item,spider):
	if 'TuanItem' == item.__class__.__name__:
	    self.process_tuan_item(item)
	elif 'StoreItem' == item.__class__.__name__:
	    self.process_store_item(item)
	else:
	    #print dict(item)
	    f=open(item['title'],'w')
	    #item['content'].replace("br","\n")
	    f.write(str(item['title'].encode('utf-8')))
	    f.write("\n*******************************\n")
	    f.write(str(item['datetime'].encode('utf-8')))
	    f.write("\n*******************************\n")
	    f.write(str(item['keywords'].encode('utf-8')))
	    f.write("\n*******************************\n")
	    f.write(str(item['content'].encode('utf-8')))
	    f.write("\n*******************************\n")
	    #f.write(str(item['comments'].encode('utf-8')))
            #f.write("\n")
	    #f.write(str(item['comments_best'].encode('utf-8')))
	    #f.write("\n")
	    f.write(str(item['images'].encode('utf-8')))
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
