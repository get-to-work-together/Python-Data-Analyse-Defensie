import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

sns.set(style="darkgrid")


csvfile='/Users/jdvlot/Downloads/7052_95_UntypedDataSet_03052020_113458.csv'

df=pd.read_csv(csvfile, sep=';')

print(df)

#re = (df.Perioden == '2017JJ00') | (df.Geslacht == 4000)
#print (df[re])

#reb = df.Perioden == '2015JJ00'
#print(df[reb])

findL = [10010, 51300, 70200, 70300, 70400, 70500, 70600,70700, 70800, 70900, 71000, 71100, 71200, 71300, 71400, 71500, 71600, 71700, 71800, 71900]
replaceL=['0', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94']
col = 'Leeftijd'
df[col] = df[col].replace(findL, replaceL)



print(df[col])

findL = [ 3000, 4000]
replaceL=['Man', 'Vrouw']
coln= 'Geslacht'
df[coln] = df['Geslacht'].replace(findL, replaceL)



print(df[coln])

df['Perioden'] = df['Perioden'].str[:-4]
#rec = (df.Leeftijd == '45-49') & df['k_216KwNvLeverEnIntrahGalwegen_15']
#print(df[rec])

#red = df[['Geslacht', 'Leeftijd', 'Perioden', 'k_216KwNvLeverEnIntrahGalwegen_15']] [:5]

#print(red)
# Subset on males and compute their median age
mannen = df[df['Geslacht'] == "Man"]
#median_male_age = male_churn['Age'].median()


#print (df.loc)
# Subset on females and compute their median age
vrouwen = df[df['Geslacht'] == "Vrouw"]
#median_female_age = female_churn['Age'].median()

alle=df.groupby(('Perioden', 'Geslacht')).agg(np.sum)
alle.reset_index(inplace=True)
print(alle.head())
#print (df[['Geslacht', 'Perioden']])

#sns.countplot(x='Perioden', data=df, hue='Geslacht')

#figure, axes= plt.subplot(nrows=3, ncolsn= 1, figsize=(28,16))


fig, axes = plt.subplots(3,1, figsize = (25,8), sharex=True)
#axes = plt.subplots(3,1, figsize = (12,8))

for ax in fig.axes:
    matplotlib.pyplot.sca(ax)
    plt.xticks(rotation=90)

sns.catplot("Perioden", "k_41Suikerziekte_33", "Geslacht", data=alle, kind="bar", height=6, aspect=2, palette="muted",legend=True , ci=None, ax= axes[0])
# axes[0].set_yticks([])
# axes[0].set_xlabel([])
# plt.xticks(rotation=90)
#ax=axes[1]

sns.catplot("Perioden", "k_41Suikerziekte_33", "Leeftijd", data=mannen, kind="bar", height=6, aspect=2, palette="muted", legend=True ,ci=None, ax=axes[1] )
#axes[1].set_yticks([])
#axes[1].set_xlabel([])
#plt.xticks(rotation=90)

sns.catplot("Perioden", "k_41Suikerziekte_33", "Leeftijd", data=vrouwen, kind="bar", height=6, aspect=2, palette="muted", legend=False , ci=None, ax=axes[2])
#axes[2].set_yticks([])
#axes[2].set_xlabel('Perioden', fontsize = 12, fontweight = 'semibold')
#plt.xticks(rotation=90)

#sns.despine(bottom=True)
axes[1].legend(fontsize = 'x-small',bbox_to_anchor=(1.0, 1.0))
axes[2].legend(fontsize = 'x-small',bbox_to_anchor=(1.0, 1.0))
plt.show()

#legend=False