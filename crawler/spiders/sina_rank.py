#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import json

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request,FormRequest
from crawler.items import *
from crawler.settings import PROJECT_PATH

class Spider(CrawlSpider):
    name = 'sina_rank'
    start_urls = [
            'http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=world&top_time=today&top_show_num=10&top_order=ASC&js_var=world_1_data&call_back=showContent&short_title=1'
            ]
    is_start = True

    def parse(self, response):
        items = []
        statuses = json.loads(response.body[19:-71:])['data']
        for rank_list in statuses:
            item = SinaRankItem()
            item['id_num'] = rank_list.get('id','')
            item['keywords'] = rank_list.get('short_title','')
            item['title'] = rank_list.get('title','')
            item['time'] = rank_list.get('time','')
            item['media'] = rank_list.get('media','')
            item['url'] = rank_list.get('url','')
            item['comment_url'] = rank_list.get('comment_url','')
            items.append(item)
	
	#rank = open(PROJECT_PATH+"/crawler/spiders/rank.txt",'r')
	#url = rank.readline()
        #yield Request(url,callback=self.parse_content)
	#rank.close()

        for item in items:
            yield self.return_item(item)

    def return_item(self,item):
        return item

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = SinaNewsItem()
        item['title'] = hxs.select("//h1[@id=\"artibodyTitle\"]/text()").extract()[0].strip()
        item['datetime'] = hxs.select("//span[@id=\"pub_date\"]/text()").extract()[0].strip()
        item['content'] = hxs.select("//div[@class=\"blkContainerSblkCon BSHARE_POP\"]").extract()[0].strip()
        item['keywords'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].strip()
	#item['image_link'] = hxs.select("//div[@class=\"img_wrapper\"]/img/@src").extract()
        return item
