# This is a simple case of problem-solving using pandas covering a few important questions asked in data analytics interviews.
import pandas as pd
from datetime import datetime
data = {
 'EmployeeID': [1, 2, 3, 4, 5],
 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
 'Department': ['HR', 'IT', 'IT', 'HR', 'Finance'],
 'Salary': [60000, 70000, 80000, 65000, 75000],
 'JoiningDate': ['2020-01-15', '2019-06-20', '2018-07-23', '2020-02-10', '2021-03-15'],
 'PerformanceScore': [3, 4, 2, 5, 3]
}

bonus_data = {
    'EmployeeID': [1, 2, 3, 6],
    'Bonus': [5000, 7000, 6000, 8000],
}

df2 = pd.DataFrame(bonus_data)

#Creating a 2-D dataframe in pandas
df = pd.DataFrame(data)

#Avg salary for each dept 
avg_salary_for_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_for_dept)

#employee with highest performance score in each dept 
employee_with_high_perf = df.loc[df.groupby('Department')['PerformanceScore'].idxmax()]
print(employee_with_high_perf[['Department','Name','PerformanceScore']])

#To add a new column that represents the number of years each employee has been with the company based on the joining date
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
current_date = datetime.now()
df['YearsWithCompany'] = (current_date - df['JoiningDate']).dt.days//365
print(df[['Name','JoiningDate','YearsWithCompany']])

#To create a pivot table to display the total salary and average performance score for each department.
pivot_table = pd.pivot_table(
    df,
    values = ['Salary','PerformanceScore'],
    index = 'Department',
    aggfunc={'Salary': 'sum', 'PerformanceScore': 'mean'}
)
pivot_table.rename(columns={'Salary': 'Total Salary', 'PerformanceScore': 'Avg Performance'}, inplace=True)
pivot_table.reset_index(inplace=True)
print(pivot_table)

#Employess from it department who have performance score more than 3
It_top_performers = df[(df['Department'] == 'IT') & (df['PerformanceScore'] > 3)]
print(It_top_performers)

#inner merge with another df
merged_df = pd.merge(df,df2,on='EmployeeID',how='inner')
print(merged_df[['EmployeeID','Name','Department','Salary','Bonus']])

#To calculate the cumulative sum of the PerformanceScore column grouped by Department
df['Cumulative Sum'] = df.groupby('Department')['PerformanceScore'].cumsum()
print(df[['Department','PerformanceScore','Cumulative Sum']])

#Rank employees within each department based on their Salary
df['Rank'] = df.groupby('Department')['Salary'].rank(ascending=False, method='dense')
print(df[['Name','Department','Salary','Rank']])

#Employees with company more than 2 years 
df = df[df['YearsWithCompany']>2]
print(df)
