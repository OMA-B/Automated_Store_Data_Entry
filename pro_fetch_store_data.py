import pandas as pd, undetected_chromedriver as uc, time, pprint, json
from selenium.webdriver.common.by import By

categories_available = ['https://thebrickbattle.com/lego-guns-sets', 'https://thebrickbattle.com/lego-tanks-sets', 'https://thebrickbattle.com/lego-ww2-sets', 'https://thebrickbattle.com/lego-military-army-sets', 'https://thebrickbattle.com/lego-swat-team-sets', 'https://thebrickbattle.com/lego-soldiers', 'https://thebrickbattle.com/lego-soldiers/page/2']
products_with_details = []

# crawl products from sites

# at first, import filtered_stores
filtered_stores = pd.read_csv('resource/filtered_stores_2.csv')
domains = filtered_stores['domains']
categories = filtered_stores['categories']
# print(domain)

# pick a store to crawl
STORE_URL = f'https://{domains[492]}'


# visit each category and gather all products presented
for category_url in categories_available:

    # products_presented = []
    # products_filtered = []

    driver = uc.Chrome(driver_executable_path='C:/Development/chromedriver.exe')
    driver.get(url=category_url)

    time.sleep(30/2)
    
    products = driver.find_elements(By.CSS_SELECTOR, '.woocommerce-loop-product__title .woocommerce-LoopProduct-link.woocommerce-loop-product__link')
    prices = driver.find_elements(By.CSS_SELECTOR, 'span.price')
    # descriptions = driver.find_elements(By.CSS_SELECTOR, '.box-excerpt.is-small')
    images = driver.find_elements(By.CSS_SELECTOR, '.attachment-woocommerce_thumbnail.size-woocommerce_thumbnail')

    for i, product in enumerate(products):
        # gather details needed        
        products_with_details.append(('BRICK BATTLE', product.text, product.text[:150], prices[i].text.split('$')[-1], product.get_attribute('href'), images[i].get_attribute('src'), categories[492], category_url.split('.')[1].strip('com'), STORE_URL))
        #  '/product-category/wedding-gift/'
    
    driver.quit()
    
    with open(file='products_with_details.json', mode='w+') as file:
        json.dump(products_with_details, file)
