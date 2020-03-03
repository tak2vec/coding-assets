#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import numpy as np


# ### ネットワークを独自にモジュール化
# 独自ネットワーク層を作成することが可能

# ##### Multipleクラスを作成
# 3次元ベクトルxと同次元重みwを乗算する処理を記載</p>
# x：[0,-1,3] | t:[0,1,2]

# In[11]:


class Multiple(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.ones(3,dtype=torch.float))
    def forward(self,x):
        assert x.shape == (3,)
        return x * self.w


# In[22]:


model = Multiple()
x = torch.tensor([0,-1,3],dtype=torch.float)
t = torch.tensor([0,1,2],dtype=torch.float)
y = model(x)
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)
loss = torch.nn.functional.mse_loss(y,t)
print(loss)
print()
print(model.w.grad)
loss.backward()
print(model.w.grad)
print(f"更新前パラメータ：{model.w}")
optimizer.step()
print(f"更新後パラメータ：{model.w}")


# ##### Multipleクラスを作成②
# 上記のクラスにさらに同次元バイアスを加算する処理を記載。モジュールのネストを実現

# In[44]:


class MultipleAndAdd(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multiple = Multiple()
        self.b = torch.nn.Parameter(torch.ones(3,dtype=torch.float))
    
    def forward(self,x):
        assert x.shape == (3,)
        x = self.multiple(x)
        return x + self.b


# In[54]:


model = MultipleAndAdd()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)
x = torch.tensor([0,-1,3],dtype=torch.float)
t = torch.tensor([0,1,2],dtype=torch.float)
y = model(x)
loss = torch.nn.functional.mse_loss(t,y)
print(f"loss:{loss}")

#Backward実施前の勾配
print(f"現時点の重み勾配：{model.multiple.w.grad}")

#Backward実施
loss.backward()
print(f"Backward後の重み勾配：{model.multiple.w.grad}")
print("----------------------")
#Parameter更新
optimizer.step()
print(f"重みw：{model.multiple.w}")
print(f"バイアスb：{model.b}")

