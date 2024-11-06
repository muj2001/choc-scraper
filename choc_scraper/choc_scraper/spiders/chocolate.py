import scrapy
import re


class ChocolateSpider(scrapy.Spider):
    name = "chocolate"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]
    base_url = "https://www.chocolate.co.uk"

    def parse(self, response):
        products = response.css('product-item')

        for product in products:
            #here we put the data returned into the format we want to output for our csv or json file
            print("-" * 30)
            print(product.css('span.price').get())
            price = re.search(".\d+(\.\d+)?", product.css('span.price').get()).group()
            # print({
            #     'name' : product.css('a.product-item-meta__title::text').get(),
            #     'price' : price,
            #     'url' : product.css('div.product-item-meta a').attrib['href'],
            # })
            print(price)
            print("-" * 30)
            yield{
                'name' : product.css('a.product-item-meta__title::text').get(),
                'price' : price,
                'url' : self.base_url + product.css('div.product-item-meta a').attrib['href'],
            }

        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page:
            next_url = self.base_url + next_page
            yield response.follow(next_url, callback=self.parse)



