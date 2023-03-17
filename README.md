# cltv_analysis_with_python

## Calculating Customer Life Time Value

1. Data Preparation
2. Average Order Value        - Average Order Value = Total Price / Total Transaction
3. Purchase Frequency         - Purchase Frequency = Total Transaction / Total Number of Customer
4. Repeat Rate & Churn Rate   - Repeat Rate = Number of Customer Making Multiple Purchases / Total Number of Customer &
                              - Churn Rate = 1 - Repeat Rate
5. Profit Margin              - Profit Margin = Total Price * 0.1
6. Customer Value             - Customer Value = Average Order Value * Purchase Frequency
7. Customer Lifetime Value    - Customer Life Time Value = (Customer Value / Churn Rate) * Profit Margin
8. Segmentation

## The dataset named "Online Retail II" includes the sales of an UK-based online store between 01/12/2009 - 09/12/2011.
dataset: https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

Variables
* **Invoice:** Invoice number. The unique number of each transaction, namely the invoice. If it starts with C, it shows the canceled invoice
* **StockCode:** A 5-digit integral number uniquely assigned to each distinct product.
* **Description:** Product description
* **Quantity:** The quantities of each product (item) per transaction.
* **InvoiceDate:** The day and time when a transaction was generated.
* **UnitPrice:** Product price (in GBP)
* **CustomerID:** Unique customer number
* **Country:** The name of the country where a customer resides.

