

def remove_goal_scores(final_path):
    print("Removing Goal Scores...")
    df = pd.read_csv(final_path)
    df = df.drop(columns=['FTHG','FTAG'])
    df.to_csv(final_path, index=False)



def save_new_data_to_database(database_path, final_data_file, prediction_results_file, standing_predictions_file,
                          final_data_file_name='previous_results', prediction_results_file_name='prediction_results',
                          standing_predictions_file_name='prediction_rankings'):
    conn = sqlite3.connect(database_path)
    
    previous_results_df = pd.read_csv(final_data_file)
    previous_results_df = previous_results_df[["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]]
    previous_results_df = previous_results_df.loc[(previous_results_df['FTHG'] != 0) | 
                            (previous_results_df['FTAG'] != 0) | 
                            ((previous_results_df['FTR'] != 'A') & 
                                (previous_results_df['FTR'] != 'H'))]
    
    prediction_results_df = pd.read_csv(prediction_results_file)
    prediction_results_df = prediction_results_df[["Date", "HomeTeam", "AwayTeam", "FTR", "prob_A", "prob_D", "prob_H"]]
    prediction_results_df = prediction_results_df.loc[prediction_results_df['prob_A'].notna()]
    
    standing_result_df = pd.read_csv(standing_predictions_file)
    
    previous_results_df.to_sql(final_data_file_name, con=conn, if_exists='replace')
    prediction_results_df.to_sql(prediction_results_file_name, con=conn, if_exists='replace')
    standing_result_df.to_sql(standing_predictions_file_name, con=conn, if_exists='replace')


def save_summary_to_database(database_path, best_clf_average, winner):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS summary')
    cur.execute('CREATE TABLE summary (time DATE, accuracy NUMBER, winner TEXT)')
    cur.execute('INSERT INTO summary (time, accuracy, winner) VALUES (?, ?, ?)', 
                (dt.now().strftime('%Y-%m-%d'), best_clf_average, winner))
    conn.commit()
