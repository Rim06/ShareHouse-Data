# -*- coding: utf-8 -*-
import scrapy

from WebScraping.items import WebscrapingItem
from scrapy.selector import Selector

pageNo = 1

class SharepareSpider(scrapy.Spider):
    name = 'sharepare'
    allowed_domains = ['sharepare.jp']
    start_urls = ['http://sharepare.jp/?t=house&s=search&page=0']
    url = "abc"

    #物件情報一覧取得用
    xpathBukkenlistSplit = '//div[contains(@class, "title-result")]'
    #物件詳細URL
    xpathBukkenUrl = 'h2/a/@href'
    #物件名
    xpathBukkenName = '//div[contains(@class, "name-deltal")]/h1/span/text()'
    #共益費
    xpathCommonCost = '//h3[contains(text(), "共益費")]/parent::td/following-sibling::td/text()'
    #保証金
    xpathDeposit = '//h3[contains(text(), "デポジット")]/parent::td/following-sibling::td/text()'
    #部屋数
    xpathRoomCnt = '//h3[contains(text(), "部屋数")]/parent::td/following-sibling::td/text()'
    #管理会社名
    xpathMgtCompany = '//div[contains(@class, "columnContent clear")]/div/div/h3/text()'
    #緯度経度
    xpathL_L = '//a[contains(@href, "maps.google")]'
    #最寄り駅1
    xpathNearStation1 = 'li[1]/text()'
    #最寄り駅2
    xpathNearStation2 = 'li[2]/text()'
    #最寄り駅3
    xpathNearStation3 = 'li[3]/text()'
    # キャッチコピー
    xpathCatchCopy = '//div[contains(@class, "house_description")]/div/p/text()'
    # 照会文
    xpathIntroduction = '//div[contains(@class, "box_content")]/p[contains(@class, "description")]/text()'
    # タバコに関して
    xpathTabacco = '//td[contains(text(), "タバコ")]/following-sibling::td[1]/text()'
    # リビング
    xpathShareLiving = '//td[contains(text(), "リビング")]/following-sibling::td/text()'
    # キッチン
    xpathSharekitchen = '//td[contains(text(), "キッチン")]/following-sibling::td/text()'
    # 浴室
    xpathShareBathroom = '//td[contains(text(), "浴室")]/following-sibling::td/text()'
    # トイレ
    xpathShareToilet = '//td[contains(text(), "トイレ")]/following-sibling::td/text()'
    # 洗濯機
    xpathShareWashing = '//td[contains(text(), "洗濯機")]/following-sibling::td/text()'
    # ポスト
    xpathSharePost = '//td[contains(text(), "ポスト")]/following-sibling::td/text()'
    # インターネット
    xpathShareInternet = '//td[contains(text(), "インターネット")]/following-sibling::td/text()'
    # 駐輪場
    xpathShareBicycleP = '//td[contains(text(), "駐輪場")]/following-sibling::td/text()'
    # 駐車場
    xpathShareParkingLot = '//td[contains(text(), "駐車場")]/following-sibling::td/text()'
    # キャッチコピー
    xpathCatchCopy = '//div[@class="intro"]/p/text()'
    # 紹介文
    xpathIntroduction = '//*[@id="houseInfomationsTab01"]/div/div/div/p/text()'
    # 共有部の清掃
    xpathShareCleaning = '//td[contains(text(), "掃除")]/following-sibling::td[1]/text()'
    # ルール
    xpathRule = '//td[contains(text(), "ルール")]/following-sibling::td[1]/text()'
    # 周辺情報
    xpathNearbyInfo = '//*[@id="areaEquipmentMetas"]/text()'
    # キャンペーン情報
    xpathCampaign = '//*[@class="page2-h62"]/text()'


    def parse(self, response):
        global pageNo

        #1件のデータはh2タグの単位でまとまってる -> h2タグを抽出
        article = WebscrapingItem()
        for d in response.xpath(self.xpathBukkenlistSplit):

            # h2 タグの中から必要な情報を抽出する
            self.url = d.xpath(self.xpathBukkenUrl).extract_first()
            yield scrapy.Request(self.url, self.parse_detail)

        next_page = "http://sharepare.jp/?t=house&s=search&page="+ str(pageNo)
        if pageNo == 32:
            return
        else:
            pageNo += 1
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):

            buffI = ""
            buffN = ""

            sel = Selector(response)
            article = WebscrapingItem()
            article['URL'] = self.url
            article['物件名'] = self.check_none(response.xpath(self.xpathBukkenName).extract_first())
            article['敷金'] = response.xpath('//*[@id="houseSummary"]/section/div/div[2]/div[4]/div/div[2]/div[1]/h3/span/span[1]/text()').extract_first()

            article['管理会社名'] = self.check_none(response.xpath(self.xpathMgtCompany).extract_first())
            article['緯度経度'] = self.check_none(response.xpath(self.xpathL_L).extract_first())
            article['共益費'] = self.check_none(response.xpath(self.xpathCommonCost).extract_first())
            article['敷金'] = self.check_none(response.xpath(self.xpathDeposit).extract_first())
            article['部屋数'] = self.check_none(response.xpath(self.xpathRoomCnt).extract_first())

            article['タバコ'] = self.check_none(response.xpath(self.xpathTabacco).extract_first())

            accessList = sel.xpath('//ul[contains(@class, "accessList")]')
            for outR in accessList:
                article['最寄り駅1'] = self.check_none(outR.xpath(self.xpathNearStation1).extract_first())
                article['最寄り駅2'] = self.check_none(outR.xpath(self.xpathNearStation2).extract_first())
                article['最寄り駅3'] = self.check_none(outR.xpath(self.xpathNearStation3).extract_first())

            article['リビング'] = self.check_none(response.xpath(self.xpathShareLiving).extract_first())
            article['キッチン'] = self.check_none(response.xpath(self.xpathSharekitchen).extract_first())
            article['浴室'] = self.check_none(response.xpath(self.xpathShareBathroom).extract_first())
            article['トイレ'] = self.check_none(response.xpath(self.xpathShareToilet).extract_first())
            article['洗濯機'] = self.check_none(response.xpath(self.xpathShareWashing).extract_first())
            article['ポスト'] = self.check_none(response.xpath(self.xpathSharePost).extract_first())
            article['インターネット'] = self.check_none(response.xpath(self.xpathShareInternet).extract_first())
            article['駐輪場'] = self.check_none(response.xpath(self.xpathShareBicycleP).extract_first())
            article['駐車場'] = self.check_none(response.xpath(self.xpathShareParkingLot).extract_first())
            article['キャッチコピー'] = self.check_none(response.xpath(self.xpathCatchCopy).extract_first())

            listIntroduction = response.xpath(self.xpathIntroduction).extract()
            for listI in listIntroduction:
                buffI += self.check_none(listI) + "\n"
            article['紹介文'] = buffI

            article['共有部の清掃'] = self.check_none(response.xpath(self.xpathShareCleaning).extract_first())
            article['ルール'] = self.check_none(response.xpath(self.xpathRule).extract_first())

            listNearbyInfo = response.xpath(self.xpathNearbyInfo).extract()
            for listN in listNearbyInfo:
                buffN += self.check_none(listN) + "\n"
            article['周辺情報'] = buffN

            article['キャンペーン情報'] = self.check_none(response.xpath(self.xpathCampaign).extract_first())

            yield article

    def check_none(self,strObj):
        if strObj is None:
            return ""
        else:
            return strObj.strip().replace('\u3000', '')
