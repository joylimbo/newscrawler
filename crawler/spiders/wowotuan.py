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
    get store info and tuangou info
    '''
    name = 'wowotuan'
    start_urls =[
            #'http://weihai.55tuan.com/meishi',
            'http://weihai.55tuan.com/meishi-0-0-0-0-0-0-2',
            'http://weihai.55tuan.com/meishi-0-0-0-0-0-0-2',
            'http://weihai.55tuan.com/meishi-0-0-0-0-0-0-2',
            'http://weihai.55tuan.com/meishi-0-0-0-0-0-0-2',
            ]
    def parse(self,response):
        items = []
        hxs = HtmlXPathSelector(response)
        if re.match(ur".*store.*",response.url):
            items += parse_store(response)
        elif re.match(ur".*goods.*",response.url):
            items += parse_goods(response)
        else :
            #for url in list(set(hxs.select("//a/@href").re(".*store.*"))):
                #yield Request(url,callback=self.parse)
            for url in list(set(hxs.select("//a/@href").re("/goods.*\.html"))):
                yield Request("http://weihai.55tuan.com"+url,callback=self.parse)

        for item in items:
            yield self.return_item(item)

    def return_item(self,item):
        return item

def parse_store(response):
    """
    query:
    http://shop.55tuan.com/s/getShopByStoreId.do?storeId=62217015030e1ae1&cityId=123&callback=jsonp1361695737488&_=1361695737489
    result:
    [{"shopId":"58ba287a7efcc01c","storeId":"62217015030e1ae1","addr":"环翠区新威路128号","shopName":"亚马逊巴西烤肉","trafficInfo":"107、109、106、9、1、12、43、101、110、53路公交车到海运学校或南大桥即到","telMsg":"0631-5210188","lon":122.125811,"lat":37.496499,"localShopTotal":1,"cityName":"威海","businessHours":"17:30-21:00"}]

    query:
    http://shop.55tuan.com/s/getShopsByGoodsId.do?cityId=123&goodsId=47f52e8676655d97&type=shoplist&callback=jsonp1361697487535&_=1361697487536
    result:
    [{"addr":"黎明村金华超市东20米","shopName":"正宗老北京绿豆饼（荣成）","trafficInfo":"","telMsg":"18660312346","lon":122.429944,"lat":37.146452,"businessHours":"08:00-17:00"}]
    """
    items = []
    data = json.loads(response.body)
    for r in data:
        item = StoreItem()
        item['store'] = r['shopId']
        item['addr'] = r['addr']
        item['name'] = r['shopName']
        item['traffic'] = r['traffic']
        item['phone'] = r['telMsg']
        item['lon'] = r['lon']
        item['lat'] = r['lat']
        item['localShopTotal'] = r['localShopTotal']
        item['city'] = r['cityName']
        item['businessHours'] = r['businessHours']
        item['market'] = "wowotuan"
        item['desc'] = hxs.select("//div[@class=\"lft\"]/ul/li/p/text()").extract()[0]

    items.append(item)
    return items

def parse_goods(response):
    items = []
    hxs = HtmlXPathSelector(response)
    #url = "http://shop.55tuan.com/s/getShopsByGoodsId.do?cityId=123&goodsId=47f52e8676655d97&type=shoplist"
    url = hxs.select("//input[@id=\"baiduDataurl\"]/@value").extract()[0]
    data = json.loads(requests.get(url).text)[0]

    item = TuanItem()
    item['market'] = "wowotuan"
    item['goodsid'] = re.findall(ur"goods-.*\.",response.url)[0][6:-1:]
    item['title'] =  hxs.select("//p[@class=\"title\"]/text()").extract()[0] 
    item['content'] = hxs.select("//textarea[@id=\"goodsAll_info\"]").extract()[0]
    item['price'] = hxs.select("//em[@class=\"xq_boem xq_boem1\"]/text()").extract()[0]
    item['lon'] = data.get("lon","")
    item['lat'] = data.get("lat","")

    items.append(item)

    item = StoreItem()
    item['market'] = "wowotuan"
    item['store'] = data.get('shopId','')
    item['addr'] = data.get('addr','')
    item['name'] = data.get('shopName','')
    item['traffic'] = data.get('traffic','')
    item['phone'] = data.get('telMsg','')
    item['lon'] = data.get('lon','')
    item['lat'] = data.get('lat','')
    item['localShopTotal'] = data.get('localShopTotal','')
    item['city'] = data.get('cityName','')
    item['businessHours'] = data.get('businessHours','')

    items.append(item)

    return items
