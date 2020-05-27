#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np


# In[ ]:





# Series型の作成

# In[7]:


#Series作成の基本
ser = pd.Series([100,200,300])
ser


# In[47]:


ary = np.array([100,200,300])
print(ary)


# In[ ]:





# In[32]:


#Series作成（index/name指定）
ser1 = pd.Series([100,200,300],index=["Jan","Feb","Mar"],name="Shop A")
ser1


# In[34]:


#Series作成（辞書型の利用）
sale_by_month = {"Jan":100,"Feb":200,"Mar":300}

ser2 = pd.Series(sale_by_month,name="Shop A")
ser2


# In[38]:


#データタイプの確認
chk = lambda x : type(x)
for ser in [ser1,ser2]:
    print(ser)
    print(f"タイプ：{chk(ser)}")
    print("--------------")


# In[ ]:





# DataFrame型とSeries型の比較

# In[27]:


#DataFrameの作成
sale_by_shop = {
    "Shop A" : [100,200,300],
    "Shop B" : [400,500,600]
}

df = pd.DataFrame(sale_by_shop,index=["Jan","Feb","Mar"])
df


# In[43]:


#DataFrameの切り出し
df["Shop A"]


# In[46]:


#データ型の確認
display(df)
print(chk(df))
print("-------------")
display(df["Shop A"])
print(chk(df["Shop A"]))


# In[ ]:




