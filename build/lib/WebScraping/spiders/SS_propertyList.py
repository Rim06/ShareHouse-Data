# -*- coding: utf-8 -*-
import scrapy

from WebScraping.items import ShareshareListItem

rootPath = 'http://share-share.jp'

class SsPropertylistSpider(scrapy.Spider):
    name = 'SS_propertyList'
    allowed_domains = ['share-share.jp']
    start_urls = ['http://share-share.jp/search/result/page=1']

    def parse(self, response):

        # 1件のデータはtrタグの単位でまとまってる -> trタグを抽出
        for d in response.css("div.result-list > table > tbody > tr"):

            article = ShareshareListItem()
            # tr タグの中から必要な情報を抽出する
            article['title']  = d.css("td > div > h3 > a::text").extract_first()
            article['url'] = rootPath + d.css("td > div > h3 > a::attr('href')").extract_first()

            yield article

        next_page = response.css("div.pager >  ul > li.next > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse)
