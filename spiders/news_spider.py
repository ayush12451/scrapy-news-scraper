import scrapy

class TechNewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    news = scrapy.Field()
    image = scrapy.Field()
    tag = scrapy.Field()

class AutoNewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    news = scrapy.Field()
    image = scrapy.Field()
    tag = scrapy.Field()

class GenNewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    news = scrapy.Field()
    image = scrapy.Field()
    tag = scrapy.Field()

class TechSpider(scrapy.Spider):
    name = "tech_news"

    def start_requests(self):
        urls = [
            'http://gadgets.ndtv.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.url_resolver)

    def url_resolver(self, response):
        news_urls = response.css("div.recent_news_widget li a::attr(href)").getall()
        for url in news_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = TechNewsCrawlerItem()

        headline = response.css("div.lead_heading h1::text").get()
        news = ''.join(response.css("div.content_text p *::text").getall())
        image = response.css("div.fullstoryImage picture img::attr(src)").get()
        tag = 'tech'

        item['headline'] = headline
        item['news'] = news
        item['image'] = image
        item['tag'] = tag

        yield item

class AutoSpider(scrapy.Spider):
    name = "auto_news"

    def start_requests(self):
        urls = [
            'https://auto.ndtv.com/news',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.url_resolver)

    def url_resolver(self, response):
        news_urls = response.css("div.blog-card a.blog-card__cover::attr(href)").getall()
        for url in news_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        item = AutoNewsCrawlerItem()
        headline = response.css("div.h__mb10 h1::text").get()
        news = ''.join(response.css("div.article__content p *::text").getall())
        image = response.css("div.article__main a.article-gallery__img img::attr(src)").get()
        tag = 'auto'

        item['headline'] = headline
        item['news'] = news
        item['image'] = image
        item['tag'] = tag

        yield item

class GeneralSpider(scrapy.Spider):
    name = "general_news"

    def start_requests(self):
        urls = [
            'https://www.ndtv.com/latest?pfrom=home-mainnavgation',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.url_resolver)

    def url_resolver(self, response):
        news_urls = response.css("div.new_storylising li div.nstory_header a::attr(href)").getall()
        for url in news_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        item = GenNewsCrawlerItem()
        headline = response.css("div.ins_headline h1 span::text").get()
        news = ''.join(response.css("div.ins_storybody p *::text").getall())
        image = response.css("div.ins_mainimage_big img::attr(src)").get()
        tag = 'general'

        item['headline'] = headline
        item['news'] = news
        item['image'] = image
        item['tag'] = tag

        yield item