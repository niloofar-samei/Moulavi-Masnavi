import scrapy


class MoulaviSpider(scrapy.Spider):
	name = "moulavi"
	start_urls = ['https://ganjoor.net/moulavi/masnavi/daftar1/sh1/']

	def parse(self, response):
		for line in response.css('div.b'):
			yield {
				'right_column': line.css('p::text').extract(),
			}


"""
import scrapy


class MoulaviSpider(scrapy.Spider):
	name = "moulavi"
	start_urls = ['https://ganjoor.net/moulavi/masnavi/daftar1/sh1/']

	def parse(self, response):
		for line in response.css('div.b'):
			yield {
				'right_column': line.css('div.m1::text').extract_first(),
			}
"""