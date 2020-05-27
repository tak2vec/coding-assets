#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[53]:


def set_DataFrame():
    df = pd.DataFrame({
        "id" : ["001","002","003"],
        "name" : ["XX","YY","ZZ"],
        "life_food" : [100000,85000,50000], #1か月当たりの生活費(食費)
        "life_hobby" : [50000,10000,30000], #1か月当たりの生活費(趣味)
        "life_study" : [30000,10000,1000],  #1か月当たりの生活費(勉強代)
    })

    df = df.iloc[:,[0,-1,1,2,3]]
    return df


# In[54]:


#初期状態のDataFrame
df = set_DataFrame()
df


# In[ ]:





# カラム(特徴量)の追加①

# In[55]:


#1か月あたり生活費(Total)を追加
df["life_total"] = df["life_food"] + df["life_hobby"] + df["life_study"]
df


# In[56]:


#1か月30日と仮定して、1日当たりの平均支出額を追加
df["life_total_per_day"] = df["life_total"] / 30
df


# In[ ]:





# カラム(特徴量)の追加②

# In[61]:


#DataFrameの初期化
df = set_DataFrame()
df


# In[62]:


#assignの使い方
df.assign(test=1)


# In[63]:


#assignの使い方
df.assign(test="loading")


# In[67]:


life_total = df["life_food"] + df["life_hobby"] + df["life_study"]
df.assign(life_total=life_total)


# In[68]:


df


# In[69]:


df = df.assign(life_total=life_total)
df


# In[70]:


life_total_per_day = df["life_total"] / 30
df = df.assign(life_total_per_day = life_total_per_day)
df


# In[ ]:




