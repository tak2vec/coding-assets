#!/usr/bin/env python
# coding: utf-8

# ### Data Visualization by using Categorical Scatterplot
# ▶ File Data : insurance.csv

# In[ ]:





# ###### Import Library

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()


# In[ ]:





# ###### Load Data

# In[2]:


dataset = pd.read_csv("./data/insurance.csv",encoding="utf-8")
dataset.head()


# ###### Plot Categorical Scatterplot
# BMIとChargesの関係をカテゴリカル散布図で可視化する

# In[3]:


lis = list(dataset.columns)
lis


# 【ケース①】カテゴリカル散布図を内訳別に表示する(男女別)

# In[12]:


#男女別に表示
plt.figure(figsize=(10,5))
sns.swarmplot(x=dataset[lis[1]],y=dataset[lis[-1]],data=dataset)
plt.title("Categorical Scatterplot of charges by sex")
plt.tight_layout()


# 【ケース②】散布図を内訳別に表示する(喫煙者or Not)

# In[21]:


#Smoker別に表示
plt.figure(figsize=(10,5))
sns.swarmplot(x=dataset[lis[4]],y=dataset[lis[-1]],data=dataset)
plt.title("Categorical Scatterplot of charges by smoker")
plt.tight_layout()


# In[22]:


#Smoker+男女別に表示
plt.figure(figsize=(10,5))
sns.swarmplot(x=dataset[lis[4]],y=dataset[lis[-1]],hue=dataset[lis[1]],data=dataset)
plt.title("Categorical Scatterplot of charges by smoker and sex")
plt.tight_layout()


# In[23]:


#Smoker+Children別に表示
plt.figure(figsize=(10,5))
sns.swarmplot(x=dataset[lis[3]],y=dataset[lis[-1]],hue=dataset[lis[4]],data=dataset)
plt.title("Categorical Scatterplot of charges by children and smoker")
plt.tight_layout()

