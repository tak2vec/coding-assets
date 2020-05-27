#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("./data/titanic-train.csv",encoding="utf-8")
data.head()


# In[19]:


#Sexに「male」が含まれているか確認
# data["Sex"].isin("male") #[]がないとError
data["Sex"].isin(["male"])


# In[20]:


#「male」だけの行を抽出
flag = data["Sex"].isin(["male"])
data[flag].head()


# In[29]:


#Survived「1(生存者)」のみを確認
data["Survived"].isin([1])


# In[30]:


#Survived「1(生存者)」のみを抽出
flag = data["Survived"].isin([1])
data[flag].head()


# In[ ]:





# #### 「isin」を使うケース

# In[79]:


#日付データを用意
s1 = pd.Series(pd.date_range(start="2020-01-01",periods=366),name="Date")
s2 = pd.Series([f"day-{i}" for i in range(1,367)],name="day-N")
df = pd.concat([s1,s2],axis=1)
df["weekday1"] = df["Date"].dt.day_name() #【参考】曜日を表示
df["weekday2"] = df["Date"].dt.dayofweek #「0-Monday」~「6-Sunday」

df.head(10)


# In[ ]:





# In[78]:


#週末flagを作る場合を想定
flag = df["weekday2"].isin([5,6]) 
df["weekend_flag"] = flag.astype(int)
df.head()


# In[ ]:




