#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[ ]:





# In[50]:


ary1 = np.random.randn(100,3)
ary1[:10]


# In[49]:


def calc1(ary1):
    return np.mean(ary1,axis=1)


# In[51]:


calc1(ary1)[:10]


# In[ ]:





# In[65]:


ary2 = np.random.randn(100,4)
print(ary2[:10])
print("--------")
print(ary2.shape)


# In[69]:


def calc2(ary2):
    assert ary2.shape[1] == 3 , f"特徴量の数が「{ary2.shape[1]}」となっているためエラーです。"
    return np.mean(ary2,axis=2)


# In[70]:


calc2(ary2)

