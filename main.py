import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data from the CSV file
df = pd.read_csv('sales_data.csv')

# Calculate the total sales for each month
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Visualize the monthly sales using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(monthly_sales['Month'], monthly_sales['Sales'], color='skyblue')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Data')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
