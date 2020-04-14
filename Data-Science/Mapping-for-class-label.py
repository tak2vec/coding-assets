#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# 必要データの作成

# In[7]:


df = pd.DataFrame([
    ["001","AAA",25,100,"N"],
    ["002","BBB",30,200,"N"],
    ["003","CCC",35,300,"Y"]],
    columns = ["ID","Name","Age","Income","Loan_Result"])

df


# In[13]:


#説明変数と目的変数に分割
X = df.drop(["Loan_Result"],axis=1) #今回使わないデータ
y = df.iloc[:,-1] #今回使うデータ
y #Series型


# In[ ]:





# マッピングデータの作成

# In[8]:


class_mapping = {"Y":1,"N":0}


# In[ ]:





# ラベルに対するマッピング処理の実行

# In[14]:


y = y.map(class_mapping)
y


# In[ ]:




