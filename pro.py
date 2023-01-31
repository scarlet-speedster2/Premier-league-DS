import pandas as pd

df = pd.read_csv('data.csv',sep='|',index_col=False,on_bad_lines='skip',
                            names=['#','Club','Club.1','Unnamed: 3','W','D','L','Goals','+/-','Pts'])

print(df)
df.to_csv()
