import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('2022-2023.csv')

team_name = 'Man United'
team_data = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)]

team_data['GoalsScored'] = team_data.apply(lambda row: row['FTAG'] if row['AwayTeam'] == team_name else row['FTHG'], axis=1)
team_data['GoalsConceded'] = team_data.apply(lambda row: row['FTHG'] if row['AwayTeam'] == team_name else row['FTAG'], axis=1)
team_data['Result'] = team_data.apply(lambda row: 'Win' if (row['FTR'] == 'H' and row['HomeTeam'] == team_name) or (row['FTR'] == 'A' and row['AwayTeam'] == team_name) else ('Draw' if row['FTR'] == 'D' else 'Loss'), axis=1)

opponent_data = team_data.groupby('AwayTeam' if team_data['HomeTeam'].iloc[0] == team_name else 'HomeTeam').agg({'GoalsScored': 'mean', 'GoalsConceded': 'mean', 'Result': pd.Series.mode})

fig, ax = plt.subplots()
ax.bar(opponent_data.index, opponent_data['GoalsScored'], label='Goals Scored')
ax.bar(opponent_data.index, opponent_data['GoalsConceded'], label='Goals Conceded')
ax.set_title(f'{team_name} vs. Opponents')
ax.set_xlabel('Opponent')
ax.set_ylabel('Goals')
ax.legend()
plt.xticks(rotation=90)
plt.show()




