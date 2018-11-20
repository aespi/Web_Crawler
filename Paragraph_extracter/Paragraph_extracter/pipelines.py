# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
class ParagraphExtracterPipeline(object):
    def open_spider(self, spider):
        self.file = open('scraped_items.json', 'w')
        self.file.write("{\n")
        self.file.write("\t\"Pages\": [\n\t")

    def close_spider(self, spider):
        self.file.write("\t [\n")
        self.file.write("}")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(
            dict(item),
            indent = 4,
            separators = (',\n', ': ')
        ) + "\n\t"
        self.file.write(line)
        return item
