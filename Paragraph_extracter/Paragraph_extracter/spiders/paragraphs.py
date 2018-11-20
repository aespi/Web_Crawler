# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy import Spider

from Paragraph_extracter.items import paraItem
class paragraphs(CrawlSpider):
    name = "paragraphs"
    #allowed_domains = [""]

    def __init__(self, url='', **kwargs):
        self.start_urls = [url]
        super().__init__(**kwargs)

    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)
    def parse_page(self, response):
        sep=' || '                                              #specifies the seperator of paragraphs in JSON file.
        for resp in response.url:                               #to goto each page and subpage in the website
            p_tag = response.xpath('//p')                       #filters out all the p tags
            content = p_tag.xpath('.//text()').extract()        #to extract only the text in the <p> tags </p>
            item = paraItem()
            item['page'] = response.url                         # to enter the URL of the page it currently crawling
            item['content'] = sep.join(list(map(str.strip, list(filter(str.strip, content)))))      #changes the list to string, removes /n from each element in list, remove null values in list.
            yield item
            break
