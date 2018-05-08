# to run file in powershell: scrapy runspider -o "books.csv(or json) 
#whatever your file name/type" you want to create
#then your file (in this case: book_scraper.py)
#so, -----> scrapy runspider -o books.csv book_scraper.py
import scrapy

class BookSpider(scrapy.Spider):
	name = 'bookspider'
	start_urls = ['http://books.toscrape.com']

	def parse(self, response):
		for article in response.css('article.product_pod'):
			yield {
				'price': article.css(".price_color::text").extract_first(),
				'title': article.css("h3 > a::attr(title)").extract_first()
			}
			next = response.css(".next > a::attr(href").extract_first()
			if next:
				yield response.follow(next, self.parse)