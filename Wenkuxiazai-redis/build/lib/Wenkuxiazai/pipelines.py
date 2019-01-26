# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WenkuxiazaiPipeline(object):
    def process_item(self, item, spider):
        return item

import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri=mongo_uri
        self.mongo_db=mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri= crawler.settings.get('MONGO_URI'),
            mongo_db= crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        # name = item.__class__.__name__
        try:
            name="wenkuxiazaiwang_data"
            self.db[name].insert(dict(item))
            print("插入成功")
            return item
        except:
            print("重复数据")

    def close_spider(self,spider):
        self.client.close()