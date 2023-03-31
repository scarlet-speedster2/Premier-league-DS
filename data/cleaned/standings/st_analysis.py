import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('2022-2023.csv')

# Set the index to the "Team" column
df.set_index('Team', inplace=True)

# Create a bar plot for the "Points" column
ax = df['Points'].plot(kind='bar', figsize=(10, 6), fontsize=12)
ax.set_title('Points', fontsize=16)
ax.set_xlabel('Team', fontsize=14)
ax.set_ylabel('Points', fontsize=14)
plt.show()

# Create a bar plot for the "Goal_Diff" column
ax = df['Goal_Diff'].plot(kind='bar', figsize=(10, 6), fontsize=12)
ax.set_title('Goal Difference', fontsize=16)
ax.set_xlabel('Team', fontsize=14)
ax.set_ylabel('Goal Difference', fontsize=14)
plt.show()

# Create a bar plot for the "Win_Rate" column
ax = df['Win_Rate'].plot(kind='bar', figsize=(10, 6), fontsize=12)
ax.set_title('Win Rate', fontsize=16)
ax.set_xlabel('Team', fontsize=14)
ax.set_ylabel('Win Rate', fontsize=14)
plt.show()
