#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# ###### Tidy Case1 ~ Column is not Variable(メイン軸1つ | Value軸1つ)

# In[3]:


dat1 = pd.read_csv("./data/tidy-data-sample1.csv",encoding="utf-8")
dat1


# In[4]:


dat1_tidy = pd.melt(
    frame = dat1,
    id_vars= "Name",
    value_vars=None,
    var_name= None,
    value_name= "Amount")

dat1_tidy


# In[ ]:





# ###### Tidy Case2 ~ Column is not Variable(メイン軸2つ | Value軸1つ)

# In[5]:


dat2 = pd.read_csv("./data/tidy-data-sample2.csv",encoding="utf-8")
dat2


# In[11]:


dat2_tidy = pd.melt(
    frame = dat2,
    id_vars= ["YE","Month"],
    value_vars=None,
    var_name="Product",
    value_name="Sales")

dat2_tidy.head()


# In[18]:


#Product別売上
dat2_product = dat2_tidy.groupby(["YE","Month","Product"]).sum()
dat2_product.head()


# In[22]:


#月別売上高
dat2_month = dat2_tidy.groupby(["YE","Month"]).mean()
dat2_month


# In[ ]:





# ###### Tidy Case3 ~ Column is not Variable(メイン軸2つ | Value軸3つ)

# In[7]:


dat3 = pd.read_csv("./data/tidy-data-sample3.csv",encoding="utf-8")
dat3.head()


# In[8]:


dat3_tidy = pd.melt(
    frame = dat3,
    id_vars= ["YE","Month"],
    value_vars= ["Sales","Cogs","Ratio"],
    var_name= "Name",
    value_name='value')

dat3_tidy.head()


# In[17]:


import numpy as np

x = np.arange(len(dat3_tidy))
perm = np.random.permutation(x)

dat3_tidy.iloc[perm,:].head()


# In[ ]:





# In[18]:


import pandas as pd


# ###### Messy Data | 雑然データ

# In[24]:


data = pd.read_csv("./data/tidy-data-sample2.csv",encoding="utf-8")
data.head()


# In[ ]:





# ###### Change to Tidy Data | 整然データ

# In[25]:


data_tidy = pd.melt(
    frame = data,
    id_vars= ["YE","Month"],
    value_vars=None,
    var_name=None,
    value_name='value',
    col_level=None,)

data_tidy


# In[ ]:





# In[ ]:





# In[ ]:




