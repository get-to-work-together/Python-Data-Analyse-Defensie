#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[35]:


x = np.linspace(0.1, 15, 100)


# In[13]:


y = np.sin(2*x) / x


# In[36]:


plt.figure(figsize=(14, 5))

for i in range(10):
    plt.plot(x, i * y)

plt.legend(['A','B','C','D','E','F','G','H','I','J'])

ax = plt.gca()
ax.set_facecolor("orange")

plt.title('aantal versus meters')
plt.xlabel('meters')
plt.ylabel('aantal')

plt.show()


# In[ ]:




