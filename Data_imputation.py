'''Problem:
You’re analyzing transaction data from different stores. Some purchase_amount entries are missing. Instead of filling with a global value, impute using the median value per store.'''
import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame({
    'store_id': ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
    'purchase_amount': [250, np.nan, 300, 400, np.nan, 600, 620]
})

# Fill Nan with median value within each store
df['purchase_amount'] = df.groupby('store_id')['purchase_amount']\
                          .transform(lambda x: x.fillna(x.median()))

print(df)
