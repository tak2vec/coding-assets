#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Library
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


# In[3]:


dataset_train = pd.read_csv("./data/train.csv",encoding="utf-8")
dataset_test = pd.read_csv("./data/test.csv",encoding="utf-8")
dataset_train.head()


# In[4]:


X = dataset_train.iloc[:,2:].drop(["Name","Ticket","Cabin"],axis=1)
y = dataset_train.iloc[:,1]
X.head()


# In[5]:


ohe_columns = ["Pclass","Sex","Embarked"]
X_ohe = pd.get_dummies(X,columns=ohe_columns,dummy_na=True)
X_ohe.head()


# In[6]:


imp = SimpleImputer()
imp.fit(X_ohe,y)

X_ohe2 = pd.DataFrame(imp.transform(X_ohe),columns=X_ohe.columns)
X_ohe2.isnull().sum()


# In[7]:


grid_params = {
    "max_depth" : [3,4,6,8,10],
    "learning_rate" : [0.1,0.05,0.01,0.001],
    "n_estimators" : [100,200,300]}

gs = GridSearchCV(
    estimator = XGBClassifier(),
    param_grid = grid_params,
    scoring= "accuracy",
    cv= 20)

gs.fit(X_ohe2,y)


# In[8]:


print(gs.best_params_)
print(gs.best_score_)


# In[9]:


dataset_test.head()


# In[10]:


passenger_id = dataset_test.iloc[:,0]
X_test = dataset_test.iloc[:,1:].drop(["Name","Ticket","Cabin"],axis=1)
X_test.head()


# In[11]:


X_test_ohe = pd.get_dummies(X_test,columns=ohe_columns,dummy_na=True)
X_test_ohe.head()


# In[12]:


X_test_ohe.isnull().sum()


# In[13]:


X_test_ohe2 = pd.DataFrame(imp.transform(X_test_ohe),columns=X_test_ohe.columns)
X_test_ohe2.isnull().sum()


# In[16]:


print(X_ohe2.shape)
print(X_test_ohe2.shape)


# In[14]:


y_test = gs.predict(X_test_ohe2)
y_test


# In[20]:


df = pd.DataFrame(y_test,columns=["Survived"])
df = pd.concat([passenger_id,df],axis=1)
df.to_csv("gender_submission.csv",index=False)

