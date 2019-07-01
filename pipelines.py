# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import requests
import json


class NewsCrawlerPipeline(object):
    def __init__(self):
        self.create_conn()

    def create_conn(self):
        self.conn = sqlite3.connect("news.db")
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        if(item['headline'] is None or item['news'] is None):
            pass
        else:
            self.curr.execute('''insert into news('headline','news','image','tag') values (?,?,?,?)''', (
                item['headline'],
                item['news'],
                item['image'],
                item['tag']
            ))
            self.conn.commit()