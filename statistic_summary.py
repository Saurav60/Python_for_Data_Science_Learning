import pandas as pd 
data = {
    'Name' : ['Saurav','Gaurav','Mahesh','david'],
    'Age'  : [25,36,28,32],
    'Salary': [100000,90000,120000,70000],
    'Department': ['IT','HR','IT','HR']
}
df = pd.DataFrame(data)
numeric_summary = df.describe()
#print(numeric_summary)
full_summary = df.describe(include='all')
print(full_summary)