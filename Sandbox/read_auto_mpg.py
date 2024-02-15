import pandas as pd

#%% Read file

filename = 'Opdrachten/datasets/auto-mpg.csv'

df = pd.read_csv(filename)

#%% EDA

df.info()

