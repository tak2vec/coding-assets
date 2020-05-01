#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using Line Charts
# ▶ File Data : spotify.csv

# In[ ]:





# ###### Import Library

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()


# In[ ]:





# ###### Load File

# In[2]:


dataset = pd.read_csv("./data/spotify.csv",encoding="utf-8",index_col="Date",parse_dates=True)
dataset.head()


# In[3]:


dataset.tail()


# In[ ]:





# ###### Plot Line Charts①

# In[6]:


plt.figure(figsize=(13,6))
sns.lineplot(data=dataset)


# In[9]:


print(sns.__version__)


# ###### Plot Line Charts②
# Choose 2 Columns

# In[7]:


lis = list(dataset.columns)
lis


# In[8]:


plt.figure(figsize=(13,6))
sns.lineplot(data=dataset[lis[0]],label=lis[0])
sns.lineplot(data=dataset[lis[1]],label=lis[1])
plt.title("Global Daily Streams on Spotify from 2017 to 2018")
plt.xlabel("Date")


# In[ ]:




