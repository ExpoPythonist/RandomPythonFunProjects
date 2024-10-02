import pandas as pd
import matplotlib.pyplot as plt

# Simulated data: coffee orders at a coffee shop
data = {
    'Coffee Type': ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha', 'Macchiato'],
    'Orders': [150, 200, 120, 180, 90, 110]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 6))

# Pie Chart
plt.subplot(1, 2, 1)
plt.pie(df['Orders'], labels=df['Coffee Type'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Coffee Orders Distribution (Pie Chart)')

# Bar Chart
plt.subplot(1, 2, 2)
plt.bar(df['Coffee Type'], df['Orders'], color=plt.cm.Paired.colors)
plt.title('Coffee Orders Distribution (Bar Chart)')
plt.xlabel('Coffee Type')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)

plt.tight_layout()

# Show plot
plt.show()
