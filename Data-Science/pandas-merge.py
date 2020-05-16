#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# DataFrameの作成

# In[22]:


df_name = pd.DataFrame({
    "ID" : ["001","002","003"],
    "Name" : ["AAA","BBB","CCC"]
})

df_name


# In[23]:


df_age = pd.DataFrame({
    "ID" : ["001","002","003"],
    "Age" : [25,30,35]
})

#カラムの並び替え
df_age = df_age.iloc[:,[1,0]]
df_age


# In[24]:


df_info = pd.DataFrame({
    "Name" : ["AAA","BBB","CCC"],
    "TEL" : ["111-111-111","123-456-789","999-000-111"],
    "Mail" : ["xxx@gmail.com","yyy@gmail.com","zzz@gmail.com"]
})

#カラムの並び替え
df_info = df_info.iloc[:,[1,2,0]]
df_info


# In[ ]:





# DataFrameの結合

# In[25]:


#df_nameとdf_ageを「ID」キーで結合
df_merge1 = df_name.merge(df_age,on="ID",how="left")
df_merge1


# In[ ]:





# In[26]:


#df_merge1とdf_infoを「Name」キーで結合
df_merge2 = df_merge1.merge(df_info,on="Name",how="left")
df_merge2


# In[ ]:




