# coding: utf-8
import scrapy
from scrapy.item import Item,Field
class ReverseItem(scrapy.item):
    defining the fields for items:
class ReverseItem(scrapy.Item):
    #defining the fields for items
    name=Field()
    link=Field()
    dept=Field()
    email=Field()
    image_src=Field()
    
