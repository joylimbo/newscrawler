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
    '''
    get news from sohu
    '''
    name = 'sohu'
    start_urls =[
            'http://m.sohu.com/',
            ]
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//a/@href").re("/n/.*"))):
            yield Request("http://m.sohu.com"+url,callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(response):
        item = NewsItem()

        return items
