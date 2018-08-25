#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import requests
import re
from bs4 import BeautifulSoup


def get_page_count(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "lxml")

    # 获得总的页数
    try:
        page_box = soup.find_all('div', class_='page-box')[0]
        matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
        total_page = int(matches.group(1))
    except Exception as e:
        print("\tWarning: only find one page for {0}".format(url))
        print("\t" + e.message)
        total_page = 1

    return total_page

if __name__ == '__main__':
    print(get_page_count("https://sh.ke.com/xiaoqu/"))