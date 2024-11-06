import scrapy


class ChocolateSpider(scrapy.Spider):
    name = "chocolate"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        pass
