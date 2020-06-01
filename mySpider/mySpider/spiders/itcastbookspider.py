#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import ItcastBookItem


class ItcastBookSpider(scrapy.Spider):
    name = 'itcase_book_spider'
    allowd_domain = ["http://resource.boxuegu.com/"]
    start_urls = [
        "http://resource.boxuegu.com/booklist/",
    ]

    def parse(self, response):
        book_list = response.xpath('//div[@class="book-home-panel-book"]')

        bookItems = []

        for item in book_list:
            bookItem = ItcastBookItem()
            name = item.xpath('./div[@class="col-md-7"]/div/div/p[@class="book-list-s-title"]/a/text()').extract()
            version = item.xpath(
                './div[@class="col-md-7"]/div/div/p[@class="book-list-s-book-list-s-press"]/text()').extract()
            ISBN = item.xpath('./div[@class="col-md-7"]/div/div/p['
                              '@class="book-list-s-book-list-s-press"]/following-sibling::p[1]/text()').extract()
            price = item.xpath('./div[@class="col-md-7"]/p/span[@class="book-list-money"]/text()').extract()

            bookItem['name'] = name[0].encode("utf8")
            bookItem['version'] = version[0].encode("utf8")
            bookItem['ISBN'] = ISBN[0].encode("utf8")
            bookItem['price'] = price[0].encode("utf8")
            bookItems.append(bookItem)

        return bookItems
