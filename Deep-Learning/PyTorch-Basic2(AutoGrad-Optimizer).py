#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
import numpy as np


# ### 自動微分の基本
# tensorで保持したデータをもとに、誤差逆伝播により勾配を算定する

# ##### 予測値yとラベルtを用いて自動微分を理解

# In[17]:


y = torch.tensor([0.5,0.5,0.5],requires_grad=True)
t = torch.tensor([0,0.5,2],dtype=torch.float)

#MSEによりLoss算定
loss = torch.mean((y-t)*(y-t))
print(f"Loss：{loss}")
print(f"現時点の勾配：{y.grad}")
print("-----------------")

#Backward実行
loss.backward()
print(f"誤差逆伝播後の勾配：{y.grad}")

#Backward実行(2回目)
loss = torch.mean((y-t)*(y-t))
loss.backward()
print(f"誤差逆伝播(2回目)後の勾配：{y.grad}")

#勾配のクリア
y.grad.zero_()
print(f"クリア後の勾配：{y.grad}")


# In[ ]:





# ##### Optimizerによりパラメータ最適化

# In[18]:


from torch import optim
from torch.nn import functional as F


# In[30]:


y = torch.nn.Parameter(torch.tensor([0.5,0.5,0.5]))
t = torch.tensor([0,0.5,2],dtype=torch.float)

#アルゴリズムとしてSGD,学習率を0.01に設定
optimizer = optim.SGD([y],lr=0.01)

#lossをMSEで算定
loss = F.mse_loss(y,t)
print(f"loss:{loss}")
print(f"現時点の勾配：{y.grad}")
print("----------------------")

#Backward実行
loss.backward()
print(f"誤差逆伝播後の勾配：{y.grad}")

#Update Parameter
optimizer.step()
print(f"更新後パラメータ：{y}")

#勾配リセット
optimizer.zero_grad()
print(f"勾配リセット：{y.grad}")

