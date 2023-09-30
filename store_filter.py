import pandas as pd
# import undetected_chromedriver as uc


# separate valid stores from opening soon
store_dataframe = pd.read_excel('resource/Latefat.xlsx')
# domains = store_dataframe['comment']
# print(type(domains[28]))

# # check each domain and take shots
# for domain in domains[134:]:
#     driver = uc.Chrome(driver_executable_path='C:/Development/chromedriver.exe')
#     driver.get(url=f'https://{domain}')
#     driver.save_screenshot(filename=f'shots/{domain}.png')
#     driver.quit()

# save filtered stores in a csv file for use later
# filtered_stores = {
#     'domains': [domain for i, domain in enumerate(store_dataframe['domain']) if type(store_dataframe['comment'][i]) == float],
#     'categories': [category for i, category in enumerate(store_dataframe['categories']) if type(store_dataframe['comment'][i]) == float],
# }

filtered_stores = {
    'domains': [domain for domain in store_dataframe['domain']],
    'categories': [category for category in store_dataframe['categories']],
    'comment': ['' for domain in store_dataframe['domain']],
}

filtered_stores_dataframe = pd.DataFrame(filtered_stores)
filtered_stores_dataframe.to_csv('resource/filtered_stores_2.csv')
# print(filtered_stores_dataframe)