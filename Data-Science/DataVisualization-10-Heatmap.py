#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using HeatMap
# ▶ File Data : flight_delays.csv

# In[ ]:





# ###### Import Library

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()


# In[ ]:





# ###### Load Data

# In[2]:


dataset = pd.read_csv("./data/flight_delays.csv",encoding="utf-8",index_col="Month")
dataset


# In[ ]:





# ###### Plot HeatMap
# 各空港会社ごとに、月別の遅延時間をヒートマップにする

# In[3]:


lis = list(dataset.columns)
lis


# In[ ]:





# In[12]:


#航空会社ごとに、月別の平均遅延時間をヒートマップ化する
plt.figure(figsize=(12,6))
sns.heatmap(data=dataset,annot=True)
plt.title("Heatmap of average arriving delay time")
plt.xlabel("American Flight Company")
plt.tight_layout()


# In[ ]:





# ###### Plot HeatMap②
# 各空港会社ごとに、月別の遅延時間をヒートマップ化する<br>
# 好きなヒートマップの色合いを見つける

# In[18]:


#https://matplotlib.org/3.1.3/tutorials/colors/colormaps.html
cmap_type = ["coolwarm","hot","plasma","PiYG",'PRGn', 'BrBG', 
             'PuOr', 'RdGy', 'RdBu','RdYlBu', 'RdYlGn', 'Spectral', 'bwr', 'seismic']

for i in range(len(cmap_type)):
    plt.figure(figsize=(10,5))
    sns.heatmap(data=dataset,annot=True,cmap=cmap_type[i])
    plt.title(f"Heatmap of using Type {cmap_type[i]}")
    plt.xlabel("American Flight Company")
    plt.tight_layout()


# In[ ]:




