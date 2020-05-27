#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris


# In[2]:


def set_dataframe():
    dataset = load_iris()
    X = pd.DataFrame(dataset.data,columns=dataset.feature_names)
    X.columns = ["sepal length","sepal width","petal length","petal width"]
    t = pd.Series(dataset.target,name="name")

    df = X.join(t)
    return df


# In[3]:


df = set_dataframe()
df.head()


# #### DataFrameから特定の行を削除｜df.drop(index,axis=0)

# In[6]:


#index「3」だけを削除
df.drop(index=3,axis=0).head()


# In[14]:


#index「1+3x」を削除
df.drop(range(1,100,3),axis=0).head(10)


# In[ ]:





# #### DataFrameから特定の列を削除｜df.drop(columns,axis=1)

# In[17]:


#カラム名「name」を削除
df.drop("name",axis=1).head()


# In[18]:


#カラム名(name)は削除されていない
df.head()


# In[19]:


#カラム名(name)を削除した状態にしたい場合
#方法①：変数に格納
df1 = df.drop("name",axis=1)
df1.head()


# In[21]:


#カラム名(name)を削除した状態にしたい場合
#方法②：drop引数の「inplace」をTrueにする

display(df.head()) #変更前「name」が存在する
print("---------")
df.drop("name",axis=1,inplace=True)
df.head() #変更後「name」が存在しない


# In[24]:


#複数カラムの削除
cols = ["sepal length","sepal width"]
df.drop(cols,axis=1).head()

