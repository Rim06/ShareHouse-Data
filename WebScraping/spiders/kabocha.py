# -*- coding: utf-8 -*-
import scrapy

from WebScraping.items import kabochaItem
from scrapy.selector import Selector

pageNo = 2

class KabochaSpider(scrapy.Spider):
    name = 'kabocha'
    allowed_domains = ['kabocha-b.jp']
    start_urls = (
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=1',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=2',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=3',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=4',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=5',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=6',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=7',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=8',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=9',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=10',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=11',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=12',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=13',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=14',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=15',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=16',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=17',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=18',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=19',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=20',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=21',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=22',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=23',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=24',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=25',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=26',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=27',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=28',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=29',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=30',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=31',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=32',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=33',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=34',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=35',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=36',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=37',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=38',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=39',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=40',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=41',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=42',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=43',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=44',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=45',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=46',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=47',
        'https://www.kabocha-b.jp/search/index/?class[]=c1&pg=48',
    )
    headURL = "https://www.kabocha-b.jp/"
    url = ""

    # タイトル
    xpathTitle = '//*[@id="bkntitle"]/text()'
    # 賃料
    xpathTinryo = '//*[@class="price border"]/span/text()'
    # 共益費
    xpathKyouekihi = '//*[@class="price border"]/span[2]/text()'
    # 敷金/礼金
    xpathShirei = '//th[contains(text(), "敷金")]/following-sibling::td[1]/text()'
    # 最寄駅
    xpathEki = '//th[contains(text(), "最寄駅")]/following-sibling::td[1]/text()'
    # 仲介手数料
    xpathTyukairyo = '//th[contains(text(), "仲介手数料")]/following-sibling::td[1]/text()'
    # 保証料
    xpathHosyouryo = '//th[contains(text(), "保証料")]/following-sibling::td[1]/text()'
    # 築年
    xpathTikunen = '//th[contains(text(), "築年")]/following-sibling::td[1]/text()'
    # 水光熱費
    xpathSuikounetu = '//th[contains(text(), "水光熱費")]/following-sibling::td[1]/text()'
    # 住所
    xpathJyusyo = '//th[contains(text(), "住所")]/following-sibling::td[1]/p/text()'
    # 専有面積
    xpathSenyumenseki = '//th[contains(text(), "専有面積")]/following-sibling::td[1]/text()'
    # インターネット
    xpathNet = '//th[contains(text(), "インターネット")]/following-sibling::td[1]/text()'
    # アクセス
    xpathAkusesu = '//th[contains(text(), "参考")]/following-sibling::td[1]/text()'
    # 構造
    xpathKouzo ='//th[contains(text(), "構造")]/following-sibling::td[1]/text()'
    # 戸数
    xpathTosu = '//th[contains(text(), "戸数")]/following-sibling::td[1]/text()'
    # 入居条件
    xpathNyukyo = '//th[contains(text(), "入居条件")]/following-sibling::td[1]/text()'
    # サポート巡回/掃除
    xpathSapoto = '//th[contains(text(), "サポート巡回")]/following-sibling::td[1]/text()'
    # セキュリティ
    xpathSekyu = '//th[contains(text(), "セキュリティ")]/following-sibling::td[1]/text()'
    # ルームクリーニング料
    xpathRoomclean = '//th[contains(text(), "ルームクリーニング料")]/following-sibling::td[1]/text()'
    # 家財保証料
    xpathKazaihosyo = '//th[contains(text(), "家財保証")]/following-sibling::td[1]/text()'
    # 鍵交換料
    xpathKeykoukan = '//th[contains(text(), "鍵交換料")]/following-sibling::td[1]/text()'
    # 家具・家電
    xpathKagukaden = '//th[contains(text(), "家具・家電")]/following-sibling::td[1]/text()'
    # 備考
    xpathBikou = '//*[@id="bknarticle"]/div[4]/dl[5]/dd/text()'

    def parse(self, response):

        #1件のデータはh2タグの単位でまとまってる -> h2タグを抽出
        for d in response.xpath('//*[@id="main"]/div[contains(@class, "list_area")]'):

            # h2 タグの中から必要な情報を抽出する
            self.url = self.headURL + d.xpath('div/div[3]/div[2]/ul/li[1]/a/@href').extract_first()
            yield scrapy.Request(self.url, self.parse_detail)
            return

    def parse_detail(self, response):

            sel = Selector(response)
            article = kabochaItem()
            article['URL'] = self.url
            article['タイトル'] = self.check_none(response.xpath(self.xpathTitle).extract_first())
            article['賃料'] = response.xpath(self.xpathTinryo).extract_first()
            article['共益費'] = self.check_none(response.xpath(self.xpathKyouekihi).extract_first())
            article['敷金_礼金'] = response.xpath(self.xpathShirei).extract()
            article['最寄駅'] =  self.check_none(response.xpath(self.xpathEki).extract_first())
            article['仲介手数料'] = self.check_none(response.xpath(self.xpathTyukairyo).extract_first())
            article['保証料'] = self.check_none(response.xpath(self.xpathHosyouryo).extract_first())
            article['築年'] = self.check_none(response.xpath(self.xpathTikunen).extract_first())
            article['水光熱費'] = self.check_none(response.xpath(self.xpathSuikounetu).extract_first())
            article['住所'] = self.check_none(response.xpath(self.xpathJyusyo).extract_first())
            article['専有面積'] = self.check_none(response.xpath(self.xpathSenyumenseki).extract_first())
            article['インターネット'] = self.check_none(response.xpath(self.xpathNet).extract_first())
            article['アクセス'] = response.xpath(self.xpathAkusesu).extract()
            article['構造'] = self.check_none(response.xpath(self.xpathKouzo).extract_first())
            article['戸数'] = self.check_none(response.xpath(self.xpathTosu).extract_first())
            article['入居条件'] = self.check_none(response.xpath(self.xpathNyukyo).extract_first())
            article['サポート巡回_掃除'] = self.check_none(response.xpath(self.xpathSapoto).extract_first())
            article['セキュリティ'] = self.check_none(response.xpath(self.xpathSekyu).extract_first())
            article['ルームクリーニング料'] = self.check_none(response.xpath(self.xpathRoomclean).extract_first())
            article['家財保証料'] = self.check_none(response.xpath(self.xpathKazaihosyo).extract_first())
            article['鍵交換料'] = self.check_none(response.xpath(self.xpathKeykoukan).extract_first())
            article['家具_家電'] = self.check_none(response.xpath(self.xpathKagukaden).extract_first())
            # article['各居室設備'] = self.check_none(response.xpath(self.xpathKakusetubi).extract_first())
            # article['共同設備'] = self.check_none(response.xpath(self.xpathKyoudousetubi).extract_first())
            article['備考'] = response.xpath(self.xpathBikou).extract()

            yield article

    def check_none(self,strObj):
        if strObj is None:
            return ""
        else:
            return strObj.strip().replace('\u3000', '')