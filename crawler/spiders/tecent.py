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
    name = 'tecent'
    start_urls =[
            'http://www.qq.com/',
            ]
    #"http://m.sohu.com/cm/367443014/?_once_=000019_pinglun_zhengwenye_gengduopinglunv2&tag=all&_smuid=1FlfiUkvPt9rZMvzn6Qjxa&v=2"
    #"http://m.sohu.com/cm/367443014/?page=3&tag=all"

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//li/a/@href").re("http://news.qq.com/a/.*"))):
            yield Request(url,callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = NewsItem()
        item['title'] = hxs.select("//div[@class=\"hd\"]/h1/text()").extract()[0].strip()
        item['datetime'] = hxs.select("//span[@class=\"article-time\"]/text()").extract()[0].strip()
	item['content'] = hxs.select("//div[@id=\"Cnt-Main-Article-QQ\"]").extract()[0].strip()
        item['keywords'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].strip()
	#item['comments'] = hxs.select("//span[@class=\"c2\"]/text()").extract()[0].strip()
	#item['tags'] = hxs.select("//div[@id=\"Cnt-Main-Article-QQ\"]/IMG/@alt").extract()
        #item['images'] = hxs.select("//div[@id=\"Cnt-Main-Article-QQ\"]/P/IMG/@src").extract() 
        return item

    def parse__comment(self,response):
	#item = []
	#hxs = HtmlXPathSelector(response)
	#url = hxs.select("//input[@id=\"?tag=hot\"]/@value").extract()[0]
	#data = json.loads(requests.get(url).text)[0]

	#item = NewsItem()
	#item['best'] = hxs.select("//meta[@name=\"keywords\"]@content").extract()[0]
	
	#items.append(item)
	pass
	#return items
