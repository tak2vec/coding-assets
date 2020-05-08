#!/usr/bin/env python
# coding: utf-8

# In[21]:


#必要ライブラリのインポート
import pandas as pd
import numpy as np


# #### DataFrameの作成① | ゼロベースで作成

# In[63]:


pd.DataFrame([
    ["AAA",111],
    ["BBB",222]
])


# In[27]:


# 3*2のデータフレームを作成
df1 = pd.DataFrame([
    ["A",100],
    ["B",200],
    ["C",300]],
    columns = ["Col1","Col2"])

df1


# In[28]:


#2*3のデータフレームを作成
df2 = pd.DataFrame([
    ["A",100,"OK"],
    ["B",200,"NG"]],
    columns = ["Col1","Col2","Col3"]
)

df2


# In[ ]:





# #### DataFrameの作成② | 辞書型の利用

# In[15]:


df3 = pd.DataFrame({
    "Col1" : ["A","B"],
    "Col2" : [100,200],
    "Col3" : ["OK","NG"]
})

df3


# In[64]:


#既存の辞書を利用する場合
my_dict = {
    "Col1":["A","B"],
    "Col2":[100,200],
    "Col3":["OK","Good"]
}

my_dict


# In[19]:


df4 = pd.DataFrame.from_dict(my_dict)
df4


# In[ ]:





# #### DataFrameの作成③ | Numpyの利用

# In[30]:


#3×2の乱数を作成
random = np.random.randn(3,2)
random


# In[53]:


df5 = pd.DataFrame(random,columns=["Col1","Col2"])
df5


# In[ ]:





# #### DataFrameの作成④ | 時間要素の追加

# In[56]:


t = pd.date_range(start="20200508",end="20200512",name="Date")
df6 = pd.DataFrame(t)
df6

