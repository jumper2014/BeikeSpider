#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import time
from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from beikespider.libs.page import *
from beikespider.items import BeikespiderItem
from beikespider.libs.city import *


class XiaoQuSpider(Spider):
    name = 'xiaoqu'
    allowed_domains = 'ke.com'
    start = time.time()
    prompt = create_prompt_text()
    city = input(prompt)
    print('[{0}]'.format(city))
    print('OK, start to crawl ' + get_chinese_city(city))
    page_count = get_page_count('https://{0}.ke.com/xiaoqu/'.format(city))
    print('total page: {0}'.format(page_count))
    start_urls = []
    for i in range(1, page_count+1):
        start_urls.append('https://{0}.ke.com/xiaoqu/pg{1}'.format(city, i))

    def __init__(self):
        pass

    def closed(self, reason):
        print("-" * 50)
        print("total time cost:{0} seconds".format(time.time() - self.start))
        print("-" * 50)

    def parse(self, response):
        item = BeikespiderItem()
        html = response.body
        soup = BeautifulSoup(html, "lxml")

        # 获得有小区信息的panel
        xiaoqu_items = soup.find_all('li', class_="xiaoquListItem")
        print("----\nlen: {0}\n----\n".format(len(xiaoqu_items)))
        for xiaoqu_elem in xiaoqu_items:
            title = xiaoqu_elem.find('div', class_="title")
            name = title.text.replace("\n", "")

            price = xiaoqu_elem.find('div', class_="totalPrice")
            price = price.text.strip()

            on_sale = xiaoqu_elem.find('div', class_="xiaoquListItemSellCount")
            on_sale = on_sale.text.replace("\n", "").strip()
            # 继续清理数据

            print("{0} {1} {2}".format(name, price, on_sale))
            item['name'] = name
            item['price'] = price
            item['on_sale'] = on_sale
            yield item


