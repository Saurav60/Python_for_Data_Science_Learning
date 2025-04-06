#Problem statement
"""
Create a pivot table showing total sales by product and region.
"""
df = pd.DataFrame({
    'Product': ['A', 'A', 'B', 'B'],
    'Region': ['East', 'West', 'East', 'West'],
    'Sales': [100, 150, 200, 250]
})

print(pd.pivot_table(df, values='Sales', index='Product', columns='Region', aggfunc='sum'))
