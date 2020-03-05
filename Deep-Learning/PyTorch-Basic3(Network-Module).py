#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import numpy as np


# ### ネットワークを独自にモジュール化
# 独自ネットワーク層を作成することが可能

# ##### Multipleクラスを作成
# 初期値重み：torch.ones(3)<p>
# Forward：重みと入力値xを掛け合わせた結果を返す<p>
# 入力値x：[0,-1,3] <p>
# ラベルt: [0,1,2]

# In[17]:


class Multiple(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.ones(3,dtype=torch.float))
    
    def forward(self,x):
        assert x.shape == (3,)
        return x * self.w


# In[13]:


from torch import optim
from torch.nn import functional as F


# In[25]:


x = torch.tensor([0,-1,3],dtype=torch.float)
t = torch.tensor([0,1,2],dtype=torch.float)

model = Multiple()
optimizer = optim.SGD(model.parameters(),lr=0.01)
y = model(x)
loss = F.mse_loss(t,y)
print(f"loss : {loss}")
print("-------------")
loss.backward()
print(f"重みwの勾配：{model.w.grad}")
print("-------------")
print(f"更新前パラメータ：{model.w}")
optimizer.step()
print(f"更新後パラメータ：{model.w}")


# ##### Multipleクラスを作成②
# 上記のクラスにさらに同次元バイアスを加算する処理を記載。モジュールのネストを実現

# In[26]:


class MultipleAndAdd(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multiple = Multiple()
        self.b = torch.nn.Parameter(torch.ones(3,dtype=torch.float))
    
    def forward(self,x):
        assert x.shape == (3,)
        return self.multiple(x) + self.b


# In[30]:


model = MultipleAndAdd()
optimizer = optim.SGD(model.parameters(),lr=0.01)
y = model(x)
loss = F.mse_loss(t,y)
print(f"loss:{loss}")
print("-----------")

loss.backward()
print(f"重みwの勾配：{model.multiple.w.grad}")
print(f"バイアスbの勾配：{model.b.grad}")
print("-----------")
optimizer.step()
print(f"更新後重みwパラメータ：{model.multiple.w}")
print(f"更新後バイアスbパラメータ：{model.b}")

