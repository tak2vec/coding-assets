#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using ViolinPlot
# ▶ File Data : Iris data of sklearn-datasets

# In[ ]:





# ###### Import Library

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

from sklearn.datasets import load_iris


# In[ ]:





# ###### Load Data

# In[2]:


dataset = load_iris()
dataset.keys()


# In[3]:


#説明変数
X = pd.DataFrame(data=dataset.data,columns=dataset.feature_names)
X.head()


# In[4]:


#ターゲット(目的変数)
y = pd.Series(data=dataset.target,name="name")
y.head()


# In[5]:


#理解用に数値をカテゴリに戻しておく
class_map = {0:"setosa",1:"versicolor",2:"virginica"}
y = y.map(class_map)
y.head()


# In[6]:


#利用データの作成
dataset = X.join(y)
dataset.head()


# In[7]:


#カラム名をシンプルにしておく
my_cols = ["sepal length","sepal width","petal length","petal width","name"]
dataset.columns = my_cols
dataset.head()


# In[ ]:





# ###### Plot Boxplot
# Petal Lengthを品種別にバイオリンプロットで可視化する

# In[8]:


lis = list(dataset.columns)[:4]
lis


# In[28]:


plt.figure(figsize=(8,6))
sns.violinplot(x=dataset.name,y=dataset[lis[2]],data=dataset)
plt.title("ViolinPlot of Iris dataset")
plt.tight_layout()


# In[18]:


plt.figure(figsize=(8,5))
sns.boxplot(x=dataset.name,y=dataset[lis[2]],data=dataset)
plt.title("Boxplot of Iris dataset")
plt.tight_layout()


# In[ ]:





# 全特徴量についてバイオリンプロットで可視化

# In[20]:


#グラフプロット用関数
def get_number(cnt):
    if cnt == 0:
        return 0,0
    elif cnt == 1:
        return 0,1
    elif cnt == 2:
        return 1,0
    else:
        return 1,1


# In[21]:


#2×2のグラフを描くためのコード
fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(10,8))

for i in range(len(lis)):
    x,y = get_number(i) #2×2グラフ用の必要値を自作関数にて取得
    sns.violinplot(x=dataset.name,y=dataset[lis[i]],data=dataset,ax=ax[x,y])
    plt.title("ViolinPlot of Iris dataset")
    fig.tight_layout()


# In[ ]:





# In[24]:


#初心者向け
plt.figure(figsize=(8,5))
sns.violinplot(x=dataset.name,y=dataset[lis[0]],data=dataset)

plt.figure(figsize=(8,5))
sns.violinplot(x=dataset.name,y=dataset[lis[1]],data=dataset)

plt.figure(figsize=(8,5))
sns.violinplot(x=dataset.name,y=dataset[lis[2]],data=dataset)

plt.figure(figsize=(8,5))
sns.violinplot(x=dataset.name,y=dataset[lis[3]],data=dataset)
plt.tight_layout()

