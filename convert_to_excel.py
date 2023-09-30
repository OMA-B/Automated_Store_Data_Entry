import pandas as pd, time, pprint


# convert product excel file to csv
# result_csv_df = pd.read_excel('resource/result/Fiverr_eCommerce_Upload_Template_15-08-23.xlsx')
# result_csv_df.to_csv('eCommerce_Upload_Template.csv', index=False)


# convert product csv file to excel
result_csv_df = pd.read_csv('resource/eCommerce_products.csv')
result_csv_df.to_excel('resource/Fiverr_eCommerce_Upload_Template_22-09-23.xlsx', index=False)


# data_retrieved = {
#     'IDCTG': result_csv_df['IDCTG'].to_list(),
#     'Name': result_csv_df['Name'].to_list(),
#     'IDCTG_Father': result_csv_df['IDCTG_Father'].to_list(),
#     'Name.1': result_csv_df['Name.1'].to_list(),
#     'Level': result_csv_df['Level'].to_list(),
#     'Store ID': result_csv_df['Store ID'].to_list(),
#     'Store Name': result_csv_df['Store Name'].to_list(),
#     'Product Title': result_csv_df['Product Title'].to_list(),
#     'Product Description': [description[:150] for description in descriptions],
#     'Price': result_csv_df['Price'].to_list(),
#     'Product Page URL': result_csv_df['Product Page URL'].to_list(),
#     'Product URL Image': result_csv_df['Product URL Image'].to_list(),
#     'Level 1 Category Name': result_csv_df['Level 1 Category Name'].to_list(),
#     'Level 2 Category Name': result_csv_df['Level 2 Category Name'].to_list(),
#     'Website URL': result_csv_df['Website URL'].to_list(),
# }
# data_retrieved_df = pd.DataFrame(data_retrieved)
# data_retrieved_df.to_excel('resource/Fiverr_eCommerce_Upload_Template_15-08-23.xlsx', index=False)

