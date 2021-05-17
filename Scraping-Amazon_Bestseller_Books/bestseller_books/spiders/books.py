import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/gp/bestsellers/books']

    def parse(self, response):
        for product in response.xpath("//ol[@class='a-ordered-list a-vertical']/li"):
            yield {
                #'title': product.xpath("normalize-space(.//div[@class='p13n-sc-truncate p13n-sc-line-clamp-1 p13n-sc-truncate-desktop-type2']/text())").get(),
                #'title': product.xpath(".//div[@class='p13n-sc-truncate-desktop-type2 p13n-sc-truncated']/text()").get(),
                						 
                'Title': product.xpath(".//div[@class='a-section a-spacing-small']/img/@alt").get(),														 
                'Rankings': product.xpath(".//span[@class='zg-badge-text']/text()").get(),
                'Url': response.urljoin(product.xpath(".//span[@class='aok-inline-block zg-item']/a/@href").get()),
                'Ratings': product.xpath(".//span[@class='a-icon-alt']/text()").get(),
                'Price': product.xpath(".//span/span[@class='p13n-sc-price']/text()").get(),
                'Img': product.xpath("//div[@class='a-section a-spacing-small']/img/@src").get() 
                 
            }

        next_page = response.xpath("//li[@class='a-last']/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
