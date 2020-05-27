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


# DataFrameから行列の値を取得

# #### 特定のカラムだけを抽出｜df[col]

# In[4]:


#sepal widthの列を抽出
df["sepal width"].head()


# In[5]:


#petal lengthの列を抽出
df["petal length"].head()


# In[6]:


#複数カラムを取得[sepal length,name]
cols = ["sepal length","name"]
df[cols].head()


# In[7]:


#複数カラムを取得[name以外]
cols = df.columns[:4]
df[cols].head()


# In[ ]:





# #### 特定の行だけを抽出①｜df[True]

# In[8]:


#nameが「0」のデータのみを抽出
(df["name"] == 0).head()


# In[9]:


flag = df["name"] == 0
df[flag].tail()


# In[24]:


#flagに該当しないデータを抽出｜name=1,2
display(df[~flag].head())
display(df[~flag].tail())


# #### 特定の行だけを抽出②｜df.query(col == 'value')

# In[10]:


#nameが「1」のデータのみを抽出
df.query("name == 1").head()


# In[63]:


#pandasのvesrion確認（アップデート前）
pd.__version__


# In[11]:


#pandasのvesrion確認（アップデート後）
#カラム名のスペース(空白)を扱えるようにするため、「version0.25」以上にする
pd.__version__


# In[64]:


#sepal lengthの長さが「5.0」以上のデータを抽出
df.query("sepal length >= 5.0") #Error｜カラム名にスペースがあるため
df.query("`sepal length` >= 5.0") #Error｜vesionが古いため、` `を使えない


# In[12]:


#sepal lengthの長さが「5.0」以上のデータを抽出
df.query("`sepal length` >= 5.0") #OK｜vesion更新したため、` `を使えた


# In[14]:


#sepal lengthの長さが「？」以上のデータを抽出
#「？」には変数を用いて指定出来るようにする

thresh = 7.0
# df.query("`sepal length` >= thresh") #NG｜変数名をそのまま書いた場合
df.query("`sepal length` >= @thresh") #OK｜変数名の前に「@」をつけた場合


# In[16]:


#sepal lengthが「7.0」以上
#sepal widthが「3.5」以上
#両方の条件を満たすデータを抽出

thresh1 = 7.0
thresh2 = 3.5
df.query("`sepal length` >= @thresh1 & `sepal width` >= @thresh2") 

