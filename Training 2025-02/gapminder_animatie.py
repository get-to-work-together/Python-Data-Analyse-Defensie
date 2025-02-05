import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import seaborn as sns

# import streamlit as st

filename = '/Users/peter/Computrain/_InCompany/Defensie/Python Data Analyse/Opdrachten/datasets/World Bank DataBank World Development Indicators/indicators_selected.csv'

df = pd.read_csv(filename)

year = 2020

df_year = df[df['Year']==year]

green = '#30ee40'
yellow = '#fee717'
red = '#fe5c75'
blue = '#5cdeee'

continent_colors = {
        'Asia': red, 
        'Europe': yellow, 
        'Africa': blue, 
        'Oceania': red, 
        'North America': green,
        'South America': green,
}

colors = df_year['Continent'].replace(continent_colors).values

scale_factor = 8000 / df['Population, total'].max()
sizes = df_year['Population, total'].values * scale_factor

fig, ax = plt.subplots(figsize=(12, 8))

ax.scatter('Fertility rate, total (births per woman)', 
           'Life expectancy at birth, total (years)', 
           data = df_year,
           c = colors,
           s = sizes,
           edgecolor = '#444',
           linewidth = 0.5,
           zorder= 10,
           label = None)

ax.set_title('World Bank Databank World Developments Indicators', fontsize=20)
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
ax.set_xticks(range(0, 10))
ax.set_yticks(range(0, 100, 10))
ax.set_xlabel('Births per woman', fontsize=16)
ax.set_ylabel('Life expectancy', fontsize=16)

ax.text(0.5, 0.35, str(year), 
        transform=ax.transAxes,
        horizontalalignment='center', verticalalignment='center',
        fontfamily='verdana', fontsize=200, color='#cfd6de')

ax.grid()

ax.set_axisbelow(True)
patches = [mpatches.Patch(color=color, label=continent) for continent, color in continent_colors.items()]
ax.legend(handles=patches)

plt.show()