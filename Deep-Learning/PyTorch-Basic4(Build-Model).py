#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
from torch.nn import functional as F
from torch import optim
import numpy as np


# ### モデル定義
# モジュールに基づき、自分の実現したいモデルを構築する<p>
# 畳み込み層と全結合層からなる下記CNNネットワークモデルの構築を目指す<p>
# <img src = "./data/mnist-model.jpg">

# In[4]:


class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #二次元畳み込み層の定義
        self.conv1 = torch.nn.Conv2d(in_channels=1,out_channels=20,kernel_size=5)
        self.conv2 = torch.nn.Conv2d(in_channels=20,out_channels=50,kernel_size=5)
        #全結合層の定義
        self.fc1 = torch.nn.Linear(in_features=50*4*4,out_features=500)
        self.fc2 = torch.nn.Linear(in_features=500,out_features=10)
    
    def forward(self,x): #X's shape(BN,1,28,28)
        #Conv1's forward
        x = F.relu(self.conv1(x)) # 畳み込んでrelu x: (batch_size * 20 * 24 * 24)
        x = F.max_pool2d(x,2,2) # 2x2サイズのmax-pooling x: (batch_size * 20 * 12 * 12)
        #Conv2's forward
        x = F.relu(self.conv2(x)) # 畳み込んでrelu x: (batch_size * 50 * 8 * 8)
        x = F.max_pool2d(x,2,2) # pooling x: (batch_size * 50 * 4 * 4)
        #FC1's forward
        x = x.view(-1,50*4*4) # テンソルの変形 x: (batch_size * 800)
        x = F.relu(self.fc1(x)) # 全結合層→relu x: (batch_size * 500)
        #FC2's forward
        x = self.fc2(x) # 全結合層 x: (batch_size * 10)
        
        return F.log_softmax(x,dim=1)


# In[ ]:




