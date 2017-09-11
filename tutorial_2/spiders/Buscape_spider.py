import scrapy

class BuscapeSpider(scrapy.Spider):
    name = "buscape"
    start_urls = ['http://www.buscape.com.br/mais-vendidos/livros/administracao-e-negocios/677353G?pagina='+str(i) for i in range(1, 7)]
  

    def parse(self, response):
        for buscape in response.css('.details div.description'):
             yield {
                'title': buscape.css('a.link div.is-truncated p.name-prd::text').extract_first(),
                'author': buscape.css('span.carac.carac-autor a.info::text').extract_first(),
                      
             }
         #forma comprida para fazer join dos links das paginas   
           
        #next_page = response.css('.content  a.item::attr(href)').extract_first()
        #if next_page is not None:
                #yield response.follow(next_page, callback=self.parse)

     
     
     
     
      ####para fazer join dos links das paginas 
      #shortcut
   #   for a in response.css('li a'):
    #       yield response.follow(a, callback=self.parse)
     
   
