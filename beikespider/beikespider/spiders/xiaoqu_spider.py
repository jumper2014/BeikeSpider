#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import time
from scrapy.spiders import Spider
from beikespider.items import BeikespiderXiaoQuItem
from beikespider.libs.const import *
from beikespider.libs.url import *
from beikespider.libs.printer import *


class XiaoQuSpider(Spider):
    name = 'xiaoqu'
    allowed_domains = KE_DOMAIN
    start = time.time()
    start_urls =[]
    city = None

    def __init__(self):
        # 只有第一次进来才初始化url列表
        if len(XiaoQuSpider.start_urls) == 0:
            url = URL(XiaoQuSpider.name)
            XiaoQuSpider.start_urls = url.start_urls
            XiaoQuSpider.city = url.city

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
        item = BeikespiderXiaoQuItem()
        html = response.body
        soup = BeautifulSoup(html, "lxml")

        # 获得有小区信息的panel
        elements = soup.find_all('li', class_="xiaoquListItem")
        print_item_num(len(elements))
        for element in elements:
            title = element.find('div', class_="title")
            name = title.text.replace("\n", "")

            price = element.find('div', class_="totalPrice")
            price = price.text.strip()

            on_sale = element.find('div', class_="xiaoquListItemSellCount")
            on_sale = on_sale.text.replace("\n", "").strip()
            # 继续清理数据

            print("{0} {1} {2}".format(name, price, on_sale))
            item['name'] = name
            item['price'] = price
            item['on_sale'] = on_sale
            yield item


