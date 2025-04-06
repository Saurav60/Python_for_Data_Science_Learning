#problem statement
"""
Perform left join with indicator column to track matches.
"""
#how to use join using python to join two data frames 
left = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
right = pd.DataFrame({'id': [2, 3], 'location': ['Delhi', 'Mumbai']})


merged = pd.merge(left, right, on='id', how='left', indicator=True)
print(merged)
