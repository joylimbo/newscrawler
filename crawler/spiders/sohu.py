#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import urlparse
import json
import requests
from md5 import md5

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from scrapy.http import Request
from crawler.items import *

class Spider(CrawlSpider):
    name = 'sohu'
    start_urls =[
            'http://m.sohu.com/',
            ]
    "http://m.sohu.com/cm/367443014/?_once_=000019_pinglun_zhengwenye_gengduopinglunv2&tag=all&_smuid=1FlfiUkvPt9rZMvzn6Qjxa&v=2"
    "http://m.sohu.com/cm/367443014/?page=3&tag=all"

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//a/@href").re("/n/.*/"))):
            yield Request("http://m.sohu.com"+url+"?show_rest_pages=1",callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = NewsItem()
        #item['title'] = hxs.select("//h2[@class=\"a3\"]/text()").extract()[0].strip()
        item['datetime'] = hxs.select("//p[@class=\"a3 f12 c2 pb1\"]/text()").extract()[0].strip()
        #item['content'] = hxs.select("//div[@class=\"w1 Text\"]/div").extract()[0].strip()
        item['keywords'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].strip()
        #item['comment1'] = hxs.select("//div[@class=\"w1 bd3\"][1]/p[2]").extract()[0].strip()
	#item['ding1'] = hxs.select("//div[@class=\"w1 bd3\"]/p[@class=\"f\"][1]/a[2]/text()").extract()[0].strip()
	#item['comment2'] = hxs.select("//div[@class=\"w1 bd3\"][2]/p[2]").extract()[0].strip()
	#item['ding2'] = hxs.select("//div[@class=\"w1 bd3\"]/p[@class=\"f\"][2]/a[2]/text()").extract()[0].strip()
	#item['comment3'] = hxs.select("//div[@class=\"w1 bd3\"][3]/p[2]").extract()[0].strip()
	#item['ding3'] = hxs.select("//div[@class=\"w1 bd3\"]/p[@class=\"f\"][3]/a[2]/text()").extract()[0].strip()
        #item['comment_num'] = hxs.select("//p[@class=\"w1 b1 bd2\"]/span/text()").extract()[0].strip()
        #item['image_link'] = hxs.select("//p[@class=\"a3\"]/img/@src").extract()
	#item['tags'] = hxs.select("//p[@class=\"a3\"]/img/@alt").extract()
        return item

#    def parse_images(self,response):
#	hxs = HtmlXPathSelector(response)
#	item = ImgItem()
#	item['link'] = hxs.select("//img/@src").extract()
	#data = json.loads(requests.get(url).text)[0]

	#item = NewsItem()
	#item['best'] = hxs.select("//meta[@name=\"keywords\"]@content").extract()[0]
	
	#items.append(item)
	
#	return items
	#pass
