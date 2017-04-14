# coding: utf-8
import scrapy
from scrapy.item import Item,Field
class ReverseItem(scrapy.Item):
    #defining the fields for items
    name=Field()
    link=Field()
    field=Field()
    dept=Field()
    email=Field()
    image_src=Field()
    
