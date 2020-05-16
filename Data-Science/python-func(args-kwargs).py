#!/usr/bin/env python
# coding: utf-8

# #### 関数引数(可変長引数) | `*args`と`**kwargs`の意味

# In[11]:


#可変長引数「*args」や「**kwargs」の意味を確認
def func(*args,**kwargs):
    print(type(args))
    print(f"args : {args}")
    print("---------")
    print(type(kwargs))
    print(f"kwargs : {kwargs}")


# In[81]:


#タプルを渡してみる
func((1,2,3))


# In[82]:


#辞書型を渡してみる
func(a=1,b=2,c=3)


# In[86]:


#タプルと辞書型を渡してみる【正】
tpl = (1,2,3)
dic = {"A":1,"B":2,"C":3}

func(tpl,**dic)


# In[85]:


#タプルと辞書型を渡してみる【誤】
tpl = (1,2,3)
dic = {"A":1,"B":2,"C":3}

func(tpl,dic)


# In[ ]:





# #### 関数引数(可変長引数) | `*args`と`**kwargs`の活用方法

# In[34]:


import pandas as pd
import numpy as np
import random


# In[101]:


#タプル型を受け取って計算結果(合計値と平均値)を返す関数
def calc(*args):
    print(type(args))
    print(args) #受け取ったargs内容を確認
    print("----------")
    total = np.sum(args)
    mu = np.mean(args)
    
    return total,mu


# In[102]:


num = np.arange(1,101)
total,mu = calc(num)
print(f"合計：{total} | 平均値：{mu}")


# In[ ]:





# In[103]:


#辞書型を受け取ってデータフレームを作成する関数
def setting_df(**kwargs):
    print(type(kwargs))
    print(kwargs) #受け取ったkwargs内容を確認
    print("--------")
    df = pd.DataFrame.from_dict(kwargs)
    
    return df


# In[104]:


lis = ["python","SQL","JAVA","GO","PHP"]

mydict = {
    "ID" : np.arange(1,11),
    "Language" : [random.choice(lis) for i in range(1,11) ]
}

df = setting_df(**mydict)
df.head()


# In[ ]:




