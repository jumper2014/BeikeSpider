# BeikeSpider
- 贝壳网房价爬虫
- 基于scrapy爬虫框架

# 运行
- cd BeikeSpider/beikespider
- scrapy crawl xiaoqu --nolog       # 爬取小区数据
- scrapy crawl ershoufang --nolog   # 爬取二手房数据


# 性能
- 小区：171秒抓取18623条小区数据，平均每秒100条


# 依赖
- Python 3.6
- scrapy
- requests
- beautifulsoup4

# 更新记录
- 2018/09/15, 爬取二手房数据
- 2018/09/09, 多线程获取城市版块信息，提升爬取速度
- 2018/09/08, 能够按城市和日期存放csv文件
- 2018/09/02, 能够存入csv, 计时，指定城市爬取
- 2018/08/19, 项目创建

# 开发计划

- 能够统计价格信息
- 能够爬取租房数据
- 能够爬取小区数据
- 能够爬取新楼盘数据
- 能够设置爬取的城市
- 能够存入MySQL
- 能够记录区县和版块
- 能够爬取二手房数据 (done)
- 进行提速 (done)
- 存入csv (done)
- 能够计时 （done）

