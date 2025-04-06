#problem Statement
#Convert long format to wide and back using melt and pivot.
df = pd.DataFrame({
    'id': [1, 1, 2, 2],
    'feature': ['height', 'weight', 'height', 'weight'],
    'value': [180, 75, 170, 68]
})

wide = df.pivot(index='id', columns='feature', values='value')
long = wide.reset_index().melt(id_vars='id', var_name='feature', value_name='value')
print(long)
