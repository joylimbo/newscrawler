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
	    #'https://api.weibo.com/2/trends/daily.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE',
            'http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=www_all&top_time=20130324&top_show_num=100&top_order=ASC&js_var=all_1_data01',
	    ]
    is_start = True

    def parse(self, response):
        items = []
	
        statuses = json.loads(response.body[19:-2:])['data']
	#print "statuses",statuses
        for s in statuses:
	    #print "s=",s
	    items.append(self.user(s))
        return items

    def user(self, user):
        item = UserItem()
        item['name'] = user.get('title','')
        #item['name'] = user.get('name','')
	#item['amount'] = user.get('amount','')
        item['url'] = user.get('url','')
        item['comment_url'] = user.get('comment_url','')
        return item
