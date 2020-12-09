import scrapy
import bs4
# Import DangdangItem from items that is in upper file, so add .. before items 
from ..items import DangdangItem
# Define a subclass that inherits functions from Spider class
class DangdangSpider(scrapy.Spider):
    # Add property name
    name = 'Dangdang'
    # Limit domains so that crawler would avoid irrelevant urls
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    # Use for loop to append 4 targeted urls to start_urls
    for x in range(1,4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(x)
        start_urls.append(url)
    # Define parse function
    def parse(self, response):
        # parse response using BeautifulSoup
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # Extract values in <li> under <ul, class_="bang_list clearfix bang_list_mode">
        elements = soup.find('ul', class_="bang_list clearfix bang_list_mode").find_all('li')
        
        for element in elements:
            # Create a DangdangItem instance
            item = DangdangItem()
            # Extract book name and assign it to name property under DangdangItem class
            item['name'] = element.find('div', class_="name").find('a')['title']
            # Extract author name and assign it to author property under DangdangItem class
            item['author'] = element.find('div', class_="publisher_info").text
            # Extract price and assign it to price property under DangdangItem class
            item['price'] = element.find('div', class_="price").find('span', class_="price_n").text
            yield item
