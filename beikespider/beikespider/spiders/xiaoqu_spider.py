#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from scrapy.spiders import Spider


class BlogSpider(Spider):
    name = 'xiaoqu'
    start_urls = ['https://sh.ke.com/xiaoqu/']

    def parse(self, response):
        titles = response.xpath('/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a/text()').extract()
        for title in titles:
            print(title.strip())
