import pandas as pd, json

with open('products_with_details.json') as file:
    products_with_details = json.load(file)

# convert data retrieved to dataframe and store in csv file, to be converted to excel file later
# print(len(products_with_details))

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