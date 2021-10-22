import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/sim-karty',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.quantity_page)

    def quantity_page(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        # product_quantity = response.css('span.goods-count span').extract()
        # product_quantity = product_quantity[-1].split(' ')
        # for find_count in product_quantity:
        #     if len(find_count.split('\n')) != 1:
        #         product_quantity = find_count.split('\n')[1]
        #         break
        # product_quantity = int(product_quantity)
        # count_page = product_quantity // 10
        # if product_quantity % 10 > 0:
        #     count_page += 1
        # new_response = self.get_products(count_page)
        section_responses = response.css('ul.breadcrumbs__list li.breadcrumbs__item')
        section = []
        for section_response in section_responses:
            section.append(section_response.css('a.breadcrumbs__link span::text').get())
        products = response.css('div.product-card')
        for product in products:
            RPC = product.css('::attr(id)').get()
            print('RPC', RPC)
            URL = product.css('a.product-card__main::attr(href)').get()
            print('URL', URL)
            TITLE = product.css('span.goods-name::text').get()
            print('TITLE', TITLE)
            SECTION = section
            print('SECTION', SECTION)
        print('########################################################################################')
        print(len(products), SECTION, len(section_responses))

    def get_products(self, urls):
        url = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/sim-karty'
        products = scrapy.Request(url=url, callback=self.get_product)
        print('#####################')
        print(products)
        # products = products.css('div')
        # products = self.get_product(products)
        # print(products)

        print('#####################')
        return products

    def get_product(self, request_products):
        request_products = request_products.css('div')
        yield 'gfg'
