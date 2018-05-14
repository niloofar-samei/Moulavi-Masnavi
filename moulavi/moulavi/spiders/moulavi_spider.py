import scrapy


class MoulaviSpider(scrapy.Spider):
	name = "moulavi"

	def start_requests(self):
		urls = ['https://ganjoor.net/moulavi/masnavi/daftar1/sh1/']
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		filename = 'moulavi.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)