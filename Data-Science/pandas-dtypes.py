#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# In[44]:


data = pd.read_csv("./data/sell_prices.csv",encoding="utf-8")
display(data.head())

print(f"data's shape:{data.shape}")


# In[45]:


data.info()


# In[46]:


data.dtypes


# In[ ]:





# #### データフレームの「データ型」を抽出

# In[22]:


#指定したデータ型のカラムを抽出
cols = data.columns

for col in cols:
    col_int = data.select_dtypes(include="int64").columns #「int64」を抽出
    col_float = data.select_dtypes(include="float64").columns #「float64」を抽出

print(col_int)
print(col_float)


# In[ ]:





# #### データフレームの「数値型(int64/float64)」を変換

# In[33]:


#int64/float64のカラムのデータ型を変換
#値を保持出来る最小のデータ型に変換するため、`pd.to_numeric()`を使用

def to_numeric(df,cols):
    cols_int = df.select_dtypes(include="int64").columns
    cols_float = df.select_dtypes(include="float64").columns
    
    #int64型カラムの変換
    for col_int in cols_int:
        df[col_int] = pd.to_numeric(df[col_int],downcast="integer")
    
    #float64型カラムの変換
    for col_float in cols_float:
        df[col_float] = pd.to_numeric(df[col_float],downcast="float")
    
    return df


# In[32]:


df_ = to_numeric(data,cols)
df_.dtypes


# In[ ]:





# #### データフレームの「数値型(int64/float64)」を変換 + 圧縮データ量の確認

# In[49]:


#データサイズ(MB表示)
data.memory_usage().sum() / 1024**2


# In[50]:


#int64/float64のカラムのデータ型を変換
#値を保持出来る最小のデータ型に変換するため、`pd.to_numeric()`を使用
#データ容量の変換をウォッチ

def to_numeric_reduction(df,cols,flag=True):
    memory_start = df.memory_usage().sum() / 1024**2
    cols_int = df.select_dtypes(include="int64").columns
    cols_float = df.select_dtypes(include="float64").columns
    
    #int64型カラムの変換
    for col_int in cols_int:
        df[col_int] = pd.to_numeric(df[col_int],downcast="integer")
    
    #float64型カラムの変換
    for col_float in cols_float:
        df[col_float] = pd.to_numeric(df[col_float],downcast="float")
    
    memory_end = df.memory_usage().sum() / 1024**2
    
    if flag:
        print(f"size(start) : {memory_start:.2f} MB")
        print(f"size(end) : {memory_end:.2f} MB")
        print(f"size(reduction) : {memory_end - memory_start:.2f} MB")
    
    return df


# In[51]:


df__ = to_numeric_reduction(data,cols)
df__.dtypes


# In[ ]:




