# -*- coding: utf-8 -*-
import scrapy

from WebScraping.items import shareshareItem
from scrapy.selector import Selector

rootPath = 'http://share-share.jp'

class shareshareSpider(scrapy.Spider):
    name = "share_share"
    allowed_domains = ["share-share.jp"]

    start_urls = (
        'http://share-share.jp/search/result/?limit=100&page=1',
    )

    def parse(self, response):

        # 1件のデータはtrタグの単位でまとまってる -> trタグを抽出
        for d in response.css("div.result-list > table > tbody > tr"):

            article = shareshareItem()
            # tr タグの中から必要な情報を抽出する
            url = rootPath + d.css("td > div > h3 > a::attr('href')").extract_first()
            yield scrapy.Request(response.urljoin(url), self.parse_detail)

        next_page = response.css("div.pager >  ul > li.next > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):

            sel = Selector(response)
            article = shareshareItem()

            article['title'] = response.xpath('//div[@class="head head-house-detail"]/h1/text()').extract()
            article['catch_copy'] = response.xpath('//div[@class="descriptions"]/h3/text()').extract()
            article['introduction'] = response.xpath('//div[@class="descriptions"]/p/text()').extract()

            # 物件基本情報テーブル抽出
            article['adr_prefecture'] = response.xpath('//div[@class="section-house-detail-info section-house-detail-basic"]/div[@class="inner"]/table/tbody/tr[1]/td[1]/text()').extract()
            article['access'] = response.xpath('//div[@class="section-house-detail-info section-house-detail-basic"]/div[@class="inner"]/table/tbody/tr[1]/td[2]/text()').extract()
            article['terms'] = response.xpath('//div[@class="section-house-detail-info section-house-detail-basic"]/div[@class="inner"]/table/tbody/tr[2]/td/text()').extract()
            article['Share_living'] = response.xpath('//div[@class="section-house-detail-info section-house-detail-shared-equipments"]/div[@class="inner"]/table/tbody/tr[1]/td[1]/text()').extract()

            # 共有設備テーブル抽出
            equipments = sel.xpath('//div[@class="section-house-detail-info section-house-detail-shared-equipments"]/div[@class="inner"]/table/tbody/tr')

            outCnt = 0
            for outE in equipments:
                if outCnt == 0:
                    article['Share_living'] = outE.xpath('td[1]/text()').extract() + outE.xpath('td[1]/div/text()').extract()
                    article['Share_kitchen'] = outE.xpath('td[2]/text()').extract() + outE.xpath('td[2]/div/text()').extract()
                elif outCnt == 1:
                    article['Share_bathroom'] = outE.xpath('td[1]/text()').extract() + outE.xpath('td[1]/div/text()').extract()
                    article['Share_toilet'] = outE.xpath('td[2]/text()').extract() + outE.xpath('td[2]/div/text()').extract()
                elif outCnt == 2:
                    article['Share_washing'] = outE.xpath('td[1]/text()').extract() + outE.xpath('td[1]/div/text()').extract()
                    article['Share_dryer'] = outE.xpath('td[2]/text()').extract() + outE.xpath('td[2]/div/text()').extract()
                elif outCnt == 3:
                    article['Share_PC'] = outE.xpath('td[1]/text()').extract() + outE.xpath('td[1]/div/text()').extract()
                    article['Share_internet'] = outE.xpath('td[2]/text()').extract() + outE.xpath('td[2]/div/text()').extract()
                elif outCnt == 4:
                    article['Share_parking'] = outE.xpath('td[1]/text()').extract() + outE.xpath('td[1]/div/text()').extract()
                    article['Share_bicycleP'] = outE.xpath('td[2]/text()').extract() + outE.xpath('td[2]/div/text()').extract()
                elif outCnt == 5:
                    article['Share_etc'] = outE.xpath('td/text()').extract() + outE.xpath('td/div/text()').extract()
                outCnt = outCnt + 1

            admin = sel.xpath('//div[@class="section-house-detail-info section-house-detail-admin"]/div[@class="inner"]/table/tbody/tr')

            outCnt = 0
            for outA in admin:
                if outCnt == 0:
                    article['mgt_style'] = outA.xpath('td[1]/text()').extract()
                    article['mgt_cleaning'] = outA.xpath('td[2]/text()').extract()
                elif outCnt == 1:
                    article['mgt_rule'] = outA.xpath('td[1]/text()').extract()
                    article['mgt_event'] = outA.xpath('td[2]/text()').extract()
                outCnt = outCnt + 1
            yield article
