# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

class WebScraperItem(scrapy.Item):
    # define the fields for your item here like:
    website_tables = scrapy.Field(
    	input_processor = MapCompose(remove_tags),
    	output_processor= TakeFirst()
    	)
    
