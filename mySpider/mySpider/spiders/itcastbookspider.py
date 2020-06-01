#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import ItcastBookItem


class ItcastBookSpider(scrapy.Spider):
    name = 'itcase_book_spider'
    allowd_domain = ["resource.boxuegu.com/"]
    start_urls = [
        "http://resource.boxuegu.com/booklist/find.html",
    ]

    def parse(self, response):
        book_list = response.xpath('//div[@class="row"]')
        bookItems = []
        print(book_list)

        for item in book_list:

            bookItem = ItcastBookItem()
            name = item.xpath('./div[2]/p[@class="book-list-s-title"]/a/text()').extract()
            version = item.xpath('./div[2]/p[@class="book-list-s-press"]/text()').extract()
            ISBN = item.xpath('./div[2]/p[@class="book-list-s-isbn"]/text()').extract()
            price = item.xpath('./div[4]/p/span[@class="book-list-money"]/text()').extract()

            bookItem['name'] = name[0].encode("utf8")
            bookItem['version'] = version[0].encode("utf8")
            bookItem['ISBN'] = ISBN[0].encode("utf8")
            if len(price) == 0:
                bookItem['price'] = ""
                bookItems.append(bookItem)
                continue
            bookItem['price'] = price[0].encode("utf8")
            bookItems.append(bookItem)

        return bookItems
