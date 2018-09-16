#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import time
from scrapy.spiders import Spider
from beikespider.libs.const import *
from beikespider.items import *
from beikespider.libs.url import *
from beikespider.libs.printer import *

class ErShouFangSpider(Spider):
    name = 'ershoufang'
    allowed_domains = KE_DOMAIN
    start = time.time()
    start_urls = []
    city = None

    def __init__(self):
        # 只有第一次进来才初始化url列表
        if len(ErShouFangSpider.start_urls) == 0:
            url = URL(ErShouFangSpider.name)
            ErShouFangSpider.start_urls = url.start_urls
            ErShouFangSpider.city = url.city

    def closed(self, reason):
        """
        结束的时候计时
        :param reason:
        :return:
        """
        print_time_cost(time.time() - self.start)

    def parse(self, response):
        """
        针对每一个URL进行处理
        :param response:
        :return:
        """
        item = BeikespiderErShouFangItem()
        html = response.body
        soup = BeautifulSoup(html, "lxml")

        # 获得有二手房信息的panel
        elements = soup.find_all('li', class_="clear")
        print_item_num(len(elements))
        for element in elements:
            title = element.find('div', class_="title")
            name = title.text.replace("\n", "")

            price = element.find('div', class_="totalPrice")
            price = price.text.strip()

            # 继续清理数据

            print("{0} {1}".format(name, price))
            item['name'] = name
            item['price'] = price
            yield item


