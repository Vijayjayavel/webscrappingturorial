import scrapy

from scrapy.crawler import CrawlerProcess
from ..items import QuoteItem

class Quotespider(scrapy.Spider):
    name='quote'
    page_number=2
    start_urls=[
        'https://quotes.toscrape.com/page/1/'
    ]
    def parse(self,response):

        Items=QuoteItem()

        all_div_quote=response.css('div.quote')
        for quote in all_div_quote:
            title=quote.css('span.text::text').extract()
            author=quote.css('.author::text').extract()
            tags=quote.css('.tag::text').extract()

            Items['title']=title
            Items['author']=author
            Items['tags']=tags
            yield Items

            next_page='https://quotes.toscrape.com/page/'+str(Quotespider.page_number)+'/'
            if Quotespider.page_number<11:
                Quotespider.page_number+=1
                yield response.follow(next_page,callback=self.parse)

