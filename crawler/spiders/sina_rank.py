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
    name = 'sina_rank'
    start_urls = [
	    #'https://api.weibo.com/2/trends/daily.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE',
	    'http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=world&top_time=today&top_show_num=10&top_order=ASC&js_var=world_1_data&call_back=showContent&short_title=1'
            #'http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=week&top_cat=www_all&top_time=20130329&top_show_num=100&top_order=ASC&js_var=all_1_data01'
	    ]
    is_start = True

    def parse(self, response):
        items = []
	
        statuses = json.loads(response.body[19:-71:])['data']
	#print "statuses",statuses
        #for s in statuses:
	    #print "s=",s
	    #items.append(self.rank_list(s))
	#return items

	for url in rank_list.get('url',''):
            yield Request(url,callback=self.parse_content)

    def rank_list(self, rank_list):
        item = SinaRankItem()
	item['id_num'] = rank_list.get('id','')
	item['keywords'] = rank_list.get('short_title','')
        item['title'] = rank_list.get('title','')
	item['time'] = rank_list.get('time','')
	item['media'] = rank_list.get('media','')
        item['url'] = rank_list.get('url','')
        item['comment_url'] = rank_list.get('comment_url','')
	
	#for url in rank_list.get('url',''):
	    #yield Request(url,callback=self.parse_content)

	return item

    def parse_content(self,response):
	hxs = HtmlPathSelector(response)
	item = SinaNewsItem()
	item['title'] = hxs.select("//h1[@id=\"artibodyTitle\"]/text()").extract()[0].strip()
	item['datetime'] = hxs.select("//span[@id=\"pub_date\"]/text()").extract()[0].strip()
	item['content'] = hxs.select("//div[@class=\"blkContainerSblkCon BSHARE_POP\"]").extract()[0].strip()
	item['keywords'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].strip()
        return item
