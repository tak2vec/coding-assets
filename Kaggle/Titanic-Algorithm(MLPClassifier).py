#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import Library
import numpy as np
import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# In[9]:


dataset_train = pd.read_csv("./data/train.csv",encoding="utf-8")
dataset_test = pd.read_csv("./data/test.csv",encoding="utf-8")
print(f"train's shape:{dataset_train.shape}")
print(f"test's shape:{dataset_test.shape}")


# In[5]:


dataset_train.head()


# In[7]:


X = dataset_train.iloc[:,2:].drop(["Name","Ticket","Cabin"],axis=1)
y = dataset_train.iloc[:,1]
X.head()


# In[8]:


ohe_columns = ["Pclass","Sex","Embarked"]
X_ohe = pd.get_dummies(X,columns=ohe_columns,dummy_na=True)
X_ohe.head()


# In[10]:


imp = SimpleImputer(strategy="median")
imp.fit(X_ohe,y)

X_ohe2 = pd.DataFrame(imp.transform(X_ohe),columns=X_ohe.columns)
X_ohe2.head()


# In[11]:


X_ohe2.isnull().sum()


# In[19]:


params_grid = {   
    "hidden_layer_sizes" : [(100),(100,100),(100,100,100)],
    "alpha" : [0.0001,0.001,0.01],
    "batch_size" : [16,32,64,128],
    "learning_rate_init" : [0.01,0.001],
    "early_stopping" : [False,True]}

gs = GridSearchCV(
    estimator = MLPClassifier(),
    param_grid = params_grid,
    scoring="accuracy",
    cv= 10)

gs.fit(X_ohe2,y)


# In[20]:


print(gs.best_params_)
print(gs.best_score_)


# In[22]:


passenger_id = dataset_test.iloc[:,0]
X_test = dataset_test.iloc[:,1:].drop(["Name","Ticket","Cabin"],axis=1)
X_test.head()


# In[25]:


X_test_ohe = pd.get_dummies(X_test,columns=ohe_columns,dummy_na=True)
X_test_ohe.head()


# In[26]:


X_test_ohe2 = pd.DataFrame(imp.transform(X_test_ohe),columns=X_test_ohe.columns)
X_test_ohe2.isnull().sum()


# In[27]:


y_test = gs.predict(X_test_ohe2)
y_test


# In[29]:


df = pd.DataFrame(y_test,columns=["Survived"])
df = pd.concat([passenger_id,df],axis=1)
df.to_csv("gender_submission.csv",index=False)


# In[ ]:




