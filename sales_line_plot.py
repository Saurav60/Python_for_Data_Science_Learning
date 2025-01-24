#here we learn how to perform basic EDA of given sales dataset using python.
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('sales_data.csv')

# Describe data
print(df.describe())

# Plot trends
df.groupby('month')['sales'].sum().plot(kind='line')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
