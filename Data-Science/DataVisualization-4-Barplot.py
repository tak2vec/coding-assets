#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using Barplot
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

# In[3]:


dataset = pd.read_csv("./data/flight_delays.csv",encoding="utf-8",index_col="Month")
dataset


# In[ ]:





# ###### Plot Barplot①
# 各空港会社ごとに、月別の遅延時間を棒グラフにする

# In[4]:


lis = list(dataset.columns)
lis


# In[ ]:





# In[23]:


#航空会社ごとに、月別の平均遅延時間を棒グラフ化する
for i in range(len(lis)):
    plt.figure(figsize=(10,5))
    name = lis[i]
    sns.barplot(x=dataset.index,y=dataset[name],data=dataset)
    plt.title(f"Average delay time of {name} company")
    plt.ylabel("Delay time")


# In[ ]:





# ###### Plot Barplot②
# 各空港会社ごとに、月別の遅延時間を棒グラフ(横向き)にする

# In[26]:


#航空会社ごとに、月別の平均遅延時間を棒グラフ化する
for i in range(len(lis)):
    plt.figure(figsize=(10,5))
    name = lis[i]
    sns.barplot(y=dataset.index,x=dataset[name],data=dataset,orient="h")
    plt.title(f"Average delay time of {name} company")
    plt.xlabel("Delay time")


# In[ ]:





# In[ ]:




