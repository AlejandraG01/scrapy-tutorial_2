import scrapy

class ProductBuscapeSpider(scrapy.Spider):
   name = "product-buscape"
   start_urls = ['http://www.buscape.com.br/mais-vendidos/livros/administracao-e-negocios/677353G?pagina='+str(i) for i in range(1, 7)]

   
   def parse(self, response):
       self.logger.info('Hi, this is my item pages! %s', response.url)
       l =  ItemLoader(item=Product(), response=response)
       l.add_css('title','div.details div.description a.link div.is-truncated p.name-prd::text')
       l.add_css('author','div.details span.carac.carac-autor a.info::text')
       l.add_css('price','div.price-range a::attr(title)')
       yield l.load_Item()
       
       
   """    for name in response.css('.details'):
           yield {
                     'title': name.css('div.description a.link div.is-truncated p.name-prd::text').extract_first(),
                     'author': name.css('span.carac.carac-autor a.info::text').extract_first(),
                     
                     }
           
       for price in response.css('.price-range'):
            yield {
                     'price': product.css('a::attr(title)').extract_first(),
                     #'image': product.css('.image img::attr(src)').extract(), 
            }
"""


        
