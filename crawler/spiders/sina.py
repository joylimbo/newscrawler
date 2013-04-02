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
from crawler.settings import PROJECT_PATH

class Spider(CrawlSpider):
    name = 'sina'
    start_urls =[
            'http://news.sina.com.cn/',
	 ]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)

	rank = open(PROJECT_PATH+"/crawler/spiders/rank.txt",'r')
        #url = rank.readline()
	for url in rank.readlines():
	    print url
            yield Request(url[0:-1:],callback=self.parse_content)
        rank.close()

        #for url in list(set(hxs.select("//a/@href").re("http://news.sina.com.cn/c/.*"))):
            #yield Request(url,callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = SinaNewsItem()
        item['title'] = hxs.select("//h1[@id=\"artibodyTitle\"]/text()").extract()[0].strip()
        item['datetime'] = hxs.select("//span[@id=\"pub_date\"]/text()").extract()[0].strip()
	item['content'] = hxs.select("//div[@class=\"blkContainerSblkCon BSHARE_POP\"]").extract()[0].strip()
        item['keywords'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].strip()
	#item['comments'] = hxs.select("//span[@class=\"c2\"]/text()").extract()[0].strip()
	#item['video_link'] = hxs.select("//h3/a[@target=\"_blank\"]/@href").extract()
        item['image_link'] = hxs.select("//div[@class=\"img_wrapper\"]/img/@src").extract()
        return item

