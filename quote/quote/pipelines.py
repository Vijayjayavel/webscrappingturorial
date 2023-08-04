# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotePipeline:

    def __int__(self):
        self.make_connection()
        self.createtable()
        pass
    def make_connection(self):
        self.conn=sqlite3.Connection('quotes.db')
        self.curr=self.conn.cursor()

    def createtable(self):
        self.curr.execute('''drop table if exists sample''')
        self.curr.execute('''create table sample(title varchar(50),author varchar(50),tag varchar(100))''')
    def process_item(self, item, spider):
        self.store_db(item)
        print('pipline:'+item['title'][0])
        return item

    def store_db(self):
        self.curr.execute(""" INSERT INTO sample VALUES (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0],
        ))
        self.conn.commit()

