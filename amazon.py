import scrapy
USER_AGENT="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    def __init__(self, category='', **kwargs):
        self.start_urls = [f"https://www.amazon.in/s?k={category}"]  # py36
        super().__init__(**kwargs)  # python3

    def parse(self, response):
        names = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").getall()
        #prices = response.xpath("//span[@class='a-price-whole']/text()").getall()
        #imgs = response.xpath("//img[@class='s-image']/@src").getall()
        c=len(names)
        for i in range(c):
            name = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").getall()
            #n.append(name)
            imgs = response.xpath("//img[@class='s-image']/@src").getall()
            prices = response.xpath("//span[@class='a-price-whole']/text()").getall()
            #p.append(prices)
            #im.append(imgs)
        for i in range(c):
            if name[i] and prices[i] and imgs[i]: 
                yield {
                    "shopping_site":"amazon", 
                    "product_name":name[i], 
                    "product_price":prices[i].replace(",", ""), 
                    "product_image":imgs[i]
                }

        names = response.xpath("//a[@class='a-link-normal a-text-normal']/text()").getall()
        prices = response.xpath("//span[@class='a-price-whole']/text()").getall()
        imgs = response.xpath("//img[@class='s-image']/@src").getall()
        print(names)
        print(imgs)
        print(prices)
        
        for i in range(len(names)):
            yield {
                "shopping_site":"amazon", 
                "product_name":names[i], 
                "product_price":int(prices[i].replace(",", "")), 
                "product_image":imgs[i]
            }
