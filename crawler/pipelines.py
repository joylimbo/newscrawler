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

	elif 'VideoItem' == item.__class__.__name__:
	    f2=open(PROJECT_PATH+"/data/videos/2013-04-02/youku_video.txt",'a')
            f2.write("<title>")
            f2.write(str(item['title'].encode('utf-8')))
            f2.write("\n")
            #f2.write("<subtitle>")
            #f2.write(str(item['subtitle'].encode('utf-8')))
	    #f2.write("\n")
	    f2.close()

        elif 'UserItem' == item.__class__.__name__:
	    f1=open(PROJECT_PATH+"/data/news/rank/2013-04-02/sina_rank.txt",'a')
	    f1.write("<name>")
	    f1.write(str(item['name'].encode('utf-8')))
	    f1.write("\n")
	    f1.write("<url>")
	    f1.write(str(item['url']))
	    f1.write("\n")
	    f1.write("<comment_url>")
	    f1.write(str(item['comment_url']))
	    f1.write("\n")
	    f1.close()

	elif 'SinaRankItem' == item.__class__.__name__:
	    f5=open(PROJECT_PATH+"/crawler/spiders/rank.txt",'a')
            f5.write(str(item['url']))
            f5.write("\n")
	    f5.close()
            #f5.write("<id>")
            #f5.write(str(item['id_num']))
            #f5.write("\n")
            #f5.write("<title>")
            #f5.write(str(item['title'].encode('utf-8')))
            #f5.write("\n")
            #f5.write("<keywords>")
            #f5.write(str(item['keywords'].encode('utf-8')))
            #f5.write("\n")
	    #f5.write("<time>")
            #f5.write(str(item['time']))
            #f5.write("\n")
            #f5.write("<media>")
            #f5.write(str(item['media'].encode('utf-8')))
            #f5.write("\n")
            #f5.write("<comment_url>")
            #f5.write(str(item['comment_url']))
            #f5.write("\n")
	    #f5.write("<url>")
	    #f5.write(str(item['url']))
            #f5.write("\n")
	    #f5.write("********************************************\n")
            #f5.close()

	elif 'SinaNewsItem' == item.__class__.__name__:
        #print dict(item)
            f4=open(PROJECT_PATH+"/data/news/sina/2013-04-02/"+item['title']+".txt",'w')
            item['content'] = re.sub(ur'<[^>]*>','\n',re.sub(ur'\]\]>','',item['content']))
            f4.write("<title>")
            f4.write(str(item['title'].encode('utf-8')))
            f4.write("\n<date>")
            f4.write(str(item['datetime'].encode('utf-8')))
            #f3.write("\n<source>")
            #f3.write(str(item['source'].encode('utf-8')))
            f4.write("\n<keywords>")
            f4.write(str(item['keywords'].encode('utf-8')))
            f4.write("\n<content>")
            f4.write(str(item['content'].encode('utf-8')))
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
            #f.write(str(item['image_link']))
            f4.write("\n<image_path>")
            f4.write(str(item['path']))
            f4.close()
      
	elif 'SohuNewsItem' == item.__class__.__name__:
        #print dict(item)
            f3=open(PROJECT_PATH+"/data/news/sohu/2013-04-02/"+item['title']+".txt",'w')
            item['content'] = re.sub(ur'<[^>]*>','\n',re.sub(ur'\]\]>','',item['content']))
            f3.write("<title>")
            f3.write(str(item['title'].encode('utf-8')))
            f3.write("\n<date>")
            f3.write(str(item['datetime'].encode('utf-8')))
	    #f3.write("\n<source>")
            #f3.write(str(item['source'].encode('utf-8')))
            f3.write("\n<keywords>")
            f3.write(str(item['keywords'].encode('utf-8')))
            f3.write("\n<content>")
            f3.write(str(item['content'].encode('utf-8')))
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
            #f.write(str(item['image_link']))
            f3.write("\n<image_path>")
	    f3.write(str(item['path']))
            f3.close()

	elif 'QQNewsItem' == item.__class__.__name__:
        #print dict(item)
            f=open(PROJECT_PATH+"/data/news/tencent/2013-04-02/"+item['title']+".txt",'w')
	    item['content'] = re.sub(ur'<[^>]*>','\n',re.sub(ur'\]\]>','',item['content']))
	    f.write("<title>")
            f.write(str(item['title'].encode('utf-8')))
	    f.write("\n<date>")
            f.write(str(item['datetime'].encode('utf-8')))
	    f.write("\n<keywords>")
            f.write(str(item['keywords'].encode('utf-8')))
	    f.write("\n<content>")
            f.write(str(item['content'].replace("<br>","\n").encode('utf-8')))
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
            #f.write(str(item['image_link']))
	    f.write("\n<image_path>")
            f.write(str(item['path']))
	    f.write("\n<video_path>")
	    f.write(str(item['video_link']))
            f.close()

	elif 'QQNewsRankItem' == item.__class__.__name__:
            f6=open(PROJECT_PATH+"/data/news/tencent/2013-04-02/"+item['title']+".txt",'w')
            item['content'] = re.sub(ur'<[^>]*>','\n',re.sub(ur'\]\]>','',item['content']))
            f6.write("<title>")
            f6.write(str(item['title'].encode('utf-8')))
            f6.write("\n<date>")
            f6.write(str(item['datetime'].encode('utf-8')))
            f6.write("\n<keywords>")
            f6.write(str(item['keywords'].encode('utf-8')))
            f6.write("\n<content>")
            f6.write(str(item['content'].replace("<br>","\n").encode('utf-8')))
            f6.write("\n<image_path>")
            f6.write(str(item['path']))
            f6.write("\n<video_path>")
            f6.write(str(item['video_link']))
            f6.close()

        return item
