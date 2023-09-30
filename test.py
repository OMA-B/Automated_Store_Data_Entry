# import undetected_chromedriver as uc, time, pprint
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


# products_with_details = []


# # driver = uc.Chrome(driver_executable_path='C:/Development/chromedriver.exe')
# # driver.get(url='https://duckduckgo.com/')
# # time.sleep(2)
# # driver.find_element(By.CSS_SELECTOR, '.searchbox_input__bEGm3').send_keys('https://gadgets1202.myshopify.com/collections/headphones-earphones/products/p595-ac5002-stereo-headset-singlecomboplug', Keys.ENTER)
# # time.sleep(2)
# # driver.find_element(By.CSS_SELECTOR, '.eVNpHGjtxRBq_gLOfGDr.LQNqh2U1kzYxREs65IJu').click()
# # time.sleep(2)

# driver = uc.Chrome(driver_executable_path='C:/Development/chromedriver.exe')
# driver.get(url='https://gadgets1202.myshopify.com/collections/car-gadget')
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, 'a.btn.close').click()
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, '.grid__item:nth-child(7) > div > div.product-container > a').click()
# time.sleep(2)

# # gather details needed
# title = driver.find_element(By.CSS_SELECTOR, '.product-single__title')
# description = driver.find_element(By.CSS_SELECTOR, '.product-description.rte')
# price = driver.find_element(By.CSS_SELECTOR, '#ProductPrice .money')
# image_url = driver.find_element(By.CSS_SELECTOR, '#product-featured-image')
# products_with_details.append(('Techy Supply', title.text, description.text[:150], price.text, image_url.get_attribute('src'), '/collections/headphones-earphones'))
# # category_url.split('.')[2].strip('com')

# pprint.pprint(products_with_details)

# driver.back()

# driver.find_element(By.CSS_SELECTOR, '.grid__item:nth-child(2) > div > div.product-container > a').click()
# time.sleep(2)

# # gather details needed
# title = driver.find_element(By.CSS_SELECTOR, '.product-single__title')
# description = driver.find_element(By.CSS_SELECTOR, '.product-description.rte')
# price = driver.find_element(By.CSS_SELECTOR, '#ProductPrice .money')
# image_url = driver.find_element(By.CSS_SELECTOR, '#product-featured-image')
# products_with_details.append(('Techy Supply', title.text, description.text[:150], price.text, image_url.get_attribute('src'), '/collections/headphones-earphones'))
# # category_url.split('.')[2].strip('com')

# pprint.pprint(products_with_details)

# driver.back()

# time.sleep(5)

# driver.quit()

print(len('''
    REFURBISHED ITEM - HP ENVY Laptop 13-ba1093cl (TOUCHSCREEN), Windows 11 Home 64-Bit, Intel Core i5-1135G7 Quad-Core Processor 2.40GHz, 16GB DDR4-2933 
'''))