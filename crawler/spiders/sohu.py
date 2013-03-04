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
        item['title'] = hxs.select("//h2[@class=\"a3\"]/text()").extract()[0].strip()
        item['datetime'] = hxs.select("//p[@class=\"a3 f12 c2 pb1\"]/text()").extract()[0].strip()
        item['content'] = hxs.select("//div[@class=\"w1 Text\"]/div").extract()[0].strip()
        item['tags'] = ""
        item['images'] = ""
        return item

    def parse__comment(self,response):
        pass
