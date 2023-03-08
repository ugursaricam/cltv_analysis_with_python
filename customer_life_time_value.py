# Calculating Customer Life Time Value

# 1. Data Preparation
# 2. Average Order Value        - Average Order Value = Total Price / Total Transaction
# 3. Purchase Frequency         - Purchase Frequency = Total Transaction / Total Number of Customer
# 4. Repeat Rate & Churn Rate   - Repeat Rate = Number of Customer Making Multiple Purchases / Total Number of Customer &
#                               - Churn Rate = 1 - Repeat Rate
# 5. Profit Margin              - Profit Margin = Total Price * 0.1
# 6. Customer Value             - Customer Value = Average Order Value * Purchase Frequency
# 7. Customer Lifetime Value    - Customer Life Time Value = (Customer Value / Churn Rate) * Profit Margin
# 8. Segmentation

# The dataset named "Online Retail II" includes the sales of an UK-based online store between 01/12/2009 - 09/12/2011.
# dataset: https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Variables
# InvoiceNo     :Invoice number. The unique number of each transaction, namely the invoice. If it starts with C, it shows the canceled invoice
# StockCode     :Unique number for each product
# Description   :Product description
# Quantity      :It expresses how many of the products on the invoices have been sold.
# InvoiceDate   :Invoice date and time
# UnitPrice     :Product price (in GBP)
# CustomerID    :Unique customer number
# Country       :Country where the customer lives

##########################################
# 1. Data Preparation
##########################################

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_ = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2009-2010')
df = df_.copy()

df.head()
df.isnull().sum()
df.dropna(inplace=True)

df = df[~df['Invoice'].str.contains('C', na=False)]

df.describe().T

df['TotalPrice'] = df['Quantity'] * df['Price']
df.head()

cltv_c = df.groupby('Customer ID').agg({'Invoice': lambda x: x.nunique(),
                                        'Quantity': lambda x: x.sum(),
                                        'TotalPrice': lambda x: x.sum()})

cltv_c.columns = ['total_transaction', 'total_unit', 'total_price']

##########################################
# 2. Average Order Value (average_order_value = total_price / total_transaction)
##########################################

total_price = cltv_c['total_price']
total_transaction = cltv_c['total_transaction']
cltv_c['average_order_value'] = total_price / total_transaction

##########################################
# 3. Purchase Frequency (purchase_frequency = total_transaction / total_number_of_customers)
##########################################

total_transaction = cltv_c['total_transaction']
total_number_of_customers = cltv_c.shape[0]
cltv_c['purchase_frequency'] = total_transaction / total_number_of_customers

##########################################
# 4. Repeat Rate (repeat_rate = number_of_customer_making_multiple_purchases / total_number_of_customers
# & Churn Rate (Churn Rate = 1 - Repeat Rate)
##########################################

number_of_customer_making_multiple_purchases = cltv_c[cltv_c['total_transaction'] > 1].shape[0]
total_number_of_customers = cltv_c.shape[0]
repeat_rate = number_of_customer_making_multiple_purchases / total_number_of_customers

churn_rate = 1 - repeat_rate

##########################################
# 5. Profit Margin (profit_margin =  total_price * 0.10)
##########################################

total_price = cltv_c['total_price']
cltv_c['profit_margin'] = total_price * 0.10

##################################################
# 6. Customer Value (customer_value = average_order_value * purchase_frequency)
##################################################

average_order_value = cltv_c['average_order_value']
purchase_frequency = cltv_c['purchase_frequency']

cltv_c['customer_value'] = average_order_value * purchase_frequency

##################################################
# 7. Customer Lifetime Value (CLTV = (customer_value / churn_rate) * profit_margin)
##################################################

customer_value = cltv_c['customer_value']
profit_margin = cltv_c['profit_margin']

cltv_c['cltv'] = (customer_value / churn_rate) * profit_margin]

cltv_c.sort_values(by='cltv', ascending=False).head()

cltv_c['total_price'].max()

##################################################
# 8. Segmentation
##################################################

cltv_c['segment'] = pd.qcut(cltv_c['cltv'], 4, labels=['D', 'C', 'B', 'A'])

# Customer ID
# 18102.00000       A
# 14646.00000       A
# 14156.00000       A
# 14911.00000       A
# 13694.00000       A

cltv_c.groupby('segment').agg({'count', 'mean', 'sum'})

cltv_c.to_csv('cltv_c.csv')
