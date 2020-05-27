#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
from sklearn.datasets import load_iris


# In[82]:


#Irisデータセットの格納
dataset = load_iris()

X = pd.DataFrame(dataset.data,columns=dataset.feature_names)
t = pd.Series(dataset.target,name="name")
class_map = {0:"setosa",1:"versicolor",2:"virginica"}
t = t.map(class_map)

data = X.join(t)
data.head(10)


# In[70]:


#グループ化しただけでは内容が確認出来ない
data.groupby(["name"])


# In[67]:


#「name」ごとの要約統計量|平均を表示
data.groupby(["name"]).mean()


# In[86]:


#「name」ごとの要約統計量|中央値を表示
data.groupby(["name"]).median()


# In[69]:


#「name」ごとの要約統計量|合計を表示
data.groupby(["name"]).sum()


# In[85]:


#「name」ごとの要約統計量|分散を表示
data.groupby(["name"]).var()


# In[71]:


#「name」ごとの要約統計量|標準偏差を表示
data.groupby(["name"]).std()


# In[72]:


#「name」ごとの要約統計量|最大値を表示
data.groupby(["name"]).max()


# In[73]:


#「name」ごとの要約統計量|最小値を表示
data.groupby(["name"]).min()


# In[76]:


#「name」ごとのカウントも可能
data.groupby(["name"]).count()


# In[81]:


#「name」ごとの要約統計量を一気に表示
data.groupby(["name"]).describe().T


# In[ ]:




