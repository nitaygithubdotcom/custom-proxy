# -*- coding: utf-8 -*-
import scrapy


class CproxySpider(scrapy.Spider):
    name = 'cproxy'
    start_urls = ['https://ipinfo.io/ip/']

    def parse(self, response):
        print(response.body)
