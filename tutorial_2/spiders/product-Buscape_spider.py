import scrapy

class ProductBuscapeSpider(scrapy.Spider):
   name = "product-buscape"
   start_urls = ['http://www.buscape.com.br/mais-vendidos/livros/administracao-e-negocios/677353G?pagina='+str(i) for i in range(1, 7)]

   
   def parse(self, response):
       
           
       for product in response.css('div.bp-wrap section.proc-search-results'):
           yield {
                     'title': product.css('.details div.description a.link div.is-truncated p.name-prd::text').extract_first(),
                     'author': product.css('.details span.carac.carac-autor a.info::text').extract_first(),
                     'price': product.css('div.price-range a::attr(title)').extract_first(),
                     #'image': product.css('.image img::attr(src)').extract(),
            }



        
