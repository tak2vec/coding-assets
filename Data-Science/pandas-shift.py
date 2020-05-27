#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd


# #### df.shift(periods,axis)の使い方

# In[47]:


df = pd.DataFrame({
    "col1" : range(10),
    "col2" : [x**2 for x in range(10)],
    "col3" : [x*10 for x in range(10)],
})

df


# In[48]:


#デフォルトの場合（periods=1）
df.shift()


# In[49]:


#periods=3の場合
df.shift(periods=3)


# In[51]:


#axis=columnsを指定した場合
df.shift(axis=1)


# In[55]:


#欠損値部分を埋める場合
df.shift(periods=3,fill_value=999)


# #### ser.shift(freq="D/M")の使い方

# In[71]:


ser = pd.Series(
    index = pd.date_range(start="2020-01",periods=12,freq="M"),
    data = range(100,1300,100)
)

ser


# In[78]:


print(ser.shift(freq="3D")) #月末から3日shift
print("----------")
print(ser.shift(freq="M")) #1ヶ月shift(月末に設定される)

