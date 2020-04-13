#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# データ作成(欠損値なし）

# In[2]:


df1 = pd.DataFrame([
    ["001","Red",1000],
    ["002","Blue",1500],
    ["003","Green",2000]],
    columns = ["ID","Color","Price"])

df1


# In[ ]:





# データ作成(欠損値あり）

# In[4]:


df2 = pd.DataFrame([
    ["001","Red",1000],
    ["002","Blue",1500],
    ["003","Green",2000],
     ["004",None,3000]],
    columns = ["ID","Color","Price"])

df2


# In[ ]:





# One-hot Encoding(欠損値なし)

# In[5]:


df1_ohe = pd.get_dummies(df1,columns=["Color"])
df1_ohe


# In[ ]:





# One-hot Encoding(欠損値あり)

# In[8]:


df2_ohe = pd.get_dummies(df2,columns=["Color"],dummy_na=True)
df2_ohe


# In[ ]:




