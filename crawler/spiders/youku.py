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
    name = 'youku'
    start_urls =[
            'http://www.youku.com/',
	 ]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//li[@class=\"v_title\"]/a/@href").re("http://v.youku.com/.*"))):
            yield Request(url,callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = VideoItem()
        item['title'] = hxs.select("//h1[@class=\"title\"]/@title").extract()[0].strip()
        #item['subtitle'] = hxs.select("//span[@id=\"subtitle\"]/text()").extract()[0].strip() 
        return item

