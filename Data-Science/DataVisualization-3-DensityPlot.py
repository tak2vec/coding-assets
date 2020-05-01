#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using Density Plot and Kdeplot
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





# ###### Plot Density①
# Petal Lengthをヒストグラムにする

# In[8]:


lis = list(dataset.columns)[:4]
lis


# In[12]:


plt.figure(figsize=(12,6))
sns.kdeplot(dataset[lis[2]],shade=True)
plt.title("Density of Petal Length")


# In[39]:


plt.figure(figsize=(12,6))
sns.distplot(dataset[lis[2]],kde=True)


# In[ ]:





# ###### Plot Density②
# Petal Lengthを種別にヒストグラムにする

# データの分割

# In[13]:


#種別にデータを分割
dat_setosa = dataset.query("name == 'setosa'")
dat_versicolor = dataset.query("name == 'versicolor'")
dat_virginica = dataset.query("name == 'virginica'")
dat_lis = [dat_setosa,dat_versicolor,dat_virginica]


# In[ ]:





# (任意)データの確認

# In[14]:


def check_data(data):
    res = set(data.name)
    if len(res) == 1:
        print(f"No problem | {res}")
    else:
        print(f"Error | {res}")


# In[15]:


for i in range(3):
    check_data(dat_lis[i])


# In[ ]:





# petal lengthを種別にヒストグラム化

# In[19]:


#効率的なコード
plt.figure(figsize=(12,6))

for i in range(3):
    dat = dat_lis[i]
    sns.kdeplot(dat[lis[2]],shade=True,label=set(dat.name))
    plt.title("Density of petal length for each type of flower")
    plt.legend()


# In[29]:


#効率的なコード
plt.figure(figsize=(12,6))

for i in range(3):
    dat = dat_lis[i]
    sns.distplot(dat[lis[2]],kde=True,label=dat.name)
    plt.title("Histgram of petal length for each type of flower")
    plt.legend()


# In[ ]:





# In[31]:


#初心者向け
plt.figure(figsize=(12,6))

sns.distplot(dat_setosa["petal length"],kde=True,label="setosa")
sns.distplot(dat_versicolor["petal length"],kde=True,label="versicolor")
sns.distplot(dat_virginica["petal length"],kde=True,label="virginica")
plt.legend()


# In[ ]:




