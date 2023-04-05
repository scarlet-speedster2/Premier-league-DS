import csv
import matplotlib.pyplot as plt
import sys



season = sys.argv[1]

# Read the data from the CSV file

with open(season) as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Extract the data into separate lists
teams = [d["Team"] for d in data]
points = [int(d["Points"]) for d in data]
goal_diff = [int(d["Goal_Diff"]) for d in data]
win_rate = [float(d["Win_Rate"]) for d in data]

# Create the scatter plot
plt.scatter(points, goal_diff, s=[w * 500 for w in win_rate], alpha=0.5)
plt.xlabel("Points")
plt.ylabel("Goal Difference")

# Add team names as labels
for i in range(len(teams)):
    plt.annotate(teams[i], xy=(points[i], goal_diff[i]), xytext=(10, 5), textcoords='offset points', ha='left', va='bottom')

# Show the plot
plt.show()

