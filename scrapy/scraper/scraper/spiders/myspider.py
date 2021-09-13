import scrapy
import os, sys

# p = os.path.abspath('..')
# sys.path.insert(1, p)

# import items
#from scraper import items
from scraper.items import Post

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['localhost']
    start_urls=['http://localhost:8000/post/1',]

    def parse(self, response):
        SET_SELECTOR='//div[@class="post"]'
        NEXT_PAGE='div.post h2 a.next-page::attr(href)'

        i = response.xpath(SET_SELECTOR)
        item = Post()
        item['product_url'] = response.url
        item['title'] = i.xpath('.//h1/text()').get(),
        item['date'] = i.xpath('.//div[@class="date"]/text()').get(),
        item['text'] = i.xpath('.//p[@class="main-text-blog"]/text()').get(),
        yield item

        next_page=response.css(NEXT_PAGE).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page), callback=self.parse
            )
