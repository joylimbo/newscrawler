#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import json

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request,FormRequest
from crawler.items import *

class Spider(CrawlSpider):
    name = 'sina1'
    start_urls = [
	    'https://api.weibo.com/2/trends/daily.json?acess_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE',
            #'http://top.news.com.cn/ws/GetTopDataList.php?top type=day&top cat=www all&top time=20130322&top show num=100&top order=ASC&js var=all 1 data01',
            ]
    is_start = True

    def parse(self, response):
        items = []
        statuses = json.loads(response.body)['trends']#'data']
        for s in statuses:
            u = s['user']
            items.append(self.user(u))
            #items.append(self.status(s))
        return items

    def user(self, user):
        item = UserItem()
        #item['name'] = user.get('title','')
        item['name'] = user.get('name','')
	item['platform'] = 'swb'
	item['amount'] = user.get('amount','')
        #item['url'] = user.get('url','')
        #item['comment_url'] = user.get('comment_url','')
        return item
