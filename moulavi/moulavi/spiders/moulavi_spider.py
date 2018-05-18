import scrapy


class MoulaviSpider(scrapy.Spider):
	name = "moulavi"

	def start_requests(self):
		start_urls = [
			'https://ganjoor.net/moulavi/masnavi/daftar1/sh1/',
			'https://ganjoor.net/moulavi/masnavi/daftar1/sh2/',
		]
		for url in start_urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for line in response.css('div.b'):
			yield {
				'title': response.css('h2 a::text').extract(),
				'right_column': line.css('div.m1').extract(),
				'left_column': line.css('div.m2').extract(),
			}
