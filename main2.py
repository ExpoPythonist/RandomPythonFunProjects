import matplotlib.pyplot as plt

def visualize_water_consumption(daily_goal, water_intake):
    days = range(1, len(water_intake) + 1)
    plt.plot(days, water_intake, marker='o', color='b', label='Water Intake')
    plt.plot(days, [daily_goal] * len(water_intake), linestyle='--', color='r', label='Daily Goal')
    plt.title("Daily Water Consumption")
    plt.xlabel("Day")
    plt.ylabel("Water Intake (ml)")
    plt.xticks(days)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example data: water intake for a week (ml)
water_intake = [2000, 1800, 2200, 2500, 2300, 2100, 2400]
daily_goal = 2000  # Daily water consumption goal (ml)

visualize_water_consumption(daily_goal, water_intake)
