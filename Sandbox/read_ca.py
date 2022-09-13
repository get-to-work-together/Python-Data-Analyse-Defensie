import pandas as pd

df = pd.read_csv('ca-500.csv')

df['full_name'] = df['first_name'] + ' ' + df['last_name']
print(df.loc[df['city']=='Montreal', ['first_name','last_name', 'full_name', 'city']])
