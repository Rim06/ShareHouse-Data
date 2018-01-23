# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from scrapy.http.request import Request
# from WebScraping.items import WebscrapingItem
#
# class FooSpider(BaseSpider):
#     name = "hoge"
#     allowed_domains = ["hoge.org"]
#     start_urls = ["http://www.geocities.jp/little_gate/01-06-01.htm"]
#
#     def parse(self, response):
#         hxs = HtmlXPathSelector(response)
#
#         item = WebscrapingItem()
#         image_urls = hxs.select('//img/@src').extract()
#         item['image_urls'] = ['http://www.geocities.jp/little_gate/'+x for x in image_urls]
#         return item