import scrapy

from ..items import QuoteItem

class Quotespider(scrapy.Spider):
    name='quote'
    page_number=2
    start_urls=[
        'https://quotes.toscrape.com/login'
    ]
    def parse(self,response):
        token=response.css('form input::attr(value)').extract_first()
        print(token)

