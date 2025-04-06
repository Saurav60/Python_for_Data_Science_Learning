"""
Remove outliers using IQR method.
"""
import numpy as np

data = pd.DataFrame({'Values': [10, 12, 14, 15, 19, 95]})
q1 = data['Values'].quantile(0.25)
q3 = data['Values'].quantile(0.75)
iqr = q3 - q1

filtered = data[(data['Values'] >= q1 - 1.5 * iqr) & (data['Values'] <= q3 + 1.5 * iqr)]
print(filtered)
