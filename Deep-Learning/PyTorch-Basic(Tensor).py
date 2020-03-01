#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
import numpy as np


# ### torch.Tensorの基本
# Tensor(変数)の使い方

# ##### 手動で作成

# In[6]:


a = torch.tensor([[1,2,3],[4,5,6]])
a


# ##### よく使う関数

# In[29]:


#zeros関数
a = torch.zeros([3,3])
print(a)
print("-----------------------------")
#ones関数
b = torch.ones([3,3])
print(b)
print("-----------------------------")
#dtypeの指定
c1 = torch.tensor([[1,2],[3,4]],dtype=torch.float) 
print(c1)
c2 = torch.tensor([[1,2],[3,4]],dtype=torch.float64)
print(c2)
print("-----------------------------")
#arange関数
d = torch.arange(10)
print(d)
print("-----------------------------")
#ガウス分布からの乱数生成
e = torch.randn([3,3])
print(e)
print("-----------------------------")
#Tensorのshape取得
print(e.size())


# ##### GPUデバイスが使用可能である場合、GPU上で変数作成

# In[12]:


if torch.cuda.is_available():
    gpu = torch.device("cuda")
    cpu = torch.device("cpu")
    x = torch.zeros((4,4),device=gpu)
    print(x)
else:
    cpu = torch.device("cpu")
    x = torch.ones((4,4),device=cpu)
    print(x)


# ##### NumpyとTensorの変換

# In[35]:


#Numpyの作成
ary = np.array([1,2,3])
print(ary)

#Numpy⇒Tensor
x = torch.from_numpy(ary)
print(x)

#Tensor⇒Numpy
print(x.numpy())


# ##### Tensorの中身を書き換え

# In[38]:


a = torch.tensor([[1,2,3],[4,5,6]])
print(a)
a.zero_()
print(a)


# In[ ]:





# In[ ]:




