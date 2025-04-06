'''Problem Statement
You are given an e-commerce dataset that tracks customer transactions over several months. Your task is to:

Clean the data (handle missing values, duplicates).

Analyze key metrics:

Total number of customers

Total revenue

Average order value

Monthly active customers

Perform RFM analysis (Recency, Frequency, Monetary)

Identify the top 5% customers based on revenue.'''



###Solution###


  
import pandas as pd
import numpy as np

# Simulate dataset
data = {
    'customer_id': [101, 102, 101, 103, 104, 105, 106, 101],
    'order_id': [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5003],
    'order_date': pd.to_datetime([
        '2023-11-01', '2023-11-03', '2023-12-05', '2023-12-09',
        '2023-12-12', '2023-12-15', '2023-12-18', '2023-12-05'
    ]),
    'order_amount': [250.0, 180.0, 300.0, 150.0, 500.0, np.nan, 0.0, 300.0]
}

df = pd.DataFrame(data)

### Step 1: Data Cleaning ###
df.drop_duplicates(inplace=True)
df.dropna(subset=['order_amount'], inplace=True)

# Filter out zero-value orders if needed
df = df[df['order_amount'] > 0]

#Step 2: Basic Metrics
total_customers = df['customer_id'].nunique()
total_revenue = df['order_amount'].sum()
average_order_value = df['order_amount'].mean()

monthly_active = df.copy()
monthly_active['month'] = df['order_date'].dt.to_period('M')
monthly_active_customers = monthly_active.groupby('month')['customer_id'].nunique()

#Step 3: RFM Analysis
reference_date = pd.to_datetime('2024-01-01')
rfm = df.groupby('customer_id').agg({
    'order_date': lambda x: (reference_date - x.max()).days,
    'order_id': 'count',
    'order_amount': 'sum'
}).rename(columns={
    'order_date': 'Recency',
    'order_id': 'Frequency',
    'order_amount': 'Monetary'
})

#Step 4: Top 5% Customers by Revenue ###
top_customers = rfm.sort_values('Monetary', ascending=False)
top_5_percent = top_customers.head(max(1, int(0.05 * len(top_customers))))


