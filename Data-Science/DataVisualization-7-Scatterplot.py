#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using Scatterplot
# ▶ File Data : Iris data of sklearn-datasets

# In[ ]:





# ###### Import Library

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()


# In[ ]:





# ###### Load Data

# In[3]:


dataset = pd.read_csv("./data/insurance.csv",encoding="utf-8")
dataset.head()


# ###### Plot Scatterplot
# BMIとChargesの関係を散布図で可視化する

# In[4]:


lis = list(dataset.columns)
lis


# In[56]:


plt.figure(figsize=(10,5))
sns.scatterplot(x=dataset[lis[2]],y=dataset[lis[-1]],data=dataset)
plt.title("Scatterplot of relationship between BMI and charges")
plt.tight_layout()


# In[ ]:





# 散布図に回帰直線を追加する

# In[59]:


plt.figure(figsize=(10,5))
sns.regplot(x=lis[2],y=lis[-1],data=dataset)
plt.title("Scatterplot and Regression line of relationship between BMI and charges")
plt.tight_layout()


# 【ケース①】散布図を内訳別に表示する(男女別)

# In[62]:


#男女別に表示
plt.figure(figsize=(10,5))
sns.scatterplot(x=dataset[lis[2]],y=dataset[lis[-1]],hue=dataset[lis[1]],data=dataset)
plt.title("Scatterplot of relationship between BMI and charges by sex")
plt.tight_layout()


# 【ケース②】散布図を内訳別に表示する(喫煙者or Not)

# In[61]:


#Smoker別に表示
plt.figure(figsize=(10,5))
sns.scatterplot(x=dataset[lis[2]],y=dataset[lis[-1]],hue=dataset[lis[4]],data=dataset)
plt.title("Scatterplot of relationship between BMI and charges by smoker or not")
plt.tight_layout()


# In[30]:


#Smoker別に表示+回帰直線
plt.figure(figsize=(16,8))
sns.lmplot(x="bmi",y="charges",hue="smoker",data=dataset)
plt.tight_layout()

