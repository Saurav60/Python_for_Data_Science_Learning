#here we learn how to create a barchart for sales by category using matplotlib library of python 
import matplotlib.pyplot as plt

# Bar chart of sales by category
df.groupby('category')['sales'].sum().plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

#here df is a dataframe containing sales and category columns
