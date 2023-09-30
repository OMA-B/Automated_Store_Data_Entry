import pandas as pd, undetected_chromedriver as uc, time, pprint, json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

categories_available = ['https://coast2coastsupplies.com/product-category/food-service-products/', 'https://coast2coastsupplies.com/product-category/laundry-department-products/', 'https://coast2coastsupplies.com/product-category/maintenance-products/page/3/', 'https://coast2coastsupplies.com/product-category/linen-and-housekeeping-products/page/5/']
# products_presented = []
# products_filtered = []
products_with_details = []


# crawl products from sites

# at first, import filtered_stores
filtered_stores = pd.read_csv('resource/filtered_stores_2.csv')
domains = filtered_stores['domains']
categories = filtered_stores['categories']
# print(domain)

# pick a store to crawl
STORE_URL = f'https://{domains[8045]}'

# visit each category and gather all products presented
for category_url in categories_available:

    products_presented = []
    products_filtered = []

    driver = uc.Chrome(driver_executable_path='C:/Development/chromedriver.exe')
    driver.get(url=category_url)
    wait = WebDriverWait(driver=driver, timeout=13)

    # try:
    #     driver.find_element(By.CSS_SELECTOR, 'a.btn.close').click()
    time.sleep(10)
    # except Exception as e: pass
    
    products = wait.until(EC.presence_of_all_elements_located(locator=(By.CSS_SELECTOR, 'div .fl-post-grid-title a')))
    for product in products[:20]:
        products_presented.append(product.get_attribute('href'))
    # driver.quit()

    print(len(products_presented))
    # extra filter to check for duplicates
    for product in products_presented:
        if product not in products_filtered:
            products_filtered.append(product)

    # visit the page of each product gathered to fetch the details needed and store in a tupled list
    # pprint.pprint(products_presented)
    for x, product_url in enumerate(products_filtered):
        print(x+1, product_url)
        time.sleep(2)
        # driver = uc.Chrome(driver_executable_path='C:/Development/chromedriver.exe', headless=True)
        # driver.get(url=product_url)
        wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, f'div:nth-child({x+1}) .fl-post-grid-title a'))).click()
        time.sleep(5)
        # gather details needed
        title = wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.fl-heading')))

        try: description = wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.woocommerce-product-details__short-description')))
        except: description = wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, 'div#tab-description')))
        
        price = wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')))
        # time.sleep(3)
        
        try: image_url = wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.wp-post-image')))
        except: image_url = wait.until(EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.zoomtoo-container img')))
        
        products_with_details.append(('Coast 2 Coast Supplies, Inc', title.text, description.text[:150], price.text.strip('$'), product_url, image_url.get_attribute('src'), categories[8045], category_url.split('.')[-1].strip('com'), STORE_URL))
        #  'Home / Science & Engineering / Nature /'
        
        with open(file='products_with_details.json', mode='w+') as file:
            json.dump(products_with_details, file)
        
        # go back to items page
        driver.back()

    driver.quit()

# convert data retrieved to dataframe and store in csv file, to be converted to excel file later
# pprint.pprint(products_with_details)
products_csv = pd.read_csv('resource/eCommerce_products.csv')
data_retrieved = {
    'IDCTG': products_csv['IDCTG'].to_list() + ['' for product in products_with_details],
    'Name': products_csv['Name'].to_list() + ['' for product in products_with_details],
    'IDCTG_Father': products_csv['IDCTG_Father'].to_list() + ['' for product in products_with_details],
    'Name.1': products_csv['Name.1'].to_list() + ['' for product in products_with_details],
    'Level': products_csv['Level'].to_list() + ['' for product in products_with_details],
    'Store ID': products_csv['Store ID'].to_list() + ['' for product in products_with_details],
    'Store Name': products_csv['Store Name'].to_list() + [product[0] for product in products_with_details],
    'Product Title': products_csv['Product Title'].to_list() + [product[1] for product in products_with_details],
    'Product Description': products_csv['Product Description'].to_list() + [product[2] for product in products_with_details],
    'Price': products_csv['Price'].to_list() + [product[3] for product in products_with_details],
    'Product Page URL': products_csv['Product Page URL'].to_list() + [product[4] for product in products_with_details],
    'Product URL Image': products_csv['Product URL Image'].to_list() + [product[5] for product in products_with_details],
    'Level 1 Category Name': products_csv['Level 1 Category Name'].to_list() + [product[6] for product in products_with_details],
    'Level 2 Category Name': products_csv['Level 2 Category Name'].to_list() + [product[7] for product in products_with_details],
    'Website URL': products_csv['Website URL'].to_list() + [product[8] for product in products_with_details],
}
data_retrieved_df = pd.DataFrame(data_retrieved)
data_retrieved_df.to_csv('resource/eCommerce_products.csv', index=False)