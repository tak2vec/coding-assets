#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# DataFrameの作成

# In[4]:


df1 = pd.DataFrame({
    "Col1" : ["A","B","C"],
    "Col2" : [1,2,3]
})

df1


# In[5]:


df2 = pd.DataFrame({
    "Col1" : ["D","E","F"],
    "Col2" : [4,5,6]
})

df2


# In[6]:


df3 = pd.DataFrame({
    "Col3" : ["X","Y","Z"],
    "Col4" : [10,20,30]
})

df3


# In[ ]:





# DataFrameの結合(行方向)

# In[7]:


#df1とdf2を行方向に結合
df12 = pd.concat([df1,df2])
df12


# In[ ]:





# DataFrameの結合(列方向)

# In[10]:


#df1とdf3を列方向に結合
df13 = pd.concat([df1,df3],axis=1)
df13


# In[11]:


df13_mis = pd.concat([df1,df3])
df13_mis


# In[ ]:




