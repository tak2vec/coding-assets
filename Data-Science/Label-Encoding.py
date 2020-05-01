#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder


# In[ ]:





# ##### 欠損値がない場合

# In[79]:


#仮データの作成
df1 = pd.DataFrame(
    [["001","Red",100.0,"A"],
    ["002","Blue",200.0,"B"],
    ["003","Green",300.0,"C"],
    ["004","Yellow",400.0,"D"],
    ["005","Silver",500.0,"E"]],
    columns = ["ID","Color","Price","Rank"]
)

df1


# In[80]:


#カテゴリ変数はそれぞれ5種類ずつ存在
#Label Encoding処理によって、0-4までが作成される
print(set(df1.Color))
print(set(df1.Rank))


# In[81]:


#カテゴリ変数ごとにLabel Encoding処理
le = LabelEncoder()
df1["Color"] = le.fit_transform(df1["Color"])
df1["Rank"] = le.fit_transform(df1["Rank"])

df1


# In[82]:


#カテゴリ変数のカラムを指定して自作関数で一気に処理
def encode_categorical(df,cols):
    for col in cols:
        le = LabelEncoder()
        df[col] = pd.Series(le.fit_transform(df[col]))
    
    return df

df1_encoded = encode_categorical(df1,cols=["Color","Rank"])
df1_encoded


# In[ ]:





# ##### 欠損値がある場合

# In[93]:


import random

#100行分のデータを持つ仮データを作成
lis_color = ["Red","Blue","Green",None]
lis_price = [100.0,200.0,300.0,400.0,500.0]
lis_rank = ["A","B","C","D","E",None]

col1 = pd.Series([i for i in range(100)],name="ID")
col2 = pd.Series([random.choice(lis_color) for i in range(100)],name="Color")
col3 = pd.Series([random.choice(lis_price) for i in range(100)],name="Price")
col4 = pd.Series([random.choice(lis_rank) for i in range(100)],name="Rank")

df2 = pd.concat([col1,col2,col3,col4],axis=1)
print(f"df2's shape : {df2.shape}")
print(f"df2's null : 合計{df2.isnull().sum().sum()}個の欠損値")
df2.head()


# In[95]:


#欠損値のないデータを対象に変換
not_null = df2["Color"][df2["Color"].notnull()]
df2["Color"] = pd.Series(le.fit_transform(not_null),index=not_null.index)
df2.head()


# In[97]:


#カテゴリ変数のカラムを指定して自作関数で一気に処理
def encode_categorical2(df,cols):
    for col in cols:
        le = LabelEncoder()
        not_null = df[col][df[col].notnull()]
        df[col] = pd.Series(le.fit_transform(not_null),index=not_null.index)
    
    return df

df2_encoded = encode_categorical2(df2,cols=["Color","Rank"])
df2_encoded.head()


# In[99]:


#欠損値も含めてLabel Encoding処理した場合
df2_if = encode_categorical(df2,cols=["Color","Rank"])
df2_if.head()

