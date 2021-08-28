import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    def __init__(self, category='', **kwargs):
        self.start_urls = [f"https://www.amazon.in/s?k={category}"]  # py36
        super().__init__(**kwargs)  # python3

    def parse(self, response):
        names = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").getall()
        prices = response.xpath("//span[@class='a-price-whole']/text()").getall()
        imgs = response.xpath("//img[@class='s-image']/@src").getall()
        for i in range(len(names)):
            yield {
                "shopping_site":"amazon", 
                "product_name":names[i], 
                "product_price":prices[i].replace("\u20b9", ""), 
                "product_image":imgs[i]
            }

        names = response.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/text()").getall()
        prices = response.xpath("//span[@class='a-price-whole']/text()").getall()
        imgs = response.xpath("//img[@class='s-image']/@src").getall()
        print(names)
        print(imgs)
        print(prices)
        
        for i in range(len(names)):
            B=yield {
                "shopping_site":"amazon", 
                "product_name":names[i], 
                "product_price":prices[i].replace("\u20b9", ""), 
                "product_image":imgs[i]
            }
        return B
