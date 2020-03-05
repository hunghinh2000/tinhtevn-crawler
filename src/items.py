# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TinhtecrawlerItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    startDateTime = scrapy.Field()
    comment = scrapy.Field()
    view = scrapy.Field()
    #imgNameList = scrapy.Field()
