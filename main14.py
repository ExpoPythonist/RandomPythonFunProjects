import pandas as pd
import matplotlib.pyplot as plt

# Simulated data: favorite colors of 100 people
data = {
    'Color': ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Black', 'White'],
    'Count': [15, 25, 10, 8, 12, 7, 5, 6, 4, 8]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 6))

# Pie Chart
plt.subplot(1, 2, 1)
plt.pie(df['Count'], labels=df['Color'], autopct='%1.1f%%', colors=plt.cm.tab10.colors)
plt.title('Favorite Colors Distribution (Pie Chart)')

# Bar Chart
plt.subplot(1, 2, 2)
plt.bar(df['Color'], df['Count'], color=plt.cm.tab10.colors)
plt.title('Favorite Colors Distribution (Bar Chart)')
plt.xlabel('Color')
plt.ylabel('Count')
plt.xticks(rotation=45)

plt.tight_layout()

# Show plot
plt.show()
