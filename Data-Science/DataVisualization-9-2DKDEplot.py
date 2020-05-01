#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using 2D KDE plot
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





# ###### Plot 2D KDE plot①
# `Petal Length`と`Sepal Width`を2D KDEとして描画する

# In[9]:


lis = list(dataset.columns)[:4]
lis


# In[24]:


plt.figure(figsize=(10,20))
sns.jointplot(x=dataset[lis[2]],y=dataset[lis[1]],data=dataset,kind="kde")
plt.tight_layout()


# In[52]:


#kindを指定しなかった場合（デフォルト時）
plt.figure(figsize=(10,20))
sns.jointplot(x=dataset[lis[2]],y=dataset[lis[1]],data=dataset)
plt.tight_layout()


# In[ ]:





# ###### Plot Histgram②
# `Petal Length`と`Sepal Width`を種別に2D KDEにする

# データの分割

# In[25]:


#種別にデータを分割
dat_setosa = dataset.query("name == 'setosa'")
dat_versicolor = dataset.query("name == 'versicolor'")
dat_virginica = dataset.query("name == 'virginica'")
dat_lis = [dat_setosa,dat_versicolor,dat_virginica]


# In[ ]:





# (任意)データの確認

# In[26]:


def check_data(data):
    res = set(data.name)
    if len(res) == 1:
        print(f"No problem | {res}")
    else:
        print(f"Error | {res}")


# In[27]:


for i in range(3):
    check_data(dat_lis[i])


# In[ ]:





# `petal length`と`sepal width`を種別に2D KDE化

# In[51]:


#効率的なコード
plt.figure(figsize=(10,5))

for i in range(3):
    dat = dat_lis[i]
    sns.jointplot(x=dat[lis[2]],y=dat[lis[1]],data=dat,kind="kde")
    plt.title(f"Plot of {set(dat.name)}")


# In[ ]:





# In[41]:


#初心者向け
plt.figure(figsize=(12,6))

sns.jointplot(x=dat_setosa["petal length"],y=dat_setosa["sepal width"],kind="kde")
sns.jointplot(x=dat_versicolor["petal length"],y=dat_versicolor["sepal width"],kind="kde")
sns.jointplot(x=dat_virginica["petal length"],y=dat_virginica["sepal width"],kind="kde")


# In[ ]:




