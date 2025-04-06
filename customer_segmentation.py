# Problem:
#Perform Recency, Frequency, Monetary (RFM) segmentation for e-commerce users.
today = pd.to_datetime("2023-12-31")

df = pd.DataFrame({
    'user_id': [1, 1, 2, 3, 3, 3],
    'order_date': pd.to_datetime(['2023-12-01', '2023-12-15', '2023-10-10', '2023-09-01', '2023-11-25', '2023-12-10']),
    'order_amount': [200, 250, 300, 100, 150, 180]
})

rfm = df.groupby('user_id').agg({
    'order_date': lambda x: (today - x.max()).days,
    'user_id': 'count',
    'order_amount': 'sum'
}).rename(columns={
    'order_date': 'Recency',
    'user_id': 'Frequency',
    'order_amount': 'Monetary'
})
print(rfm)
