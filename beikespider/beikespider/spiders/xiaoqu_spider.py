#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from beikespider.libs.page import *
from beikespider.items import BeikespiderItem


class BlogSpider(Spider):
    name = 'xiaoqu'
    allowed_domains = 'ke.com'
    page_count = get_page_count('https://sh.ke.com/xiaoqu/')
    start_urls = ['https://sh.ke.com/xiaoqu/pg{0}'.format(i) for i in range(1, page_count+1)]

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


