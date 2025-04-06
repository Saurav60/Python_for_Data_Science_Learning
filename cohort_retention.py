'''Problem:
You’re analyzing customer retention. Create a cohort matrix where rows = cohort month, columns = months since first purchase, and values = % retained.'''

# Sample data
df = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 1, 2, 3, 5],
    'purchase_date': pd.to_datetime(['2023-01-01', '2023-01-05', '2023-02-10', '2023-02-15',
                                     '2023-02-25', '2023-03-05', '2023-03-10', '2023-04-01'])
})
df['cohort_month'] = df.groupby('user_id')['purchase_date'].transform('min').dt.to_period('M')
df['order_month'] = df['purchase_date'].dt.to_period('M')
df['cohort_index'] = (df['order_month'] - df['cohort_month']).apply(attrgetter('n'))

#cohort matrix
cohort_counts = df.groupby(['cohort_month', 'cohort_index'])['user_id'].nunique().unstack(1)
cohort_sizes = cohort_counts.iloc[:, 0]
retention = cohort_counts.divide(cohort_sizes, axis=0).round(2)

print(retention.fillna(0))
