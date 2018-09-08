#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from beikespider.libs.city import *
from beikespider.libs.district import *
from beikespider.libs.area import *
from beikespider.libs.page import *

class XiaoQuURL(object):
    def __init__(self):
        prompt = create_prompt_text()
        city = input(prompt)
        self.city = city
        print('[{0}]'.format(city))
        chinese_city = get_chinese_city(city)
        if chinese_city is None:
            print("No such city, please try again.")
        else:
            print('OK, start to crawl ' + chinese_city)

        areas = []
        districts = get_districts(city)
        for district in districts:
            areas.extend(get_areas(city, district))

        print("-------------")
        print("Area is: ")
        print(areas)
        print("-------------")
        self.start_urls = []
        for area in areas:
            page_count = get_page_count('https://{0}.ke.com/xiaoqu/{1}'.format(city, area))
            print('total page: {0} for {1}:{2}'.format(page_count, city, area))
            for i in range(1, page_count + 1):
                self.start_urls.append('https://{0}.ke.com/xiaoqu/{1}/pg{2}'.format(city, area, i))
        print(self.start_urls)

if __name__ == '__main__':
    pass