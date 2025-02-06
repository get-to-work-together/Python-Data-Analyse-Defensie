from math import pi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

x_min = 0
x_max = 2
n = 1000
x = np.linspace(x_min, x_max, n)

amplitude = 2
frequency = 2   # Hz
phase = 0.5     # between 0 and 1

amplitude = st.slider('Amplitude', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
frequency = st.slider('Frequency', min_value=0.5, max_value=20.0, value=1.0, step=0.1)
phase = st.slider('Phase', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
                              
y = amplitude * np.sin(2 * pi * (x * frequency + phase))

fig, ax = plt.subplots(figsize=(14, 6))

ax.set_title('Sine wave')
ax.axhline(0, linewidth=1, color='k')
ax.plot(x, y, color='green', linewidth=3)
ax.set_xlim(x_min, x_max)
ax.set_ylim(-10, 10)
ax.grid()
ax.set_xlabel('seconds')

plt.show()
st.pyplot(fig)

data = np.vstack([x, y]).transpose()
indeces = np.random.choice(data.shape[0], size=10)
data = data[indeces]

df = pd.DataFrame({
    'x': data[:, 0],
    'y': data[:, 1],
})

# print(df)
st.dataframe(df)
