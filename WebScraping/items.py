# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class WebscrapingItem(Item):
    URL = Field()
    物件名 = Field() #物件名
    管理会社名 = Field() #管理会社名
    住所 = Field() #住所
    緯度経度 = Field() #緯度経度
    最寄り駅1 = Field() #最寄り駅1
    最寄り駅2 = Field() #最寄り駅2
    最寄り駅3 = Field() #最寄り駅3
    キャッチコピー = Field() #キャッチコピー
    紹介文 = Field() #紹介文
    部屋数 = Field() #部屋数
    管理人の有無 = Field() #管理人の有無
    タバコ = Field() #タバコに関して
    リビング = Field() #リビング
    キッチン = Field()  # キッチン
    浴室 = Field()  # 浴室
    洗濯機 = Field()  # 洗濯機
    トイレ = Field()  # トイレ
    ポスト = Field()  # ポスト
    インターネット = Field()  # インターネット
    駐輪場 = Field()  # 駐輪場
    駐車場 = Field()  # 駐車場
    共有部の清掃 = Field() #共有部の清掃
    ルール = Field() #ルール
    周辺情報 = Field() #周辺情報
    敷金 = Field() #敷金
    礼金 = Field() #礼金
    保証金 = Field() #保証金
    契約形態 = Field() #契約形態
    再契約_更新時の費用 = Field() #再契約_更新時の費用
    保証人の有無 = Field() #保証人の有無
    保証人の有無_注意文言 = Field() #保証人の有無_注意文言
    費用関連_その他文言 = Field() #費用関連_その他文言
    共益費 = Field() #共益費

    #シェアパレード独自
    キャンペーン情報 = Field() #キャンペーン情報

    #LLC独自
    特典 = Field()  # 特典
    特徴 = Field()  # 特徴
    家賃 = Field()  # 家賃
    家賃詳細 = Field()  # 家賃詳細
    共有部設置物 = Field()  # 共有部設置物

    title = Field()
    url = Field()

    image_urls = Field()
    images = Field()

class shareshareItem(Item):
    title = Field()
    catch_copy = Field()
    introduction = Field()
    adr_prefecture = Field()
    adr_municipality = Field()
    access = Field()
    terms = Field()
    Share_living = Field()
    Share_kitchen = Field()
    Share_bathroom = Field()
    Share_toilet = Field()
    Share_washing = Field()
    Share_dryer = Field()
    Share_PC = Field()
    Share_internet = Field()
    Share_parking = Field()
    Share_bicycleP = Field()
    Share_etc = Field()
    mgt_style = Field()
    mgt_cleaning = Field()
    mgt_rule = Field()
    mgt_event = Field()

class ShareshareListItem(Item):
    title = Field()
    url = Field()

class kabochaItem(Item):
    タイトル = Field()
    URL = Field()
    賃料 = Field()
    共益費 = Field()
    敷金_礼金 = Field()
    最寄駅 = Field()
    仲介手数料 = Field()
    保証料 = Field()
    築年 = Field()
    水光熱費 = Field()
    住所 = Field()
    専有面積 = Field()
    インターネット = Field()
    アクセス = Field()
    構造 = Field()
    戸数 = Field()
    入居条件 = Field()
    サポート巡回_掃除 = Field()
    セキュリティ = Field()
    ルームクリーニング料 = Field()
    家財保証料 = Field()
    鍵交換料 = Field()
    家具_家電 = Field()
    各居室設備 = Field()
    共同設備 = Field()
    備考 = Field()