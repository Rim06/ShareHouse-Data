# -*- coding: utf-8 -*-
import scrapy

from WebScraping.items import WebscrapingItem
from scrapy.selector import Selector

class LlcSpider(scrapy.Spider):
    name = 'llc'
    allowed_domains = ['llc-house.com']
    start_urls = (
        'http://llc-house.com/area/001',  #新宿エリア
        'http://llc-house.com/area/002',  #渋谷エリア
        'http://llc-house.com/area/003',  #六本木エリア
        'http://llc-house.com/area/004',  #上野エリア
        'http://llc-house.com/area/005',  #浅草エリア
        'http://llc-house.com/area/006',  #池袋エリア
        'http://llc-house.com/area/007',  #横浜エリア
        'http://llc-house.com/area/008',  #川崎エリア
        'http://llc-house.com/area/009',  #海外エリア
    )

    #物件情報一覧取得用
    xpathBukkenlistSplit = '//*[@class="llc-card-object mdl-card mdl-shadow--2dp"]'
    #物件詳細URL
    xpathBukkenUrl = 'a/@href'
    #物件名
    xpathBukkenName = '//h2[contains(@class, "llc-content-title")]/text()'
    #住所
    xpathaddress = 'table/tbody/tr[1]/td/text()'
    #契約形態
    xpathContractType = 'table/tbody/tr[2]/td/text()'
    #最寄り駅1
    xpathNearStation1 = 'table/tbody/tr[3]/td/text()'
    #家賃
    xpathRoomRent = 'table/tbody/tr[4]/td/text()'
    #紹介文
    xpathIntroduction = 'p[1]/text()'
    #家賃詳細
    xpathRoomRentDetails = 'p[2]/text()'


    #共有部設置物
    xpathCommonObject = 'ul[1]/text()'
    #特典
    xpathPrivilege = 'ul[2]/text()'
    #特徴
    xpathFeature = 'ul[3]/text()'

    def parse(self, response):
        global pageNo
        headerURL = "http://llc-house.com"

        #1件のデータはh2タグの単位でまとまってる -> h2タグを抽出
        article = WebscrapingItem()

        for d in response.xpath(self.xpathBukkenlistSplit):

            # h2 タグの中から必要な情報を抽出する
            url = headerURL + d.xpath(self.xpathBukkenUrl).extract_first()
            article['URL'] = url
            yield scrapy.Request(url, self.parse_detail)

    def parse_detail(self, response):

            buffRentDetails = ""
            buffCommonObject = ""
            buffPrivilege = ""
            buffFeature = ""

            sel = Selector(response)
            article = WebscrapingItem()

            article['物件名'] = self.check_none(response.xpath(self.xpathBukkenName).extract_first())

            accessList = sel.xpath('//div[@class="mdl-cell mdl-cell--6-col mdl-cell--4-col-tablet mdl-cell--4-col-phone mdl-typography--text-left"][1]')
            for outR in accessList:
                article['住所'] = self.check_none(outR.xpath(self.xpathaddress).extract_first())
                article['契約形態'] = self.check_none(outR.xpath(self.xpathContractType).extract_first())
                article['最寄り駅1'] = self.check_none(outR.xpath(self.xpathNearStation1).extract_first())
                article['家賃'] = self.check_none(outR.xpath(self.xpathRoomRent).extract_first())
                article['紹介文'] = self.check_none(outR.xpath(self.xpathIntroduction).extract_first())
                RentDetails = outR.xpath(self.xpathRoomRentDetails).extract()
                for listRentDetails in RentDetails:
                    buffRentDetails += self.check_none(listRentDetails) + "\n"
                    article['家賃詳細'] = buffRentDetails

            accessList = sel.xpath('//div[@class="mdl-cell mdl-cell--6-col mdl-cell--4-col-tablet mdl-cell--4-col-phone mdl-typography--text-left"][2]')
            for outR in accessList:
                article['共有部設置物'] = outR.xpath(self.xpathRoomRentDetails).extract()
                CommonObject = outR.xpath(self.xpathRoomRentDetails).extract()
                for listCommonObject in CommonObject:
                    buffCommonObject += self.check_none(listCommonObject) + "\n"
                    article['共有部設置物'] = buffCommonObject

                article['特典'] = self.check_none(outR.xpath(self.xpathPrivilege).extract_first())
                Privilege = outR.xpath(self.xpathPrivilege).extract()
                for listPrivilege in Privilege:
                    buffPrivilege += self.check_none(listPrivilege) + "\n"
                    article['特典'] = buffPrivilege

                article['特徴'] = self.check_none(outR.xpath(self.xpathFeature).extract_first())
                Feature = outR.xpath(self.xpathFeature).extract()
                for listFeature in Feature:
                    buffFeature += self.check_none(listFeature) + "\n"
                    article['特徴'] = buffFeature

            yield article

    def check_none(self,strObj):
        if strObj is None:
            return ""
        else:
            return strObj.strip().replace('\u3000', '')