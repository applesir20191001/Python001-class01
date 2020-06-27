# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
class MaoyanmoviePipeline:
#    def process_item(self, item, spider):
#        return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
     def process_item(self, item, spider):
         movie_name = item['movie_name']
         movie_type = item['movie_type']
         movie_time = item['movie_time']
         output = f'|{movie_name}|\t|{movie_type}|\t|{movie_time}|\n\n'
         with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
             article.write(output)
             #article.close()
         return item
