import matplotlib.pyplot as plt
import pandas as pd 
data = {
    'date': ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01"],
    'Revenue': [5000,6000,7000,8000,90000]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['Revenue'], marker='o', color='b', label='Revenue')
plt.title('Revenue Trends over time', fontsize=14)
plt.xlabel('Date', fontsize =12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()