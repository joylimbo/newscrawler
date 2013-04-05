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
    name = 'tencent_rank'
    start_urls =[
            'http://news.qq.com/world_index.shtml',
	 ]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//ol/li/a/@href").extract())):
            yield Request(url,callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = QQNewsItem()
        item['title'] = hxs.select("//div[@class=\"hd\"]/h1/text()").extract()[0].strip()
        item['datetime'] = hxs.select("//span[@class=\"article-time\"]/text()").extract()[0].strip()
	item['content'] = hxs.select("//div[@id=\"Cnt-Main-Article-QQ\"]").extract()[0].strip()
        item['keywords'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].strip()
	#item['comments'] = hxs.select("//span[@class=\"c2\"]/text()").extract()[0].strip()
	item['video_link'] = hxs.select("//h3/a[@target=\"_blank\"]/@href").extract()
        item['image_link'] = hxs.select("//div[@id=\"Cnt-Main-Article-QQ\"]/p[@align=\"center\"]/img/@src").extract() 
        return item

